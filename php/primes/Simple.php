#!/usr/bin/env php

<?php

const NUMBER = 100000;

function getLastPrime($count) {
    $lastPrime = 2;

    // Traverse each number from 1 to N with the help of for loop
    for ($i = 2; $i <= $count; $i++)
    {
        $isPrime = true;

        for ($j = 2; $j <= $i / 2; ++$j) {
            if ($i % $j == 0) {
                $isPrime = false;
                break;
            }
        }

        if ($isPrime) {
            $lastPrime = $i;
        }
    }

    return $lastPrime;
}

(function () {
    $startTimeMs = floor(microtime(true) * 1000);

    $lastPrime = getLastPrime(NUMBER);
    echo "Last prime: " . $lastPrime . "\n";

    $endTimeMs = floor(microtime(true) * 1000);
    $durationMs = $endTimeMs - $startTimeMs;
  
    echo "Execution time: " . $durationMs . "ms\n";
})();
