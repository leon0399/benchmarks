package main

import (
	"fmt"
	"time"
)

func index() {
	for y := -39; y < 39; y++ {
		fmt.Printf("\n")

		for x := -39; x < 39; x++ {
			i := mandelbrot(
				float64(x)/40.0,
				float64(y)/40.0,
			)

			if i == 0 {
				fmt.Printf("*")
			} else {
				fmt.Printf(" ")
			}
		}
	}

	fmt.Printf("\n")
}

func mandelbrot(x, y float64) int {
	cr := y - 0.5
	ci := x
	zi := 0.0
	zr := 0.0
	i := 0

	for {
		i++

		temp := zr * zi

		zr2 := zr * zr
		zi2 := zi * zi

		zr = zr2 - zi2 + cr
		zi = temp + temp + ci

		if zi2+zr2 > 16 {
			return i
		}

		if i > 5000 {
			return 0
		}
	}
}

func main() {
	startTime := time.Now()

	index()

	duration := time.Since(startTime)
	fmt.Printf("Execution time: %dms\n", duration.Milliseconds())
}
