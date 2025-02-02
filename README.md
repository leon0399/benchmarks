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
