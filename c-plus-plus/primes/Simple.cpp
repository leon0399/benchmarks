#include <iostream>

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
    printPrimes(NUMBER);
}