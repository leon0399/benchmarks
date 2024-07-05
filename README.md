# Complete Benchmark

World's complete programming language benchmark.

## Results

> [!IMPORTANT]
> This project is not intended to be the sole source for your decisions. Each programming language has its own unique advantages and disadvantages, and performance is only one aspect. Some languages may be more suitable for different projects due to their ecosystem, established best practices, and other factors. Always consider the specific needs and context of your project before making a decision.

> See [`RESULTS.md`](RESULTS.md)

## Running benchmark

### Docker

#### Run full suite

```bash
docker-compose run benchmark python3 ./benchmark.py
```

#### Run specific languages only

```bash
docker-compose run benchmark python3 ./benchmark.py --lang rust go php
```

#### Run specific scripts only

```bash
docker-compose run benchmark python3 ./benchmark.py --script primes/Simple linpack/Linpack recursion/Tak
```

> [!TIP]
> You can combine options above 

### Running manually

```bash
python3 ./benchmark.py
```
