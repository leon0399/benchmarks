package main

import (
	"fmt"
	"strconv"
	"time"
)

const (
	UPPER_BOUND = 5000000
	PREFIX      = 32338
)

type Node struct {
	children map[rune]*Node
	terminal bool
}

func NewNode() *Node {
	return &Node{children: make(map[rune]*Node), terminal: false}
}

type Sieve struct {
	limit int
	prime []bool
}

func NewSieve(limit int) *Sieve {
	return &Sieve{
		limit: limit,
		prime: make([]bool, limit+1),
	}
}

func (s *Sieve) toList() []int {
	result := []int{2, 3}
	for p := 5; p <= s.limit; p++ {
		if s.prime[p] {
			result = append(result, p)
		}
	}
	return result
}

func (s *Sieve) omitSquares() *Sieve {
	for r := 5; r*r < s.limit; r++ {
		if s.prime[r] {
			for i := r * r; i < s.limit; i += r * r {
				s.prime[i] = false
			}
		}
	}
	return s
}

func (s *Sieve) step1(x, y int) {
	n := (4 * x * x) + (y * y)
	if n <= s.limit && (n%12 == 1 || n%12 == 5) {
		s.prime[n] = !s.prime[n]
	}
}

func (s *Sieve) step2(x, y int) {
	n := (3 * x * x) + (y * y)
	if n <= s.limit && n%12 == 7 {
		s.prime[n] = !s.prime[n]
	}
}

func (s *Sieve) step3(x, y int) {
	n := (3 * x * x) - (y * y)
	if x > y && n <= s.limit && n%12 == 11 {
		s.prime[n] = !s.prime[n]
	}
}

func (s *Sieve) loopY(x int) {
	for y := 1; y*y < s.limit; y++ {
		s.step1(x, y)
		s.step2(x, y)
		s.step3(x, y)
	}
}

func (s *Sieve) loopX() {
	for x := 1; x*x < s.limit; x++ {
		s.loopY(x)
	}
}

func (s *Sieve) calc() *Sieve {
	s.loopX()
	return s.omitSquares()
}

func generateTree(l []int) *Node {
	root := NewNode()
	for _, el := range l {
		head := root
		for _, ch := range strconv.Itoa(el) {
			if _, exists := head.children[ch]; !exists {
				head.children[ch] = NewNode()
			}
			head = head.children[ch]
		}
		head.terminal = true
	}
	return root
}

func find(upperBound, prefix int) []int {
	primes := NewSieve(upperBound).calc()
	strPrefix := strconv.Itoa(prefix)
	head := generateTree(primes.toList())

	for _, ch := range strPrefix {
		if _, exists := head.children[ch]; !exists {
			return nil
		}
		head = head.children[ch]
	}

	queue := [][2]interface{}{{head, strPrefix}}
	result := []int{}

	for len(queue) > 0 {
		n := len(queue) - 1
		top, prefix := queue[n][0].(*Node), queue[n][1].(string)
		queue = queue[:n]

		if top.terminal {
			p, _ := strconv.Atoi(prefix)
			result = append(result, p)
		}

		for ch, child := range top.children {
			queue = append([][2]interface{}{{child, prefix + string(ch)}}, queue...)
		}
	}

	return result
}

func main() {
	startTime := time.Now()

	result := find(UPPER_BOUND, PREFIX)
	fmt.Println(result)

	duration := time.Since(startTime)
	fmt.Printf("Execution time: %v\n", duration)
}
