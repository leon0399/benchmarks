<?php

const NUMBER = 500;

function printFibonacciSequence($count)
{
    $first = 0;
    $second = 1;

    for($i = 0; $i < $count; $i++)
    {
        if($i < 1)
        {
            $next = $i;
        } else {
            $next = $first + $second;
            $first = $second;
            $second = $next;
        }

        echo $next . ' ';
    }
}

printFibonacciSequence(NUMBER);
