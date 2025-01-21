#!/usr/bin/python3

import pprint
import subprocess
import psutil
import os.path
import glob
import yaml
import json
import time
import statistics
import argparse
import numpy

from collections import defaultdict


# ---------------------------------------
# Terminal colors
# ---------------------------------------
class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def parse_arguments():
    parser = argparse.ArgumentParser(description='Run benchmarks')
    parser.add_argument(
        'action',
        type=str,
        help='Action to perform',
        choices=['run', 'results']
    )
    parser.add_argument(
        '--times',
        type=int,
        default=5,
        help='Number of times to run each benchmark'
    )
    parser.add_argument(
        '--languages',
        type=str,
        nargs='+',
        help='Languages to run (subdirectories under langs/)',
    )
    parser.add_argument(
        '--scripts',
        type=str,
        nargs='+',
        help='Scripts to run (otherwise all scripts in config will run)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print additional debug information, including final commands'
    )
    return parser.parse_args()


def load_configurations(languages):
    configurations = []
    if languages:
        for language in languages:
            configurations += (
                glob.glob(f'langs/{language}/benchmark.yml') +
                glob.glob(f'langs/{language}/benchmark.yaml')
            )
    else:
        configurations = (
            glob.glob('langs/*/benchmark.yml') +
            glob.glob('langs/*/benchmark.yaml')
        )
    configurations.sort()
    return configurations


def load_configuration(filename, config_directory):
    """
    Loads a YAML configuration like the one you provided for PHP:
      - top-level 'versions' array for commands that don't specify their own
      - command-specific 'versions' that override the default
      - multiple 'files' entries
    Returns a list of runs, each run being a dict with the final command string fully substituted.
    """
    with open(filename, 'r') as f:
        conf = yaml.safe_load(f)

    config_title = conf['title']
    matrix = conf['strategy']['matrix']
    
    # The global default versions
    global_versions = matrix.get('versions', [])

    commands = matrix.get('command', [])
    files = matrix.get('files', [])
    global_exclude = matrix.get('exclude', [])  # List of exclude rules

    runs = []

    for script in files:
        # We'll assume it's just a string like "primes/Simple.php"
        # so we can build the script_title easily
        script_title = os.path.splitext(script)[0]

        # Build the full path to the file, so {file} can be replaced
        # if your code expects an absolute path, do os.path.abspath here
        full_script_path = os.path.join(config_directory, script)

        for cmd_info in commands:
            # Each cmd_info might have its own versions or rely on global_versions
            command_versions = cmd_info.get('versions', global_versions)
            
            # If no versions, we can treat as [None] to create one run
            if not command_versions:
                command_versions = [None]
            
            command_str_template = cmd_info['command']
            command_title = cmd_info['title']

            # For each version in either the command's own or the global list
            for version in command_versions:
                final_command = command_str_template

                # If version is set and the template has {version}, replace it
                if version and '{version}' in final_command:
                    final_command = final_command.replace('{version}', str(version))

                # If {file} is present, replace it with the actual file path
                if '{file}' in final_command:
                    final_command = final_command.replace('{file}', full_script_path)

                run_def = {
                    'config_title': config_title,
                    'script_file': script,  # or full_script_path if you prefer
                    'script_title': script_title, 
                    'command_title': command_title,
                    'command_str': final_command,
                    'version': str(version) if version else None
                }

                # If there are tags in the command, you might store them here
                if 'tags' in cmd_info:
                    run_def['tags'] = cmd_info['tags']

                runs.append(run_def)

    if global_exclude:
        runs = [r for r in runs if not is_excluded(r, global_exclude)]

    return runs

def is_excluded(run_def, exclude_list):
    """
    Returns True if run_def matches ANY rule in exclude_list.
    """
    for rule in exclude_list:
        if rule_matches(run_def, rule):
            return True
    return False


def rule_matches(run_def, rule):
    """
    Check if all specified keys in 'rule' match the corresponding fields in 'run_def'.
    Example rule: { command: 'gcc', file: 'collatz/MaxSequence' }
    We compare run_def['command_title'] and run_def['script_file'] accordingly.
    """
    # Must match *all* fields in the rule to be considered a match.
    for key, value in rule.items():
        if key == 'file':
            if run_def.get('script_file') != value:
                return False
        elif key == 'command':
            if run_def.get('command_title') != value:
                return False
        elif key == 'version':
            # If your rule might say version: 16, compare strings or convert both
            if str(run_def.get('version', '')) != str(value):
                return False
        else:
            # If you add more fields, handle them here
            return False
        
    return True

def normalize_command_info(cmd_info):
    if isinstance(cmd_info, str):
        cmd_info = {
            'title': cmd_info,
            'command': cmd_info,
            'versions': [],
        }
    if 'versions' not in cmd_info:
        cmd_info['versions'] = []
    if 'title' not in cmd_info:
        cmd_info['title'] = cmd_info['command']
    return cmd_info


def prepare_configurations(configuration_files):
    print(TerminalColors.HEADER + 'Preparing configurations...' + TerminalColors.ENDC)

    for cfg_file in configuration_files:
        directory = os.path.dirname(cfg_file)
        makefile_path = os.path.join(directory, 'Makefile')

        if os.path.isfile(makefile_path):
            print(f'\tMaking {directory}')
            result_clean = subprocess.run(['make', 'clean'], cwd=directory, shell=True, stdout=subprocess.DEVNULL)
            result_build = subprocess.run(['make', 'all'], cwd=directory, shell=True, stdout=subprocess.DEVNULL)

            if result_clean.returncode != 0 or result_build.returncode != 0:
                print(
                    TerminalColors.WARNING +
                    f'\tWarning: Makefile build failed for {directory}, continuing...' +
                    TerminalColors.ENDC
                )


def run_benchmark(command_str, verbose=False):
    """
    Executes command_str, measuring:
    - Total elapsed time (script_duration),
    - Reported script time (reported_duration),
    - Peak memory (top_memory).

    Returns (script_duration, reported_duration, top_memory).
    If the command fails (non-zero exit), returns (-1, -1, top_memory).
    """
    if verbose:
        print(TerminalColors.OKCYAN + f"[*] Executing: {command_str}" + TerminalColors.ENDC)

    start = time.time()
    top_memory = 0
    reported_duration = -1

    with subprocess.Popen(
        command_str.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    ) as proc:
        try:
            process = psutil.Process(proc.pid)
            while proc.poll() is None:
                memory = process.memory_info()
                top_memory = max(top_memory, memory.rss)
        except subprocess.TimeoutExpired:
            proc.kill()
            return -1, -1, top_memory

        if proc.returncode != 0:
            if verbose:
                print(TerminalColors.WARNING + f"Command failed with code {proc.returncode}" + TerminalColors.ENDC)
            return -1, -1, top_memory

        stdout = proc.communicate()[0]
        decoded = stdout.decode('utf-8')
        lines = decoded.split('\n')
        for line in lines:
            if 'Execution time' in line:
                # e.g. "Execution time: 123ms"
                time_str = line.split(' ')[-1].replace('ms', '')
                reported_duration = float(time_str) / 1000.0
                break

        if verbose and decoded.strip():
            print(TerminalColors.OKBLUE + f"[*] Command output:\n{decoded}" + TerminalColors.ENDC)

    script_duration = time.time() - start
    return script_duration, reported_duration, top_memory


def collect_statistics(values):
    values.sort()
    if not values:
        return {
            'results': [],
            'median': 0,
            'stdev': 0,
            'p99': 0,
            'p95': 0,
            'p50': 0,
            'p5': 0,
        }

    med = statistics.median(values)
    stdev_ = statistics.stdev(values) if len(values) > 1 else 0.0
    p99_ = numpy.percentile(values, 99)
    p95_ = numpy.percentile(values, 95)
    p50_ = numpy.percentile(values, 50)
    p5_ = numpy.percentile(values, 5)

    return {
        'results': values,
        'median': med,
        'stdev': stdev_,
        'p99': p99_,
        'p95': p95_,
        'p50': p50_,
        'p5': p5_,
    }


def write_results_json(flat_results):
    import os
    os.makedirs('.results', exist_ok=True)
    with open('.results/results.json', 'w') as file:
        json.dump(flat_results, file, indent=2)

def write_results_markdown(flat_results):
    """
    Produces RESULTS.md grouped by script.
    Each script gets its own heading, followed by a table that includes
    columns for 'Language' (a.k.a. 'config'), 'Command', 'Version', 
    and the usual median, stdev, p95, memory, etc.
    """
    # Group results by 'script'
    grouped_by_script = defaultdict(list)
    for entry in flat_results:
        grouped_by_script[entry['script']].append(entry)

    with open('RESULTS.md', 'w') as file:
        file.write('# Results\n\n')

        # For each script, produce a separate section
        for script_name in sorted(grouped_by_script.keys()):
            file.write(f'## {script_name}\n\n')

            # Table header
            file.write(
                '| Language | Command | Version | Time (median ± stdev), s | '
                'p99, s | p95, s | p50, s | p5, s | '
                'Startup (median ± stdev), s | Total (median ± stdev), s | '
                'Memory (median ± stdev), MiB |\n'
            )
            file.write(
                '| :------- | :------ | :------ | ------------------------: | '
                '-------: | ------: | ------: | ------: | '
                '--------------------------: | --------------------------: | '
                '--------------------------: |\n'
            )

            # Print one row per result in this script
            for entry in grouped_by_script[script_name]:
                language = entry.get('config', '')    # or 'config_title'
                command = entry.get('command', '')
                version = entry.get('version', '')    # might be empty string
                time_stats = entry['time']
                startup_stats = entry['startup_time']
                total_stats = entry['total_time']
                mem_stats = entry['memory']

                file.write(
                    '| {lang} | {cmd} | {ver} | {time_med:.3f}±{time_std:.3f} | '
                    '{time_p99:.3f} | {time_p95:.3f} | {time_p50:.3f} | {time_p5:.3f} | '
                    '{startup_med:.3f}±{startup_std:.3f} | '
                    '{total_med:.3f}±{total_std:.3f} | '
                    '{mem_med:.2f}±{mem_std:.2f} |\n'.format(
                        lang=language,
                        cmd=command,
                        ver=version,

                        time_med=time_stats['median'],
                        time_std=time_stats['stdev'],
                        time_p99=time_stats['p99'],
                        time_p95=time_stats['p95'],
                        time_p50=time_stats['p50'],
                        time_p5=time_stats['p5'],

                        startup_med=startup_stats['median'],
                        startup_std=startup_stats['stdev'],

                        total_med=total_stats['median'],
                        total_std=total_stats['stdev'],

                        mem_med=(mem_stats['median'] / 1024 / 1024),
                        mem_std=(mem_stats['stdev'] / 1024 / 1024),
                    )
                )

            file.write('\n\n')

        # Legend
        file.write('## Legend\n\n')
        file.write('| Field         | Description |\n')
        file.write('| :------------ | :---------- |\n')
        file.write('| Time          | Time spent in the algorithm itself, reported by the program. |\n')
        file.write('| Total time    | End-to-end time from program start to finish, measured by the benchmark. |\n')
        file.write('| Startup time  | (Total time - Time) => overhead before the algorithm. |\n')
        file.write('| Memory        | Peak RSS memory usage measured by psutil. |\n')


def run_action(args):
    configuration_files = load_configurations(args.languages)
    prepare_configurations(configuration_files)

    times = args.times
    scripts_filter = args.scripts if args.scripts else ['*']

    final_results = []

    for cfg_file in configuration_files:
        directory = os.path.dirname(cfg_file)
        runs = load_configuration(cfg_file, directory)

        for run_def in runs:
            script_file = run_def['script_file']
            script_title = run_def['script_title']
            config_title = run_def['config_title']
            command_title = run_def['command_title']
            command_str = run_def['command_str']
            version = run_def['version']

            # Skip if user specifically said skip:script_name
            if f"skip:{script_title}" in scripts_filter:
                continue

            # If user specified scripts, skip if not in them
            if (script_title not in scripts_filter) and ('*' not in scripts_filter):
                continue

            # Possibly fix the command if first token is not a file but found via 'which'
            split_cmd = command_str.split()
            executable = split_cmd[0]
            if not os.path.isfile(executable):
                found_executable, _ = subprocess.Popen(['which', executable], stdout=subprocess.PIPE).communicate()
                if found_executable:
                    split_cmd[0] = found_executable.decode("utf-8").strip()
                    command_str = ' '.join(split_cmd)

            if version:
                print(
                    f"Running {config_title} - {script_title} - {command_title} (v{version or ''}):",
                    end='\n\t', flush=True
                )
            else:
                print(
                    f"Running {config_title} - {script_title} - {command_title}:",
                    end='\n\t', flush=True
                )

            time_results = []
            reported_results = []
            memory_results = []

            # If {file} is supposed to be replaced, do it here if needed
            # (Though in your example, we used {version} in the command, not {file}.)
            # If your commands rely on {file}, you'd do final_command_str = command_str.format(file=script_file)
            # We'll assume you handle that in the YAML or your code.

            for _ in range(times):
                # Verbose so we see the final command
                elapsed, reported, mem = run_benchmark(command_str, verbose=args.verbose)
                print(f"{reported:.3f}", end='\t', flush=True)

                if elapsed > 0:
                    time_results.append(elapsed)
                    reported_results.append(reported)
                    memory_results.append(mem)

            print()

            if time_results and memory_results:
                startup_results = [t - r for (t, r) in zip(time_results, reported_results)]
                aggregated = {
                    'script': script_title,
                    'config': config_title,
                    'command': command_title,
                    'version': version or '',
                    'executed_command': command_str,
                    'total_time': collect_statistics(time_results),
                    'time': collect_statistics(reported_results),
                    'startup_time': collect_statistics(startup_results),
                    'memory': collect_statistics(memory_results),
                }

                print(
                    TerminalColors.OKGREEN +
                    '\tFinal: {:.3f} ± {:.3f}; p95% = {:.3f}; p50% = {:.3f}; p5% = {:.3f}'
                    .format(
                        aggregated['time']['median'],
                        aggregated['time']['stdev'],
                        aggregated['time']['p95'],
                        aggregated['time']['p50'],
                        aggregated['time']['p5']
                    ) +
                    TerminalColors.ENDC,
                    flush=True
                )

                final_results.append(aggregated)
            else:
                print(
                    TerminalColors.WARNING +
                    f'\tSkipping {script_title}-{command_title}-v{version} (no valid results)...' +
                    TerminalColors.ENDC
                )

    write_results_json(final_results)
    write_results_markdown(final_results)


def results_action(args):
    with open('.results/results.json', 'r') as file:
        flat_results = json.load(file)
    write_results_markdown(flat_results)


def main():
    args = parse_arguments()

    if args.action == 'run':
        run_action(args)
    elif args.action == 'results':
        results_action(args)
    else:
        print("Invalid action provided.")


if __name__ == "__main__":
    main()
