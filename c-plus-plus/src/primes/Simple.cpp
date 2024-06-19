#include <iostream>
#include <chrono>

static const auto NUMBER = 100000;

auto getLastPrime(int count) -> int
{
    auto lastPrime = 0;

    for (auto i = 2; i <= count; i++) {
        bool isPrime = true;

        for (auto j = 2; j <= i / 2; ++j) {
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
    const auto start_time = std::chrono::high_resolution_clock::now();

    const auto last_prime = getLastPrime(NUMBER);
    std::cout << "Last prime: " << last_prime << std::endl;
  
    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;

    return 0;
}