#include <iostream>

int tak(int x, int y, int z) {
    return y < x
        ? tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
        : z;
}

int main() {
    std::cout << tak(30, 22, 12) << std::endl;
}
