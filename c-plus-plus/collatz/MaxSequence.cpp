#include <iostream>
#include <utility>

static const auto NUMBER = 500000;

int collatz(int x) {
    int len = 0;

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

std::pair<int, int> findMaxCollatz(int to) {
    std::pair<int, int> result = std::make_pair(1, 1);

    for (int number = 1; number <= to; number++) {
        auto len = collatz(number);

        if (len > result.second) {
            result = std::make_pair(number, len);
        }
    }

    return result;
}

int main() {
    auto result = findMaxCollatz(NUMBER);

    std::cout << "[" << result.first << ", " << result.second << "]" << std::endl;
}