#include <iostream>
#include <chrono>
#include <cmath>

static const auto NUMBER = 500000;

auto getLastPrime(int count) -> int
{
    auto lastPrime = 0;

    for (auto i = 3; i <= count; i += 2) {
        bool isPrime = true;
        int limit = static_cast<int>(std::sqrt(i));

        for (auto j = 3; j <= limit; j += 2) {
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