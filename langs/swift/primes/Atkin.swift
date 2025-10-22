#!/usr/bin/swift

import Foundation

let UPPER_BOUND = 5000000
let PREFIX = 32338

class Node {
    var children: [Character: Node] = [:]
    var terminal: Bool = false
    
    init() {
        self.children = [:]
        self.terminal = false
    }
}

class Sieve {
    var limit: Int
    var prime: [Bool]
    
    init(_ limit: Int) {
        self.limit = limit
        self.prime = Array(repeating: false, count: limit + 1)
    }
    
    func toList() -> [Int] {
        var result = [2, 3]
        for p in 5...limit {
            if prime[p] {
                result.append(p)
            }
        }
        return result
    }
    
    func omitSquares() -> Sieve {
        var r = 5
        while r * r < limit {
            if prime[r] {
                var i = r * r
                while i < limit {
                    prime[i] = false
                    i = i + r * r
                }
            }
            r = r + 1
        }
        return self
    }
    
    func step1(_ x: Int, _ y: Int) {
        let n = (4 * x * x) + (y * y)
        if n <= limit && (n % 12 == 1 || n % 12 == 5) {
            prime[n] = !prime[n]
        }
    }
    
    func step2(_ x: Int, _ y: Int) {
        let n = (3 * x * x) + (y * y)
        if n <= limit && n % 12 == 7 {
            prime[n] = !prime[n]
        }
    }
    
    func step3(_ x: Int, _ y: Int) {
        let n = (3 * x * x) - (y * y)
        if x > y && n <= limit && n % 12 == 11 {
            prime[n] = !prime[n]
        }
    }
    
    func loopY(_ x: Int) {
        var y = 1
        while y * y < limit {
            step1(x, y)
            step2(x, y)
            step3(x, y)
            y = y + 1
        }
    }
    
    func loopX() {
        var x = 1
        while x * x < limit {
            loopY(x)
            x = x + 1
        }
    }
    
    func calc() -> Sieve {
        loopX()
        return omitSquares()
    }
}

func generateTree(_ l: [Int]) -> Node {
    let root = Node()
    for el in l {
        var head = root
        for ch in String(el) {
            if head.children[ch] == nil {
                head.children[ch] = Node()
            }
            head = head.children[ch]!
        }
        head.terminal = true
    }
    return root
}

func find(_ upperBound: Int, _ prefix: Int) -> [Int]? {
    let primes = Sieve(upperBound).calc()
    let strPrefix = String(prefix)
    var head = generateTree(primes.toList())
    
    for ch in strPrefix {
        if let next = head.children[ch] {
            head = next
        } else {
            return nil
        }
    }
    
    var queue: [(Node, String)] = [(head, strPrefix)]
    var result: [Int] = []
    
    while !queue.isEmpty {
        let (top, prefix) = queue.removeLast()
        if top.terminal {
            result.append(Int(prefix)!)
        }
        for (ch, v) in top.children.sorted(by: { $0.key < $1.key }) {
            queue.insert((v, prefix + String(ch)), at: 0)
        }
    }
    
    return result
}

let startTimeMs = Int(Date().timeIntervalSince1970 * 1000)

if let result = find(UPPER_BOUND, PREFIX) {
    print(result)
} else {
    print("[]")
}

let endTimeMs = Int(Date().timeIntervalSince1970 * 1000)
let durationMs = endTimeMs - startTimeMs

print("Execution time: \(durationMs)ms")
