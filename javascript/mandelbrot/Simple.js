#!/usr/bin/env node

'use strict';

function index()
{
    for (var y = -39; y < 39; y++) {
        process.stdout.write("\n");

        for (var x = -39; x < 39; x++) {
            var i = mandelbrot(
                x / 40.0,
                y / 40.0
            );

            if (i == 0) {
                process.stdout.write("*");
            } else {
                process.stdout.write(" ");
            }
        }
    }

    process.stdout.write("\n");
}

function mandelbrot(x, y)
{
    var cr = y - 0.5;
    var ci = x;
    var zi = 0.0;
    var zr = 0.0;
    var i = 0;

    while (1) {
        i++;

        var temp = zr * zi;

        var zr2 = zr * zr;
        var zi2 = zi * zi;

        zr = zr2 - zi2 + cr;
        zi = temp + temp + ci;

        if (zi2 + zr2 > 16) {
            return i;
        }

        if (i > 5000) {
            return 0;
        }
    }
}

(async function() {
    const startTimeMs = new Date().getTime();
      
    index();

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();
