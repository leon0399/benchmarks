package main

import (
	"fmt"
	"time"
	"math"
)

const NUMBER = 500000

func getLastPrime(count int) int {
	lastPrime := 2

	for i := 3; i <= count; i += 2 {
		isPrime := true
		limit := int(math.Sqrt(float64(i)))

		for j := 3; j <= limit; j += 2 {
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

func main() {
	startTime := time.Now()

	lastPrime := getLastPrime(NUMBER)
	fmt.Printf("Last prime: %d\n", lastPrime)

	duration := time.Since(startTime)
	fmt.Printf("Execution time: %dms\n", duration.Milliseconds())
}
