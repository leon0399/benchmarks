import time

NUMBER = 500000

def collatz(x):
    length = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        length += 1
    return length

def findMaxCollatz(to):
    result = (1, 1)
    for number in range(1, to + 1):
        length = collatz(number)
        if len > result[1]:
            result = (number, len)
    return result

if __name__ == "__main__":
    startTimeMs = int(round(time.time() * 1000))
    result = findMaxCollatz(NUMBER)
    endTimeMs = int(round(time.time() * 1000))
    executionTime = endTimeMs - startTimeMs
    print(result)
    print(f"Execution time: {executionTime}ms")
    length = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        length += 1
    return length
