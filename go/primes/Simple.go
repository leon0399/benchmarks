package main

import (
	"fmt"
	"time"
)

const NUMBER = 100000

func getLastPrime(count int) int {
	lastPrime := 2

	for i := 2; i <= count; i++ {
		isPrime := true

		for j := 2; j <= i/2; j++ {
			if i%j == 0 {
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

func main() {
	startTime := time.Now()

	lastPrime := getLastPrime(NUMBER)
	fmt.Printf("Last prime: %d\n", lastPrime)

	duration := time.Since(startTime)
	fmt.Printf("Execution time: %dms\n", duration.Milliseconds())
}
