#include <iostream>
#include <utility>
#include <chrono>

static const auto NUMBER = 500000;

unsigned long long collatz(unsigned long long x) {
    unsigned long long len = 0;

    while (x > 1) {
        if (x % 2 == 0) {
            x = x / 2;
        } else {
            x = 3 * x + 1;
        }
        len++;
    }
    return len;
}

std::pair<int, unsigned long long> findMaxCollatz(int to) {
    std::pair<int, unsigned long long> result = {1, 1};

    for (int number = 1; number <= to; number++) {
        auto len = collatz(static_cast<unsigned long long>(number));
        if (len > result.second) {
            result = {number, len};
        }
    }

    return result;
}

int main() {
    const auto start_time = std::chrono::high_resolution_clock::now();

    const auto result = findMaxCollatz(NUMBER);
    std::cout << "[" << result.first << ", " << result.second << "]" << std::endl;

    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;
    return 0;
}
