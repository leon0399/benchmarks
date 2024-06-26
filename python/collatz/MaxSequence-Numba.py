import time
from numba import jit

NUMBER = 500000

@jit(nopython=True)
def collatz(x):
    len = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        len += 1
    return len

@jit(nopython=True)
def findMaxCollatz(to):
    result = (1, 1)
    for number in range(1, to + 1):
        len = collatz(number)
        if len > result[1]:
            result = (number, len)
    return result

if __name__ == "__main__":
    startTimeMs = int(round(time.time() * 1000))

    result = findMaxCollatz(NUMBER)
    print(result)
    
    endTimeMs = int(round(time.time() * 1000))
    executionTime = endTimeMs - startTimeMs
    
    print(f"Execution time: {executionTime}ms")
