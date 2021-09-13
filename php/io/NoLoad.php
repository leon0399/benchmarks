#!/usr/bin/env php

<?php

const NUMBER = 500000;

function run($times) {
    $x = 0;
    for ($i = 0; $i <= $times; $i++) {
        $x = $i * $i;
    }
    print($x . "\n");
}

(function () {
    run(NUMBER);
})();

