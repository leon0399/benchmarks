import time

limit = 100000

def print_primes(limit):
    last_prime = 2

    # Traverse each number from 1 to N with the help of for loop
    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
            
        if is_prime:
            last_prime = num

    return last_prime

if __name__ == "__main__":
    start_time_ms = int(round(time.time() * 1000))

    primes = print_primes(limit)
    
    end_time_ms = int(round(time.time() * 1000))
    execution_time = end_time_ms - start_time_ms
    print(f"Execution time: {execution_time}ms")
