#!/usr/bin/python3

import subprocess
import psutil

import os.path
import glob
import yaml
import json

import time
import statistics

times = 10

configurations = glob.glob('*/benchmark.yml')
configurations.sort()

results = {}

def runBenchmark(command):
    start = time.time()
    maxMemory = 0

    with subprocess.Popen(command.split(), stdout=subprocess.DEVNULL) as proc:
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

def loadConfiguration(filename):
    file = open(filename);
    conf = yaml.safe_load(file)
    file.close()

    return conf

for configurationFilename in configurations:
    dir = os.path.dirname(configurationFilename)
    conf = loadConfiguration(configurationFilename)

    title = conf['title']
    matrix = conf['strategy']['matrix']

    if (os.path.isfile(dir + '/Makefile')):
        # print('Running make for %s' % (scriptFilename))
        subprocess.run(['make', 'all'], cwd=dir, shell=True, stdout=subprocess.DEVNULL)

    for fileInfo in matrix['files']:
        scriptFilename = fileInfo
        scriptName = os.path.splitext(scriptFilename)[0]

        for commandInfo in matrix['command']:
            commandTitle = command = commandInfo

            if (isinstance(commandInfo, dict)):
                commandTitle = commandInfo['title']
                command = commandInfo['command']

            split = command.split()
            executable = split[0]

            if not os.path.isfile(executable):
                executable, err = subprocess.Popen(['which', executable], stdout=subprocess.PIPE).communicate()

                if executable:
                    split[0] = executable.decode("utf-8").replace('\n', '')
                    command = ' '.join(split)

            print('Running: %s - %s - %s:' % (scriptName, title, commandTitle), end='\t', flush=True)

            timeResults = []
            memoryResults = []

            for _ in range(times):
                elapsed, memory = runScript(dir + '/' + scriptFilename, command)
                print('%f' % elapsed, end=' ', flush=True)

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

                if (scriptName not in results):
                    results[scriptName] = {}
                if (title not in results[scriptName]):
                    results[scriptName][title] = {}

                results[scriptName][title][commandTitle] = result

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
