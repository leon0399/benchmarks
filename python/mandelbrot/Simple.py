import time

def index():
  for y in range(-39, 39):
    print()
    for x in range(-39, 39):
      i = mandelbrot(x / 40.0, y / 40.0)

      if i == 0:
        print("*", end="")
      else:
        print(" ", end="")
        

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

if __name__ == "__main__":
  startTimeMs = int(round(time.time() * 1000))

  index()
  
  endTimeMs = int(round(time.time() * 1000))
  executionTime = endTimeMs - startTimeMs

  print(f"Execution time: {executionTime}ms")
