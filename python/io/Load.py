NUMBER = 500000

def run(times):
    x = 1

    for i in range(times):
        x = i * i
        print(x)

    print(x)

def main():
    run(NUMBER)

main()
