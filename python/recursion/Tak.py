import time

def tak(x, y, z):
    if (y < x):
        return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
    else:
        return z
    
startTimeMs = int(round(time.time() * 1000))

print(tak(30, 22, 12))

endTimeMs = int(round(time.time() * 1000))
executionTime = endTimeMs - startTimeMs
print(f"Execution time: {executionTime}ms")
