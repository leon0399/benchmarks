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
hasMem = os.path.isfile('proc/self/statm')

results = {}

def deep_set(d, key, value):
    dd = d
    keys = key.split('.')
    latest = keys.pop()
    for k in keys:
        dd = dd.setdefault(k, {})
    dd[latest] = value

def runBenchmark(command):
    start = time.time()

    with subprocess.Popen(['/bin/sh', '-c', command, '> /dev/null 2>&1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as proc:
        proc.wait()

    diff = (time.time() - start)

    return (diff)

def runConfiguration(filename, command = './%s'):
    return runBenchmark(command % (filename))

def loadConfiguration(filename):
    file = open(filename);
    conf = yaml.safe_load(file)
    file.close()

    return conf

for _ in range(times):
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

                if (scriptName not in results):
                    results[scriptName] = {}

                if (title not in results[scriptName]):
                    results[scriptName][title] = {}

                if (commandTitle not in results[scriptName][title]):
                    results[scriptName][title][commandTitle] = {'values': []}


                print('Running:\t%s - %s - %s (%s)' % (title, commandTitle, scriptName, _))

                result = runConfiguration(dir + '/' + scriptFilename, command)

                results[scriptName][title][commandTitle]['values'].append(result)
                results[scriptName][title][commandTitle]['median'] = median = statistics.median(results[scriptName][title][commandTitle]['values'])
                results[scriptName][title][commandTitle]['delta'] = delta = max(map(
                    lambda secs : abs(secs - median),
                    results[scriptName][title][commandTitle]['values']
                ))

                print('Result:\t(median: %s \t delta: %s)' % (median, delta))

    # print(results)