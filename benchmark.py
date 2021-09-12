#!/usr/bin/python3

import subprocess
import resource
import psutil

import os.path
import glob
import yaml

import time
import statistics

times = 10

configurations = glob.glob('*/benchmark.yml')

results = {}

def runBenchmark(command):
    start = time.time()

    with subprocess.Popen(['/bin/sh', '-c', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as proc:
        proc.wait()

    diff = (time.time() - start)

    return diff

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

    for commandInfo in matrix['command']:
        commandTitle = command = commandInfo

        if (isinstance(commandInfo, dict)):
            commandTitle = commandInfo['title']
            command = commandInfo['command']

        for fileInfo in matrix['files']:
            scriptFilename = fileInfo
            scriptName = os.path.splitext(scriptFilename)[0]

            if (os.path.isfile(dir + '/Makefile')):
                # print('Running make for %s' % (scriptFilename))
                subprocess.run(['/bin/sh', '-c', 'make', scriptFilename], cwd=dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            scriptResults = []

            print('Running: %s - %s - %s:' % (scriptName, title, commandTitle), end='\t', flush=True)

            for _ in range(times):
                result = runScript(dir + '/' + scriptFilename, command)
                print('%f' % (result), end=' ', flush=True)
                scriptResults.append(result)

            print()

            median = statistics.median(scriptResults)
            delta = max(map(lambda x : abs(x - median), scriptResults))

            result = {
                'time': {
                    'results': scriptResults,
                    'median': median,
                    'delta': delta,
                }
            }

            print('\tFinal: %f ± %f' % (median, delta))

            if (scriptName not in results):
                results[scriptName] = {}
            if (title not in results[scriptName]):
                results[scriptName][title] = {}

            results[scriptName][title][commandTitle] = result

with open('RESULTS.md', 'w') as file:
    for (scriptName, languages) in results.items():
        file.write('### %s\n\n' % (scriptName))

        file.write('| Language | Time, s |\n')
        file.write('| :------- | ------: |\n')

        for (language, configurations) in languages.items():
            for (configuration, result) in configurations.items():
                file.write('| %s (%s) | %s<sub>±%s</sub> |\n' % (language, configuration, round(result['time']['median'], 3), round(result['time']['delta'], 3)))

        file.write('\n\n')
