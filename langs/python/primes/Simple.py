import time
from math import sqrt

limit = 1000000

def get_last_prime(count):
    last_prime = 2

    # Traverse each number from 1 to N with the help of for loop
    for num in range(3, count, 2):
        is_prime = True
        limit = int(sqrt(num))

        for i in range(3, limit, 2):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            last_prime = num

    return last_prime

if __name__ == "__main__":
    start_time_ms = int(round(time.time() * 1000))

    last_prime = get_last_prime(limit)
    print(f"Last prime: {last_prime}")
    
    end_time_ms = int(round(time.time() * 1000))
    execution_time = end_time_ms - start_time_ms
    print(f"Execution time: {execution_time}ms")
