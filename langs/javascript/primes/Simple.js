#!/usr/bin/env node

'use strict';

const NUMBER = 1000000;

function getLastPrime(number)
{
    var lastPrime = 2;

    // Traverse each number from 1 to N with the help of for loop
    for (var i = 3; i <= number; i += 2)
    {
        var isPrime = true;
        var limit = Math.sqrt(i);

        for (var j = 3; j <= limit; j += 2) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            lastPrime = i;
        }
    }

    return lastPrime;
}

(async function() {
    const startTimeMs = new Date().getTime();
      
    const lastPrime = getLastPrime(NUMBER);
    console.log(`Last prime: ${lastPrime}`);

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();
