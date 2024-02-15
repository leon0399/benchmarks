#!/usr/bin/env php

<?php

const NUMBER = 100000;

function printPrimes($count) {
    // Traverse each number from 1 to N with the help of for loop
    for ($i = 1; $i <= $count; $i++)
    {
        // Skip 0 and 1 as they are neither prime nor composite
        if ($i == 1 || $i == 0) {
            continue;
        }

        $isPrime = true;

        for ($j = 2; $j <= $i / 2; ++$j) {
            if ($i % $j == 0) {
                $isPrime = false;
                break;
            }
        }

        if ($isPrime) {
            echo $i . "\n";
        }
    }
}

(function () {
    $startTimeMs = floor(microtime(true) * 1000);

    printPrimes(NUMBER);

    $endTimeMs = floor(microtime(true) * 1000);
    $durationMs = $endTimeMs - $startTimeMs;
  
    echo "Execution time: " . $durationMs . "ms\n";
})();
