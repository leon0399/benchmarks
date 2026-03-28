# AGENTS.md

Guidance for **AI coding agents** working on the Complete Benchmark project.

**Read [CONTRIBUTING.md](CONTRIBUTING.md) first** — it defines the exact implementation requirement, allowed adaptations, forbidden optimizations, file naming, algorithm families, and PR process. Everything there applies. This file adds agent-specific context.

## Project Overview

Programming language benchmark suite comparing performance across multiple languages using **identical algorithm implementations**. Core principle: exact logical equivalence across all languages for fair comparison.

### Repository Structure

```
benchmarks/
├── langs/                 # Language-specific implementations
│   ├── <language>/
│   │   ├── benchmark.yml  # Benchmark configuration for this language
│   │   ├── <algorithm>/   # Algorithm implementations
│   │   │   └── <Name>.<ext>
├── docker/                # Per-language Dockerfiles
│   ├── _base/
│   ├── <language>/
├── CONTRIBUTING.md        # General contribution guidelines (for humans)
├── README.md              # Main documentation with implementation status table
├── RESULTS.md             # Benchmark results
├── Dockerfile             # All-in-one Docker image
├── docker-compose.yml     # Docker Compose for running benchmarks
└── benchmark.py           # Main benchmark runner
```

## Agent-Specific Rules

### Before Writing Any Code

1. **Read** the PHP, C++, and Python reference implementations for the target algorithm
2. Verify algorithmic equivalence **line-by-line**, not by "it looks similar"
3. When in doubt between idiomatic and exact, choose **exact**

### After Implementation

1. Add the file to `benchmark.yml` under `files:`
2. Update README.md implementation table (change ❌ to ✅)
3. Both updates MUST be in the same PR as the implementation

## Infrastructure Notes

### Language directories without benchmark.yml

`langs/` contains directories for languages that don't yet have a `benchmark.yml` (e.g., dart, elixir, haskell, scala). These are either planned or abandoned. Check README.md's implementation table for the canonical list of active languages.

### Compiled languages

Some languages (Go, Rust, C, C++, Zig) compile to binaries. The benchmark runner or Docker setup handles compilation. Check the language's `benchmark.yml` `command:` field to understand whether the runner expects a source file or a compiled binary.

### Docker images

Each active language has a Dockerfile in `docker/<language>/`. The AIO (all-in-one) image is built from the root `Dockerfile`. When adding a new language, a Docker image may also be needed.

## benchmark.yml

Each language directory must have a `benchmark.yml`. Study an existing one (e.g., `langs/go/benchmark.yml`) as a starting template. Minimal structure:

```yaml
title: 'Language Name'

strategy:
  matrix:
    command:
      - title: 'Variant Name'
        command: './{file}'  # or 'python{version} {file}', etc.

    files:
      - algorithm/Name.ext
```

Optional `versions:` section is used by languages with multiple runtimes (PHP, Python, Node). Check existing `benchmark.yml` files for the pattern that fits your language.

**Important**:
- List all implemented algorithm files under `files:`
- Use `{version}` placeholder for version substitution (when using `versions:`)
- Use `{file}` placeholder for file path
- Disable JIT/optimizations where they would violate fairness

## Testing

```bash
# Full benchmark suite
docker-compose run benchmark python3 ./benchmark.py run --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md

# Test specific language only
docker-compose run benchmark python3 ./benchmark.py run --lang <language> --output jsonl=./.results/results.jsonl

# Test specific algorithm only
docker-compose run benchmark python3 ./benchmark.py run --script <algorithm>/<Name> --output jsonl=./.results/results.jsonl
```

## Development Workflow

1. Check the implementation status table in README.md to see what's missing
2. Find the corresponding GitHub issue (check issue #65 for language tracking issues)
3. Study reference implementations (PHP, C++, Python) for the algorithm
4. Implement with exact logic in the target language
5. Add to `benchmark.yml` in the language directory
6. Test locally using Docker
7. Update README.md table to mark the algorithm as ✅ implemented
8. Submit PR with clear description

## Commit & PR Conventions

### Commit message format

```
feat(<language>): add <algorithm>/<Name> benchmark
```

### PR checklist

- [ ] Implementation follows exact logic of reference implementations
- [ ] No language-specific optimizations added
- [ ] File placed in correct directory: `langs/<language>/<algorithm>/<Name>.<ext>`
- [ ] Added to `benchmark.yml` in language directory
- [ ] README.md implementation table updated
- [ ] Tested with Docker locally

## Getting Help

- Check existing implementations in `langs/` for examples of the target language's patterns
- Review tracking issues: issue #65 for language-specific tracking
- Study reference implementations (PHP, C++, Python) carefully before implementing
- When in doubt, prioritize **fairness over performance** and **exact implementation over idiomatic code**
