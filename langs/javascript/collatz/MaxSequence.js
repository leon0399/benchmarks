#!/usr/bin/env node

'use strict';

const NUMBER = 500000;

function collatz(x)
{
    var len = 0;

    while (x > 1) {
        if (x % 2 == 0) {
            x = x / 2;
        } else {
            x = 3 * x + 1;
        }

        len++;
    }

    return len;
}

function findMaxCollatz(to) {
    var result = [1, 1];

    for (var number = 1; number <= to; number++) {
        var len = collatz(number);

        if (len > result[1]) {
            result = [number, len];
        }
    }

    return result;
}

(async function() {
    const startTimeMs = new Date().getTime();
    
    console.log(findMaxCollatz(NUMBER));

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();

