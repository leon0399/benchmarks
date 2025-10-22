# Complete Benchmark

World's complete programming language benchmark.

## Results

> [!IMPORTANT]
> This project is not intended to be the sole source for your decisions. Each programming language has its own unique advantages and disadvantages, and performance is only one aspect. Some languages may be more suitable for different projects due to their ecosystem, established best practices, and other factors. Always consider the specific needs and context of your project before making a decision.

> See [`RESULTS.md`](RESULTS.md)

## Algorithms

The benchmark suite covers a variety of individual scripts grouped by algorithm family:

- **collatz/MaxSequence** – find the number below a limit that produces the longest Collatz sequence.
- **linpack/Linpack** – solve a dense system of linear equations from the LINPACK benchmark.
- **mandelbrot/Simple** – render an ASCII Mandelbrot set.
- **primes/Atkin** – generate primes using the Sieve of Atkin.
- **primes/Simple** – generate primes via straightforward trial division.
- **recursion/Tak** – compute the Tak function to test deep recursion.
- **treap/Naive** – exercise inserts and deletes on a treap data structure.

### Implementations

The following table shows which languages include implementations of each algorithm.

| Language | collatz/MaxSequence | linpack/Linpack | mandelbrot/Simple | primes/Atkin | primes/Simple | recursion/Tak | treap/Naive |
|---|---|---|---|---|---|---|---|
| c | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| c-plus-plus | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| c-sharp | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| fortran | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| go | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| java | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| javascript | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| kotlin | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| lua | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| perl | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| php | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| python | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ruby | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| rust | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| swift | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| zig | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |

## Running benchmark

### Docker

#### Run full suite

```bash
docker-compose run benchmark python3 ./benchmark.py run --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md
```

#### Run specific languages only

```bash
docker-compose run benchmark python3 ./benchmark.py run --lang rust go php --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md
```

#### Run specific scripts only

```bash
docker-compose run benchmark python3 ./benchmark.py run --script primes/Simple linpack/Linpack recursion/Tak --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md
```

> [!TIP]
> You can combine options above

### Running manually

```bash
python3 ./benchmark.py
```
