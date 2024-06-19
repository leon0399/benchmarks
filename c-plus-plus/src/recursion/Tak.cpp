#include <iostream>
#include <chrono>

int tak(int x, int y, int z) {
    return y < x
        ? tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
        : z;
}

int main() {
    const auto start_time = std::chrono::high_resolution_clock::now();

    std::cout << tak(30, 22, 12) << std::endl;
  
    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;
}
