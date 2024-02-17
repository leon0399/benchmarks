import time


def mandelbrot(x, y):
    cr = y - 0.5
    ci = x
    zi = 0.0
    zr = 0.0
    i = 0
    while True:
        i += 1
        temp = zr * zi
        zr2 = zr ** 2
        zi2 = zi ** 2
        zr = zr2 - zi2 + cr
        zi = 2 * temp + ci
        if zi2 + zr2 > 16:
            return i
        if i > 5000:
            return 0

def index():
    for y in range(-39, 39):
        line = ""
        for x in range(-39, 39):
            i = mandelbrot(x / 40.0, y / 40.0)
            line += "*" if i == 0 else " "
        print(line)

if __name__ == "__main__":
    startTime = time.time()
    index()
    endTime = time.time()
    duration = endTime - startTime
    print(f"Execution time: {duration:.2f}s")
