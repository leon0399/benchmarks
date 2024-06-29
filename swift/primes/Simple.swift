#!/usr/bin/swift

import Foundation

let NUMBER = 100000

func getLastPrime(_ count: Int) -> Int {
    var lastPrime = 2

    for i in 2...count {
        var isPrime = true

        for j in 2...(i / 2 + 1) {
            if i % j == 0 {
                isPrime = false
                break
            }
        }

        if isPrime {
            lastPrime = i
        }
    }

    return lastPrime
}

let startTimeMs = Int(Date().timeIntervalSince1970 * 1000)

let lastPrime = getLastPrime(NUMBER)
print("Last prime: \(lastPrime)")

let endTimeMs = Int(Date().timeIntervalSince1970 * 1000)
let durationMs = endTimeMs - startTimeMs

print("Execution time: \(durationMs)ms")
