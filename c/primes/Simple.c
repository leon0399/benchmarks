#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#define NUMBER 100000

int getLastPrime(int count) {
    int lastPrime = 0;

    for (int i = 2; i <= count; i++) {
        bool isPrime = true;

        for (int j = 2; j <= i / 2; ++j) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            lastPrime = i;
        }
    }

    return lastPrime;
}

int main() {
    clock_t start_time = clock();

    int last_prime = getLastPrime(NUMBER);
    printf("Last prime: %d\n", last_prime);
  
    clock_t end_time = clock();
    double duration = ((double)(end_time - start_time)) / CLOCKS_PER_SEC * 1000.0;
    
    printf("Execution time: %.2fms\n", duration);

    return 0;
}
