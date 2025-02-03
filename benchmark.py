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
from abc import ABC, abstractmethod

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


class OutputFormat(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def write(self, results):
        pass

class LiveOutputFormat(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def write_single_result(self, result):
        pass

class JsonOutputFormat(OutputFormat):
    def __init__(self, path):
        self.path = path

    def prepare(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def write(self, results):
        formatted_results = {}
        for result in results:
            if result['script'] not in formatted_results:
                formatted_results[result['script']] = {}

            if result['language'] not in formatted_results[result['script']]:
                formatted_results[result['script']][result['language']] = {}

            configurationName = result['configuration']
            if result['version'] != None and 'Old' in result['tags']:
                configurationName = f'{result["configuration"]} ({result["version"]})'
            
            formatted_results[result['script']][result['language']][configurationName] = {
                'total_time': {
                    'results': result['total_time']['results'],
                    'median': result['total_time']['p50'],
                    'stdev': result['total_time']['std_pop'],
                    'mean': result['total_time']['mean'],
                    'std_sample': result['total_time']['std_sample'],
                    'n99': result['total_time']['p99'],
                    'n95': result['total_time']['p95'],
                    'n50': result['total_time']['p50'],
                    'n05': result['total_time']['p5'],
                },
                'time': {
                    'results': result['time']['results'],
                    'median': result['time']['p50'],
                    'stdev': result['time']['std_pop'],
                    'mean': result['time']['mean'],
                    'std_sample': result['time']['std_sample'],
                    'n99': result['time']['p99'],
                    'n95': result['time']['p95'],
                    'n50': result['time']['p50'],
                    'n05': result['time']['p5'],
                },
                'startup_time': {
                    'results': result['startup_time']['results'],
                    'median': result['startup_time']['p50'],
                    'stdev': result['startup_time']['std_pop'],
                    'mean': result['startup_time']['mean'],
                    'std_sample': result['startup_time']['std_sample'],
                    'n99': result['startup_time']['p99'],
                    'n95': result['startup_time']['p95'],
                    'n50': result['startup_time']['p50'],
                    'n05': result['startup_time']['p5'],
                },
                'memory': {
                    'results': result['memory']['results'],
                    'median': result['memory']['p50'],
                    'stdev': result['memory']['std_pop'],
                    'mean': result['memory']['mean'],
                    'std_sample': result['memory']['std_sample'],
                    'n99': result['memory']['p99'],
                    'n95': result['memory']['p95'],
                    'n50': result['memory']['p50'],
                    'n05': result['memory']['p5'],
                }
            }

        with open(self.path, 'w') as file:
            json.dump(formatted_results, file, indent=4)

class JsonLinesOutputFormat(LiveOutputFormat):
    def __init__(self, path):
        self.path = path

    def prepare(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        # Clear the file
        open(self.path, 'w').close()

    def write_single_result(self, result):
        with open(self.path, 'a') as file:
            file.write(json.dumps(result) + '\n')

class MarkdownOutputFormat(OutputFormat):
    def __init__(self, path):
        self.path = path

    def prepare(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def write(self, results):
        grouped_by_script = defaultdict(list)
        for entry in results:
            grouped_by_script[entry['script']].append(entry)

        with open(self.path, 'w') as file:
            file.write('# Results\n\n')
            file.write('## Algorithms\n\n')

            for script_name in sorted(grouped_by_script.keys()):
                file.write(f'### {script_name}\n\n')

                file.write('| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |\n')
                file.write('| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |\n')

                for entry in grouped_by_script[script_name]:
                    languageName = entry['language'] if entry['version'] == None else f'{entry["language"]} ({entry["version"]})'
                    languageName = languageName if entry['language'] == entry['configuration'] else f'{languageName} ({entry["configuration"]})'
                    file.write(
                        f'| {languageName} | {entry["time"]["mean"]:.3f} | {entry["time"]["p99"]:.3f} | {entry["time"]["p95"]:.3f} | {entry["time"]["p50"]:.3f} | {entry["time"]["p5"]:.3f} | {entry["startup_time"]["mean"]:.3f} | {entry["total_time"]["mean"]:.3f} | {entry["memory"]["mean"] / 1024 / 1024:.2f} |\n'
                    )
                
                file.write('\n')

            file.write('## Legend\n\n')
            file.write('| Field        | Description |\n')
            file.write('| :----------- | :---------- |\n')
            file.write('| Time         | Time spent in the algorithm itself, reported by the program itself. |\n')
            file.write('| Total time   | Total time spent from the start of the program to the end of the algorithm, measured by the benchmark. |\n')
            file.write('| Startup time | Time spent from the start of the program to the start of the algorithm, measured by the benchmark (Total time - Time). |\n')
            file.write('| Memory       | Peak memory usage during the algorithm, measured by the benchmark. |\n')

def format_full_configuration_name(configuration):
    return f"{configuration['script']} - {configuration['language']} - {configuration['configuration']}"

def parse_output(value):
    """
    Parse an output option provided in the format FORMAT=PATH.
    For example: jsonl=./results/results.json
    Returns an OutputFormat object.
    """

    try:
        fmt, path = value.split('=', 1)

        if fmt == 'json':
            return JsonOutputFormat(path)
        elif fmt == 'jsonl':
            return JsonLinesOutputFormat(path)
        elif fmt == 'markdown':
            return MarkdownOutputFormat(path)
    except ValueError:
        raise argparse.ArgumentTypeError("Output option must be in the format FORMAT=PATH")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run benchmarks')
    subparsers = parser.add_subparsers(dest='action', required=True, help='Action to perform')

    run_parser = subparsers.add_parser('run', help='Run benchmarks')
    run_parser.add_argument(
        '-N', '--times',
        type=int,
        default=5,
        help='Number of times to run each benchmark'
    )
    run_parser.add_argument(
        '-l', '--languages',
        type=str,
        nargs='+',
        help='Languages to run (subdirectories under langs/)',
    )
    run_parser.add_argument(
        '--scripts',
        type=str,
        nargs='+',
        help='Scripts to run (otherwise all scripts in config will run)'
    )
    run_parser.add_argument(
        '--output', type=parse_output, action='append', default=[],
        help='Specify output format and file path as FORMAT=PATH. '
             'Example: --output markdown=./results/RESULTS.json'
    )
    run_parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Print additional debug information, including final commands'
    )
    
    transform_parser = subparsers.add_parser('transform-results', help='Generate results markdown')
    transform_parser.add_argument(
        '--input', type=str, required=True,
        help='Input results file'
    )
    transform_parser.add_argument(
        '--output', type=parse_output, action='append', default=[],
        help='Specify output format and file path as FORMAT=PATH. '
             'Example: --output markdown=./results/RESULTS.json'
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

def run_benchmark(command):
    start = time.time()
    top_memory = 0
    reported_duration = -1

    with subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as proc:
        try:
            process = psutil.Process(proc.pid)
            while proc.poll() is None:
                memory = process.memory_info()
                if memory.rss > top_memory:
                    top_memory = memory.rss
        except subprocess.TimeoutExpired:
            proc.kill()
            return (-1, -1, top_memory)

        if (proc.returncode != 0):
            return (-1, -1, top_memory)

        stdout = proc.communicate()[0]
        decoded = stdout.decode('utf-8')
        lines = decoded.split('\n')

        # Find the `Execution time: %dms` line
        for line in lines:
            if 'Execution time' in line:
                time_str = line.split(' ')[-1]
                time_str = time_str.replace('ms', '')
                reported_duration = float(time_str) / 1000
                break
            
    script_duration = time.time() - start

    return (script_duration, reported_duration, top_memory)

def run_script(filename, command = './%s'):
    return run_benchmark(command % (filename))

def get_script_info(script_info):
    if isinstance(script_info, str):
        script_info = {
            'file': script_info,
            'title': os.path.splitext(script_info)[0]
        }

    if 'title' not in script_info:
        script_info['title'] = script_info['title']

    return script_info

def get_command_info(command_info):
    if isinstance(command_info, str):
        command_info = {
            'title': command_info,
            'command': command_info,
            'tags': [],
        }

    return command_info

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

                if isinstance(version, str):
                    version = {
                        'version': version
                    }

                # If version is set and the template has {version}, replace it
                if version and '{version}' in final_command:
                    final_command = final_command.replace('{version}', str(version['version']))

                # If {file} is present, replace it with the actual file path
                if '{file}' in final_command:
                    final_command = final_command.replace('{file}', full_script_path)

                run_def = {
                    'config_title': config_title,
                    'script_file': script,  # or full_script_path if you prefer
                    'script_title': script_title, 
                    'command_title': command_title,
                    'command_str': final_command,
                    'version': str(version['version']) if version else None,
                    'tags': [],
                }

                # If there are tags in the command, you might store them here
                if 'tags' in cmd_info:
                    run_def['tags'] += cmd_info['tags']

                if version and 'tags' in version:
                    run_def['tags'] += version['tags']

                runs.append(run_def)

    return runs

def collect_statistics(values):
    values.sort()
    if not values:
        return {
            'results': [],
            'mean': 0,
            'stdev': 0,
            'p99': 0,
            'p95': 0,
            'p50': 0,
            'p5': 0,
        }

    mean = numpy.mean(values)
    pop_std = numpy.std(values) if len(values) > 1 else 0.0
    sample_std = numpy.std(values, ddof=1) if len(values) > 1 else 0.0
    p99 = numpy.percentile(values, 99)
    p95 = numpy.percentile(values, 95)
    p50 = numpy.percentile(values, 50)
    p5 = numpy.percentile(values, 5)

    return {
        'results': values,
        'mean': mean,
        'std_pop': pop_std,
        'std_sample': sample_std,
        'p99': p99,
        'p95': p95,
        'p50': p50,
        'p5': p5,
    }

def prepare_benchmarks(configurations):
    for configuration_filename in configurations:
        dir = os.path.dirname(configuration_filename)

        if (os.path.isfile(dir + '/Makefile')):
            print('Making %s' % (dir))
            subprocess.run(['make', 'clean'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)
            made = subprocess.run(['make', 'all'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)

            if made.returncode != 0:
                # throw error
                print('Error in makefile for %s' % (dir))
                exit(1)

def action_run(args):
    for output in args.output:
        output.prepare()

    configurations = load_configurations(args.languages)
    prepare_benchmarks(configurations)

    scripts_filter = args.scripts if args.scripts else '*'

    results = []

    for cfg_file in configurations:
        dir = os.path.dirname(cfg_file)
        runs = load_configuration(cfg_file, dir)

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
                    f"Running {config_title} ({version or ''}) - {script_title} - {command_title}:",
                    end='\n\t', flush=True
                )
            else:
                print(
                    f"Running {config_title} - {script_title} - {command_title}:",
                    end='\n\t', flush=True
                )

            time_results = []
            reported_results = []
            startup_results = []
            memory_results = []

            for _ in range(args.times):
                elapsed, reported, memory = run_benchmark(command_str)
                print("{:.3f}".format(reported), end='\t', flush=True)

                if (elapsed > 0):
                    time_results.append(elapsed)
                    reported_results.append(reported)
                    memory_results.append(memory)

                    startup_results = [t - r for (t, r) in zip(time_results, reported_results)]

            print()

            if time_results and memory_results:
                result = {
                    'script': script_title,
                    'language': config_title,
                    'version': version,
                    'configuration': command_title,
                    'tags': run_def.get('tags', []),
                    'total_time': collect_statistics(time_results),
                    'time': collect_statistics(reported_results),
                    'startup_time': collect_statistics(startup_results),
                    'memory': collect_statistics(memory_results),
                }

                print('\tFinal: {:.3f} ± {:.3f}'.format(result['time']['mean'], result['time']['std_sample']), flush=True)

                for output in args.output:
                    if isinstance(output, LiveOutputFormat):
                        output.write_single_result(result)

                results.append(result)

            else:
                print('\tSkipping...')

    for output in args.output:
        if isinstance(output, OutputFormat):
            output.write(results)

def action_transform_results(args):
    with open(args.input) as file:
        results = json.load(file)

    for output in args.output:
        output.prepare()

        if isinstance(output, OutputFormat):
            output.write(results)

def main():
    args = parse_arguments()

    if args.action == 'run':
        action_run(args)
    elif args.action == 'transform-results':
        action_transform_results(args)
    else:
        print(f"Unknown action: {args.action}")

if __name__ == '__main__':
    main()