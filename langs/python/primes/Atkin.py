import time

UPPER_BOUND = 5000000
PREFIX = 32338

class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False


class Sieve:
    def __init__(self, limit):
        self.limit = limit
        self.prime = [False] * (limit + 1)

    def to_list(self):
        result = [2, 3]
        for p in range(5, self.limit + 1):
            if self.prime[p]:
                result.append(p)
        return result

    def omit_squares(self):
        r = 5
        while r * r < self.limit:
            if self.prime[r]:
                i = r * r
                while i < self.limit:
                    self.prime[i] = False
                    i = i + r * r
            r = r + 1
        return self

    def step1(self, x, y):
        n = (4 * x * x) + (y * y)
        if n <= self.limit and (n % 12 == 1 or n % 12 == 5):
            self.prime[n] = not self.prime[n]

    def step2(self, x, y):
        n = (3 * x * x) + (y * y)
        if n <= self.limit and n % 12 == 7:
            self.prime[n] = not self.prime[n]

    def step3(self, x, y):
        n = (3 * x * x) - (y * y)
        if x > y and n <= self.limit and n % 12 == 11:
            self.prime[n] = not self.prime[n]

    def loop_y(self, x):
        y = 1
        while y * y < self.limit:
            self.step1(x, y)
            self.step2(x, y)
            self.step3(x, y)
            y = y + 1

    def loop_x(self):
        x = 1
        while x * x < self.limit:
            self.loop_y(x)
            x = x + 1

    def calc(self):
        self.loop_x()
        return self.omit_squares()


def generate_tree(l):
    root = Node()
    for el in l:
        head = root
        for ch in str(el):
            if ch not in head.children:
                head.children[ch] = Node()
            head = head.children[ch]
        head.terminal = True
    return root


def find(upper_bound, prefix):
    primes = Sieve(upper_bound).calc()
    str_prefix = str(prefix)
    head = generate_tree(primes.to_list())
    for ch in str_prefix:
        head = head.children.get(ch)
        if head is None:
            return None

    queue, result = [(head, str_prefix)], []
    while queue:
        top, prefix = queue.pop()
        if top.terminal:
            result.append(int(prefix))
        for ch, v in top.children.items():
            queue.insert(0, (v, prefix + ch))
    return result


def run():
    startTimeMs = int(round(time.time() * 1000))

    print(find(UPPER_BOUND, PREFIX))

    endTimeMs = int(round(time.time() * 1000))
    executionTime = endTimeMs - startTimeMs
    print(f"Execution time: {executionTime}ms")

run()