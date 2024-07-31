#!/usr/bin/swift

import Foundation

let NUMBER = 1000000

func getLastPrime(_ count: Int) -> Int {
    var lastPrime = 2

    for i in stride(from: 3, to: count, by: 2) {
        var isPrime = true
        var limit = Int(sqrt(Double(i)))

        for j in stride(from: 3, to: limit, by: 2) {
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
