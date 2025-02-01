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

def runBenchmark(command):
    start = time.time()
    topMemory = 0
    reportedDuration = -1

    with subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as proc:
        try:
            process = psutil.Process(proc.pid)
            while proc.poll() is None:
                memory = process.memory_info()
                if memory.rss > topMemory:
                    topMemory = memory.rss
        except subprocess.TimeoutExpired:
            proc.kill()
            return (-1, -1, topMemory)

        if (proc.returncode != 0):
            return (-1, -1, topMemory)

        stdout = proc.communicate()[0]
        decoded = stdout.decode('utf-8')
        lines = decoded.split('\n')

        # Find the `Execution time: %dms` line
        for line in lines:
            if 'Execution time' in line:
                timeStr = line.split(' ')[-1]
                timeStr = timeStr.replace('ms', '')
                reportedDuration = float(timeStr) / 1000
                break
            
    scriptDuration = time.time() - start


    return (scriptDuration, reportedDuration, topMemory)

def runScript(filename, command = './%s'):
    return runBenchmark(command % (filename))

def getScriptInfo(scriptInfo):
    if isinstance(scriptInfo, str):
        scriptInfo = {
            'file': scriptInfo,
            'title': os.path.splitext(scriptInfo)[0]
        }

    if 'title' not in scriptInfo:
        scriptInfo['title'] = scriptInfo['title']

    return scriptInfo

def getCommandInfo(commandInfo):
    if isinstance(commandInfo, str):
        commandInfo = {
            'title': commandInfo,
            'command': commandInfo,
            'tags': [],
        }

    return commandInfo


def loadConfiguration(filename):
    conf = {}

    with open(filename) as file:
        conf = yaml.safe_load(file)
        file.close()

    configuration = {}
    configuration['title'] = conf['title']
    configuration['runs'] = []

    matrix = conf['strategy']['matrix']

    for scriptInfo in matrix['files']:
        scriptInfo = getScriptInfo(scriptInfo)

        for commandInfo in matrix['command']:
            tags = []
            commandInfo = getCommandInfo(commandInfo)

            if 'tags' in scriptInfo:
                tags += scriptInfo['tags']

            if 'tags' in commandInfo:
                tags += commandInfo['tags']

            configuration['runs'].append({
                'script': scriptInfo,
                'command': commandInfo,
                'tags': tags,
            })

    if 'exclude' in matrix:
        for exclude in matrix['exclude']:
            configuration['runs'] = list(filter(
                lambda run : not (run['command']['title'] == exclude['command'] and run['script']['title'] == exclude['file']),
                configuration['runs']
            ))

    return configuration

def writeResultsMarkdown(results):
    with open('RESULTS.md', 'w') as file:
        file.write('# Results\n\n')

        file.write('## Algorithms\n\n')

        for (scriptName, languages) in results.items():
            file.write('### %s\n\n' % (scriptName))

            file.write('| Language | Time, s | %99 Time, s | %95 Time, s | %50 Time, s | %5 Time, s | Startup time, s | Total time, s | Memory, MiB |\n')
            file.write('| :------- | ------: | ----------: |  ---------: |  ---------: |  --------: | --------------: | ------------: | ----------: |\n')

            for (language, configurations) in languages.items():
                for (configuration, elapsed) in configurations.items():
                    langugageTitle = ('%s' % (language)) if language == configuration else ('%s (%s)' % (language, configuration))

                    file.write('| %s | %s<sub>±%s</sub> | %s | %s | %s | %s | %s<sub>±%s</sub> | %s<sub>±%s</sub> | %s<sub>±%s</sub> |\n' % (
                            langugageTitle,
                            "{:6.3f}".format(elapsed['time']['median']),
                            "{:.3f}".format(elapsed['time']['stdev']),

                            "{:6.3f}".format(elapsed['time']['n99']),
                            "{:6.3f}".format(elapsed['time']['n95']),
                            "{:6.3f}".format(elapsed['time']['n50']),
                            "{:6.3f}".format(elapsed['time']['n05']),

                            "{:6.3f}".format(elapsed['startup_time']['median']),
                            "{:.3f}".format(elapsed['startup_time']['stdev']),

                            "{:6.3f}".format(elapsed['total_time']['median']),
                            "{:.3f}".format(elapsed['total_time']['stdev']),

                            "{:10.2f}".format(elapsed['memory']['median'] / 1024 / 1024),
                            "{:.2f}".format(elapsed['memory']['stdev'] / 1024 / 1024),
                        )
                    )

            file.write('\n\n')

        file.write('## Legend\n\n')

        file.write('| Field        | Description |\n')
        file.write('| :----------- | :---------- |\n')
        file.write('| Time         | Time spent in the algorithm itself, reported by the program itself. |\n')
        file.write('| Total time   | Total time spent from the start of the program to the end of the algorithm, measured by the benchmark. |\n')
        file.write('| Startup time | Time spent from the start of the program to the start of the algorithm, measured by the benchmark (Total time - Time). |\n')
        file.write('| Memory       | Peak memory usage during the algorithm, measured by the benchmark. |\n')

        file.write('\n\n')

def actionRun(args):
    results = {}

    configurations = load_configurations(args.languages)
    scripts = args.scripts if args.scripts else '*'

    for configurationFilename in configurations:
        dir = os.path.dirname(configurationFilename)

        if (os.path.isfile(dir + '/Makefile')):
            print('Making %s' % (dir))
            subprocess.run(['make', 'clean'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)
            made = subprocess.run(['make', 'all'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)

            if made.returncode != 0:
                # throw error
                print('Error in makefile for %s' % (dir))
                exit(1)

    for configurationFilename in configurations:
        dir = os.path.dirname(configurationFilename)
        conf = loadConfiguration(configurationFilename)

        for run in conf['runs']:
            if run['script']['title'] not in scripts and '*' not in scripts:
                continue

            split = run['command']['command'].split()
            executable = split[0]

            if not os.path.isfile(executable):
                executable, err = subprocess.Popen(['which', executable], stdout=subprocess.PIPE).communicate()

                if executable:
                    split[0] = executable.decode("utf-8").replace('\n', '')
                    run['command']['command'] = ' '.join(split)

            print(
                'Running: %s - %s - %s:' % (
                    conf['title'],
                    run['script']['title'],
                    run['command']['title'],
                ),
                end='\n\t',
                flush=True
            )

            timeResults = []
            reportedResults = []
            startupResults = []
            memoryResults = []

            for _ in range(args.times):
                elapsed, reported, memory = runScript(dir + '/' + run['script']['file'], run['command']['command'])
                print("{:.3f}".format(reported), end='\t', flush=True)

                if (elapsed > 0):
                    timeResults.append(elapsed)
                    reportedResults.append(reported)
                    memoryResults.append(memory)

                    # substract reported time from total time for each entry to get startup time results
                    for i in range(len(timeResults)):
                        startupResults.append(timeResults[i] - reportedResults[i])

            print()

            if timeResults and memoryResults:
                timeResults.sort()
                timeMedian = statistics.median(timeResults)
                timeStdev = 0
                if len(timeResults) > 1:
                    timeStdev = statistics.stdev(timeResults)

                reportedResults.sort()
                reportedMedian = statistics.median(reportedResults)
                reportedStdev = 0
                if len(reportedResults) > 1:
                    reportedStdev = statistics.stdev(reportedResults)

                reportedN99 = numpy.percentile(reportedResults, 99)
                reportedN95 = numpy.percentile(reportedResults, 95)
                reportedN50 = numpy.percentile(reportedResults, 50)
                reportedN05 = numpy.percentile(reportedResults, 5)

                memoryResults.sort()
                memoryMedian = statistics.median(memoryResults)
                memoryStdev = 0
                if len(memoryResults) > 1:
                    memoryStdev = statistics.stdev(memoryResults)

                startupResults.sort()
                startupMedian = statistics.median(startupResults)
                startupStdev = 0
                if len(startupResults) > 1:
                    startupStdev = statistics.stdev(startupResults)


                result = {
                    'tags': run['tags'],
                    'total_time': {
                        'results': timeResults,
                        'median': timeMedian,
                        'stdev': timeStdev,
                    },
                    'time': {
                        'results': reportedResults,
                        'median': reportedMedian,
                        'stdev': reportedStdev,
                        'n99': reportedN99,
                        'n95': reportedN95,
                        'n50': reportedN50,
                        'n05': reportedN05,
                    },
                    'startup_time': {
                        'results': startupResults,
                        'median': startupMedian,
                        'stdev': startupStdev,
                    },
                    'memory': {
                        'results': memoryResults,
                        'median': memoryMedian,
                        'stdev': memoryStdev,
                    },
                }

                print('\tFinal: {:.3f} ± {:.3f}'.format(reportedMedian, reportedStdev), flush=True)

                if (run['script']['title'] not in results):
                    results[run['script']['title']] = {}
                if (conf['title'] not in results[run['script']['title']]):
                    results[run['script']['title']][conf['title']] = {}

                results[run['script']['title']][conf['title']][run['command']['title']] = result

            else:
                print('\tSkipping...')

    with open('.results/results.json', 'w') as file:
        json.dump(results, file, indent=2)

    with open('.results/results.jsonl', 'w') as file:
        for (scriptName, languages) in results.items():
            for (language, configurations) in languages.items():
                for (configuration, elapsed) in configurations.items():
                    aggregated = {
                        'script': scriptName,
                        'language': language,
                        'configuration': configuration,
                        'tags': elapsed['tags'],
                        'time': {
                            'median': elapsed['time']['median'],
                            'std_pop': elapsed['time']['stdev'],
                            'p99': elapsed['time']['n99'],
                            'p95': elapsed['time']['n95'],
                            'p50': elapsed['time']['n50'],
                            'p5': elapsed['time']['n05'],
                        },
                        'time_startup': {
                            'median': elapsed['startup_time']['median'],
                            'stdev': elapsed['startup_time']['stdev'],
                        },
                        'memory': {
                            'median': elapsed['memory']['median'],
                            'stdev': elapsed['memory']['stdev'],
                        },
                    }

                    file.write(json.dumps(aggregated) + '\n')

    writeResultsMarkdown(results)

def actionResults(args):
    with open('.results/results.json', 'r') as file:
        results = json.load(file)

    writeResultsMarkdown(results)

def main():
    args = parse_arguments()

    if args.action == 'run':
        actionRun(args)
    elif args.action == 'results':
        actionResults(args)

if __name__ == '__main__':
    main()