package main

const NUMBER = 500000

func run(times int) {
	x := 0

	for i := 1; i < times; i++ {
		x = i * i
	}

	println(x)
}

func main() {
	run(NUMBER)
}
