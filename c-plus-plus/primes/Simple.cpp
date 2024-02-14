#include <iostream>
#include <chrono>

static const auto NUMBER = 100000;

void printPrimes(int count) {
    // Traverse each number from 1 to N with the help of for loop
    for (auto i = 1; i <= count; i++) {
        if (i == 1 || i == 0) {
            continue;
        }

        bool isPrime = true;

        for (auto j = 2; j <= i / 2; ++j) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            std::cout << i << std::endl;
        }
    }
}

int main() {
    const auto start_time = std::chrono::high_resolution_clock::now();

    printPrimes(NUMBER);
  
    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;
}