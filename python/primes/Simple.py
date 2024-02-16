#!/usr/bin/env python3

import time

NUMBER = 100000

def print_primes(count):
    for num in range(2, count + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

if __name__ == "__main__":
    start_time = time.time()
    print_primes(NUMBER)
    end_time = time.time()
    duration = (end_time - start_time) * 1000
    print(f"Execution time: {duration}ms")
