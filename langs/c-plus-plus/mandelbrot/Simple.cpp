#include <iostream>
#include <chrono>

int mandelbrot(double x, double y) {
    double cr = y - 0.5;
    double ci = x;

    double zi = 0.0;
    double zr = 0.0;
    int i = 0;

    while (true) {
        i++;

        double temp = zr * zi;

        double zr2 = zr * zr;
        double zi2 = zi * zi;

        zr = zr2 - zi2 + cr;
        zi = temp + temp + ci;

        if (zi2 + zr2 > 16) {
            return i;
        }

        if (i > 5000) {
            return 0;
        }
    }
}

void index()
{
    for (auto y = -39; y < 39; y++) {
        std::cout << std::endl;

        for (auto x = -39; x < 39; x++) {
            auto i = mandelbrot(
                (double) x / 40.0,
                (double) y / 40.0
            );

            if (i == 0) {
                std::cout << "*";
            } else {
                std::cout << " ";
            }
        }
    }

    std::cout << std::endl;
}

int main() {
    const auto start_time = std::chrono::high_resolution_clock::now();

    index();
    
    const auto end_time = std::chrono::high_resolution_clock::now();
    const auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    std::cout << "Execution time: " << duration << "ms" << std::endl;
}