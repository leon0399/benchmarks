#!/usr/bin/env php
<?php

const NUMBER = 500000;

function getLastPrime($count) {
    $lastPrime = 2;

    // Traverse each number from 3 to N, skipping even numbers
    for ($i = 3; $i <= $count; $i += 2) {
        $isPrime = true;
        $limit = floor(sqrt($i));

        for ($j = 3; $j <= $limit; $j += 2) {
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
