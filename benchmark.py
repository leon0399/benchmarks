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

times = 5
if 'TIMES' in os.environ:
    times = int(os.environ['TIMES'])

configurations = glob.glob('*/benchmark.yml')
configurations.sort()

results = {}

def runBenchmark(command):
    start = time.time()
    maxMemory = 0

    with subprocess.Popen(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as proc:
        try:
            process = psutil.Process(proc.pid)
            while proc.poll() is None:
                memory = process.memory_info()
                if memory.rss > maxMemory:
                    maxMemory = memory.rss
        except subprocess.TimeoutExpired:
            proc.kill()
            return (-1, maxMemory)

        if (proc.returncode != 0):
            return (-1, maxMemory)

    return ((time.time() - start), maxMemory)

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
    conf = loadConfiguration(configurationFilename)

    if (os.path.isfile(dir + '/Makefile')):
        # print('Running make for %s' % (scriptFilename))
        subprocess.run(['make', 'all'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)

    for run in conf['runs']:
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
        memoryResults = []

        for _ in range(times):
            elapsed, memory = runScript(dir + '/' + run['script']['file'], run['command']['command'])
            print("{:.5f}".format(elapsed), end='\t', flush=True)

            if (elapsed > 0):
                timeResults.append(elapsed)
                memoryResults.append(memory)

        print()

        if timeResults and memoryResults:
            timeResults.sort()
            timeMedian = statistics.median(timeResults)
            timeDelta = max(map(lambda x : abs(x - timeMedian), timeResults))

            memoryResults.sort()
            memoryMedian = statistics.median(memoryResults)
            memoryDelta = max(map(lambda x : abs(x - memoryMedian), memoryResults))

            result = {
                'tags': run['tags'],
                'time': {
                    'results': timeResults,
                    'median': timeMedian,
                    'delta': timeDelta,
                },
                'memory': {
                    'results': memoryResults,
                    'median': memoryMedian,
                    'delta': memoryDelta,
                },
            }

            print('\tFinal: %f ± %f' % (timeMedian, timeDelta))

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

        file.write('| Language | Time, s | Memory, MiB |\n')
        file.write('| :------- | ------: | ----------: |\n')

        for (language, configurations) in languages.items():
            for (configuration, elapsed) in configurations.items():
                langugageTitle = ('%s' % (language)) if language == configuration else ('%s (%s)' % (language, configuration))

                file.write('| %s | %s<sub>±%s</sub> | %s<sub>±%s</sub> |\n' % (
                        langugageTitle,
                        "{:6.3f}".format(elapsed['time']['median']),
                        "{:.3f}".format(elapsed['time']['delta']),
                        "{:10.2f}".format(elapsed['memory']['median'] / 1024 / 1024),
                        "{:.2f}".format(elapsed['memory']['delta'] / 1024 / 1024),
                    )
                )

        file.write('\n\n')
