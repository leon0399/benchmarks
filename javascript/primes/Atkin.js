#!/usr/bin/env node

'use strict';

const UPPER_BOUND = 5000000;
const PREFIX = 32338;

class Node {
    constructor() {
        this.children = new Map();
        this.terminal = false;
    }
}

const toInt = function(n) {
    return n >>> 0;
}

class Sieve {
    constructor(limit) {
        this.limit = limit;
        this.prime = new Int8Array(limit + 1);
    }

    toList() {
        const result = [2, 3];
        for (let p = 5; p <= this.limit; ++p) {
            if (this.prime[p]) {
                result.push(p);
            }
        }
        return result;
    }

    omitSquares() {
        for (let r = 5; r * r < this.limit; ++r) {
            if (this.prime[r]) {
                for (let i = r * r; i < this.limit; i += r * r) {
                    this.prime[i] = 0;
                }
            }
        }
        return this;
    }

    step1(x, y) {
        const n = (4 * x * x) + (y * y);
        if (n <= this.limit && (n % 12 == 1 || n % 12 == 5)) {
            this.prime[n] = !this.prime[n];
        }
    }

    step2(x, y) {
        const n = (3 * x * x) + (y * y);
        if (n <= this.limit && n % 12 == 7) {
            this.prime[n] = !this.prime[n];
        }
    }

    step3(x, y) {
        const n = (3 * x * x) - (y * y);
        if (x > y && n <= this.limit && n % 12 == 11) {
            this.prime[n] = !this.prime[n];
        }
    }

    loopY(x) {
        for (let y = 1; y * y < this.limit; ++y) {
            this.step1(x, y);
            this.step2(x, y);
            this.step3(x, y);
        }
    }

    loopX() {
        for (let x = 1; x * x < this.limit; ++x) {
            this.loopY(x);
        }
    }

    calc() {
        this.loopX();
        return this.omitSquares();
    }
}

function generateTree(l) {
    const root = new Node()
    for (const el of l) {
        let head = root;
        for (const ch of el.toString()) {
            if (!head.children.has(ch)) {
                head.children.set(ch, new Node());
            }
            head = head.children.get(ch);
        }
        head.terminal = true;
    }
    return root;
}

function find(upperBound, prefix) {
    const primes = new Sieve(upperBound).calc();
    const strPrefix = prefix.toString();
    let head = generateTree(primes.toList());

    for (const ch of strPrefix) {
        head = head.children.get(ch);
        if (typeof head === 'undefined') {
            return null;
        }
    }

    let [queue, result] = [[[head, strPrefix]], []]
    while (queue.length > 0) {
        const [top, prefix] = queue.pop();
        if (top.terminal) {
            result.push(toInt(prefix));
        }

        for (const [ch, v] of top.children) {
            queue.splice(0, 0, [v, prefix + ch]);
        }
    }
    return result;
}

(async function() {
    const startTimeMs = new Date().getTime();
      
    console.log(find(UPPER_BOUND, PREFIX));

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();
