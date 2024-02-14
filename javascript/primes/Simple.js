#!/usr/bin/env node

'use strict';

const NUMBER = 100000;

function printPrimes(number)
{
    // Traverse each number from 1 to N with the help of for loop
    for (var i = 0; i <= number; i++)
    {
        // Skip 0 and 1 as they are neither prime nor composite
        if (i == 1 || i == 0)
        {
            continue;
        }

        var isPrime = true;

        for (var j = 2; j <= i / 2; ++j) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            console.log(i);
        }
    }
}

(async function() {
    const startTimeMs = new Date().getTime();
      
    printPrimes(NUMBER);

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();
