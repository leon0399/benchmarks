<?php

const UPPER_BOUND = 5000000;
const PREFIX = 32338;

class Node
{
    /** @var array<Node> $children */
    public $children = [];

    /** @var bool $terminal */
    public $terminal = false;

    public function __construct()
    {
        $this->children = [];
        $this->terminal = false;
    }
}

class Sieve
{
    /** @var int $limit */
    public $limit;

    /** @var array<bool> $prime */
    public $prime;

    /**
     * @var int $limit
     */
    public function __construct($limit)
    {
        $this->limit = $limit;
        $this->prime = array_fill(0, $this->limit + 1, false);
    }

    /**
     * @return array
     */
    public function toList()
    {
        $result = [2, 3];

        for ($p = 5; $p <= $this->limit; ++$p)
        {
            if ($this->prime[$p])
            {
                $result[] = $p;
            }
        }

        return $result;
    }

    public function omitSquares()
    {
        for ($r = 5; $r * $r < $this->limit; ++$r)
        {
            if ($this->prime[$r])
            {
                for ($i = $r * $r; $i < $this->limit; $i += $r * $r)
                {
                    $this->prime[$i] = false;
                }
            }
        }

        return $this;
    }

    public function step1($x, $y)
    {
        $n = (4 * $x * $x) + ($y * $y);

        if ($n <= $this->limit && ($n % 12 == 1 || $n % 12 == 5))
        {
            $this->prime[$n] = !$this->prime[$n];
        }
    }

    public function step2($x, $y)
    {
        $n = (3 * $x * $x) + ($y * $y);

        if ($n <= $this->limit && $n % 12 == 7)
        {
            $this->prime[$n] = !$this->prime[$n];
        }
    }

    public function step3($x, $y)
    {
        $n = (3 * $x * $x) - ($y * $y);

        if ($x > $y && $n <= $this->limit && $n % 12 == 11)
        {
            $this->prime[$n] = !$this->prime[$n];
        }
    }

    public function loopY($x)
    {
        for ($y = 1; $y * $y < $this->limit; ++$y)
        {
            $this->step1($x, $y);
            $this->step2($x, $y);
            $this->step3($x, $y);
        }
    }

    public function loopX()
    {
        for ($x = 1; $x * $x < $this->limit; ++$x)
        {
            $this->loopY($x);
        }
    }

    public function calc()
    {
        $this->loopX();
        return $this->omitSquares();
    }
}

function generateTree($l)
{
    $root = new Node();

    foreach ($l as $el)
    {
        /** @var Node $head */
        $head = $root;

        foreach (str_split((string) $el) as $ch)
        {
            if (!isset($head->children[$ch]))
            {
                $head->children[$ch] = new Node();
            }
            $head = $head->children[$ch];
        }

        $head->terminal = true;
    }

    return $root;
}

function find($upperBound, $prefix)
{
    $primes = (new Sieve($upperBound))->calc();
    $strPrefix = (string) $prefix;
    $head = generateTree($primes->toList());

    foreach (str_split($strPrefix) as $ch)
    {
        if (!isset($head->children[$ch]))
        {
            return null;
        }

        $head = $head->children[$ch];
    }

    $queue = [[$head, $strPrefix]];
    $result = [];

    while (count($queue) > 0)
    {
        [$top, $prefix] = array_pop($queue);

        if ($top->terminal)
        {
            $result[] = (int) $prefix;
        }

        foreach ($top->children as $ch => $v)
        {
            array_splice($queue, 0, 0, [[$v, $prefix . $ch]]);
        }
    }

    return $result;
}

(function () {
    print_r(find(UPPER_BOUND, PREFIX));
})();
