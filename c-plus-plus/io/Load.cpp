#include <iostream>

static const auto NUMBER = 500000;

void run(int times) {
    int x = 0;

    for (auto i = 0; i <= times; i++) {
        x = i * i;
        std::cout << x << std::endl;
    }

    std::cout << x << std::endl;
}

int main() {
    run(NUMBER);
}