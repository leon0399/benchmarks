#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>

#define NUMBER 500000

int getLastPrime(int count) {
    int lastPrime = 0;

    for (int i = 3; i <= count; i += 2) {
        bool isPrime = true;
        int limit = sqrt(i);

        for (int j = 3; j <= limit; j += 2) {
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
