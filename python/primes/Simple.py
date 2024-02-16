import time

NUMBER = 100000

def printPrimes(number):
    for num in range(2, number + 1):
        isPrime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            print(num)

if __name__ == "__main__":
    start_time = time.time()
    printPrimes(NUMBER)
    print(f"Execution time: {time.time() - start_time}")
