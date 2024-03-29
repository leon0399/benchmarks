#!/usr/bin/env node

class Node {
    constructor(x) {
        this.x = x
        this.y = Math.random()
        this.left = null
        this.right = null
    }
}


function merge(lower, greater) {
    if (lower === null) {
        return greater
    }

    if (greater === null) {
        return lower
    }

    if (lower.y < greater.y) {
        lower.right = merge(lower.right, greater)

        return lower
    } else {
        greater.left = merge(lower, greater.left)

        return greater
    }
}

function splitBinary(orig, value) {
    if (orig === null) {
        return [null, null]
    }

    if (orig.x < value) {
        const splitPair = splitBinary(orig.right, value)
        orig.right = splitPair[0]

        return [orig, splitPair[1]]
    } else {
        const splitPair = splitBinary(orig.left, value)
        orig.left = splitPair[1]

        return [splitPair[0], orig]
    }
}

function merge3(lower, equal, greater) {
    return merge(merge(lower, equal), greater)
}


class SplitResult {
    constructor(lower, equal, greater) {
        this.lower = lower
        this.equal = equal
        this.greater = greater
    }
}


function split(orig, value) {
    const [lower, equalGreater] = splitBinary(orig, value)
    const [equal, greater] = splitBinary(equalGreater, value + 1)

    return new SplitResult(lower, equal, greater)
}


class Tree {
    constructor() {
        this.root = null
    }

    hasValue(x) {
        const splited = split(this.root, x)
        const res = splited.equal !== null
        this.root = merge3(splited.lower, splited.equal, splited.greater)

        return res
    }

    insert(x) {
        const splited = split(this.root, x)

        if (splited.equal === null) {
            splited.equal = new Node(x)
        }

        this.root = merge3(splited.lower, splited.equal, splited.greater)
    }

    erase(x) {
        const splited = split(this.root, x)
        this.root = merge(splited.lower, splited.greater)
    }
}

function main() {
    const tree = new Tree()
    let cur = 5
    let res = 0

    for (let i = 1; i < 1000000; ++i) {
        let a = i % 3
        cur = (cur * 57 + 43) % 10007
        if (a === 0) {
            tree.insert(cur)
        } else if (a === 1) {
            tree.erase(cur)
        } else if (a == 2) {
            res += tree.hasValue(cur) ? 1 : 0
        }
    }
    console.log(res)
}

(async function() {
    const startTimeMs = new Date().getTime();
      
    main();

    const endTimeMs = new Date().getTime();
    const durationMs = endTimeMs - startTimeMs;
    console.log(`Execution time: ${durationMs}ms`);
})();
