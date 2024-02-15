#!/usr/bin/env php

<?php

const NUMBER = 500000;

function collatz($x) {
    $len = 0;

    while ($x > 1) {
        if ($x % 2 == 0) {
            $x = $x / 2;
        } else {
            $x = 3 * $x + 1;
        }

        $len++;
    }

    return $len;
}

function findMaxCollatz($to) {
    $result = [1, 1];

    for ($number = 1; $number <= $to; $number++) {
        $len = collatz($number);

        if ($len > $result[1]) {
            $result = [$number, $len];
        }
    }

    return $result;
}

(function () {
    $startTimeMs = floor(microtime(true) * 1000);

    print_r(findMaxCollatz(NUMBER));

    $endTimeMs = floor(microtime(true) * 1000);
    $durationMs = $endTimeMs - $startTimeMs;

    echo "Execution time: " . $durationMs . "ms\n";
})();
