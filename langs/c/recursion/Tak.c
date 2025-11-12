#include <stdio.h>
#include <time.h>

int tak(int x, int y, int z) {
    if (y < x)
        return tak(
            tak(x - 1, y, z),
            tak(y - 1, z, x),
            tak(z - 1, x, y)
        );
    else
        return z;
}

int main() {
    clock_t start_time, end_time;
    double duration;

    start_time = clock();

    printf("%d\n", tak(30, 22, 12));

    end_time = clock();
    duration = ((double)(end_time - start_time)) / CLOCKS_PER_SEC * 1000.0;

    printf("Execution time: %.2fms\n", duration);

    return 0;
}
