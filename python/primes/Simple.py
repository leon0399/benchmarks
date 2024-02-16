import time


def print_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    start_time_ms = int(round(time.time() * 1000))
    limit = 100000
    primes = print_primes(limit)
    for prime in primes:
        print(prime)
    end_time_ms = int(round(time.time() * 1000))
    print(f"Execution time: {end_time_ms - start_time_ms}ms")
