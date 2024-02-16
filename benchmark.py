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

parser = argparse.ArgumentParser(description='Run benchmarks')
parser.add_argument('--times', type=int, default=5, help='Number of times to run each benchmark')
parser.add_argument('--languages', type=str, nargs='+', help='Languages to run')
parser.add_argument('--scripts', type=str, nargs='+', help='Scripts to run')
args = parser.parse_args()

times = args.times

# Load the configuration
configurations = []
if args.languages:
    for language in args.languages:
        configurations += glob.glob(language + '/benchmark.yml') + glob.glob(language + '/benchmark.yaml')
else:
    configurations = glob.glob('*/benchmark.yml') + glob.glob('*/benchmark.yaml')
configurations.sort()

scripts = ['*']
if args.scripts:
    scripts = args.scripts

results = {}
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

for configurationFilename in configurations:
    dir = os.path.dirname(configurationFilename)

    if (os.path.isfile(dir + '/Makefile')):
        print('Making %s' % (dir))
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
                run['command']['title'],
                run['script']['title'],
            ),
            end='\n\t',
            flush=True
        )

        timeResults = []
        reportedResults = []
        memoryResults = []

        for _ in range(times):
            elapsed, reported, memory = runScript(dir + '/' + run['script']['file'], run['command']['command'])
            print("{:.3f}".format(reported), end='\t', flush=True)

            if (elapsed > 0):
                timeResults.append(elapsed)
                reportedResults.append(reported)
                memoryResults.append(memory)

        print()

        if timeResults and memoryResults:
            timeResults.sort()
            timeMedian = statistics.median(timeResults)
            timeStdev = statistics.stdev(timeResults)

            reportedResults.sort()
            reportedMedian = statistics.median(reportedResults)
            reportedStdev = statistics.stdev(reportedResults)

            memoryResults.sort()
            memoryMedian = statistics.median(memoryResults)
            memoryStdev = statistics.stdev(memoryResults)

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

with open('RESULTS.md', 'w') as file:
    for (scriptName, languages) in results.items():
        file.write('### %s\n\n' % (scriptName))

        file.write('| Language | Time, s | Total time, s | Memory, MiB |\n')
        file.write('| :------- | ------: | ------------: | ----------: |\n')

        for (language, configurations) in languages.items():
            for (configuration, elapsed) in configurations.items():
                langugageTitle = ('%s' % (language)) if language == configuration else ('%s (%s)' % (language, configuration))

                file.write('| %s | %s<sub>±%s</sub> | %s<sub>±%s</sub> | %s<sub>±%s</sub> |\n' % (
                        langugageTitle,
                        "{:6.3f}".format(elapsed['time']['median']),
                        "{:.3f}".format(elapsed['time']['stdev']),
                        "{:6.3f}".format(elapsed['total_time']['median']),
                        "{:.3f}".format(elapsed['total_time']['stdev']),
                        "{:10.2f}".format(elapsed['memory']['median'] / 1024 / 1024),
                        "{:.2f}".format(elapsed['memory']['stdev'] / 1024 / 1024),
                    )
                )

        file.write('\n\n')
