import time

NUMBER = 100000

def printPrimes(number):
    for i in range(2, number + 1):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)

if __name__ == "__main__":
    startTimeMs = int(round(time.time() * 1000))
    printPrimes(NUMBER)
    endTimeMs = int(round(time.time() * 1000))
    executionTime = endTimeMs - startTimeMs
    print(f"Execution time: {executionTime}ms")
