package main

import (
	"fmt"
	"time"
)

const NUMBER = 500000

func collatz(x int) int {
	len := 0

	for x > 1 {
		if x%2 == 0 {
			x = x / 2
		} else {
			x = 3*x + 1
		}
		len++
	}

	return len
}

func findMaxCollatz(to int) (int, int) {
	result := [2]int{1, 1}

	for number := 1; number <= to; number++ {
		len := collatz(number)
		if len > result[1] {
			result = [2]int{number, len}
		}
	}

	return result[0], result[1]
}

func main() {
	startTime := time.Now()

	number, length := findMaxCollatz(NUMBER)
	fmt.Printf("[%d %d]\n", number, length)

	duration := time.Since(startTime)
	fmt.Printf("Execution time: %dms\n", duration.Milliseconds())
}
