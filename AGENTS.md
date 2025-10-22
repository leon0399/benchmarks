# AGENTS.md

This file provides guidance for AI coding agents working on the Complete Benchmark project.

## Project Overview

This is a comprehensive programming language benchmark suite comparing performance across multiple languages using identical algorithm implementations. The project's core principle is **exact logical implementation** across all languages to ensure fair comparison.

### Key Principles

1. **Exact Implementation**: All algorithm implementations must follow the exact same logic as reference implementations (PHP, C++, Python) without any language-specific optimizations
2. **Fair Comparison**: The goal is to compare language performance, not developer optimization skills
3. **Comprehensive Coverage**: We benchmark 7 algorithm families across 16+ programming languages

### Repository Structure

```
benchmarks/
├── langs/                 # Language-specific implementations
│   ├── <language>/
│   │   ├── benchmark.yml  # Benchmark configuration for this language
│   │   ├── <algorithm>/   # Algorithm implementations
│   │   │   └── <Name>.<ext>
├── README.md              # Main documentation with implementation status table
├── RESULTS.md             # Benchmark results
└── benchmark.py           # Main benchmark runner
```

## Critical Rules for Adding Implementations

### ⚠️ MOST IMPORTANT: Exact Implementation Requirement

When implementing a benchmark in a new language, you **MUST**:

1. **Study the reference implementations first**:
   - Primary references: `langs/php/<algorithm>/<Name>.php`, `langs/c-plus-plus/<algorithm>/<Name>.cpp`, `langs/python/<algorithm>/<Name>.py`
   - Use the EXACT same algorithm logic, loop structures, and data structures
   - Do NOT optimize or use language-specific features that would give unfair advantage

2. **Maintain algorithmic equivalence**:
   - Same variable naming patterns where possible
   - Same loop iteration order
   - Same mathematical operations in same order
   - Same data structure choices (arrays, not specialized structures)

3. **Examples of FORBIDDEN optimizations**:
   - ❌ Using SIMD instructions
   - ❌ Replacing loops with vectorized operations
   - ❌ Using specialized data structures not in reference
   - ❌ Parallelizing sequential algorithms
   - ❌ Using JIT-specific hints or compiler directives
   - ❌ Replacing algorithms with library-optimized equivalents

4. **Allowed language adaptations**:
   - ✅ Idiomatic syntax for loops (for vs while)
   - ✅ Standard library I/O functions
   - ✅ Type declarations as required by language
   - ✅ Memory management as required by language
   - ✅ Standard timing/benchmarking utilities

### File Naming and Location

- Place implementations in: `langs/<language>/<algorithm>/<Name>.<ext>`
- For languages with multiple runtimes (Kotlin, Java), use suffixes:
  - Example: `Simple-JVM.kt` and `Simple-Native.kt`
- File names must match the algorithm name exactly (case-sensitive)

### Algorithm Families

The benchmark suite includes these algorithm families:

1. **collatz/MaxSequence** – Find number below limit with longest Collatz sequence
2. **linpack/Linpack** – Solve dense system of linear equations (LINPACK benchmark)
3. **mandelbrot/Simple** – Render ASCII Mandelbrot set
4. **primes/Atkin** – Generate primes using Sieve of Atkin
5. **primes/Simple** – Generate primes via trial division
6. **recursion/Tak** – Compute Tak function (deep recursion test)
7. **treap/Naive** – Treap data structure with inserts/deletes

## Development Workflow

### Adding a New Language Implementation

1. **Check the implementation status table** in README.md to see what's missing
2. **Find the corresponding GitHub issue** (check issue #65 for language tracking issues)
3. **Study reference implementations** (PHP, C++, Python) for the algorithm
4. **Implement with exact logic** in the target language
5. **Add to benchmark.yml** in the language directory
6. **Test locally** using Docker or manual runs
7. **Update README.md table** to mark the algorithm as ✅ implemented
8. **Submit PR** with clear description of what was implemented

### Updating README.md Implementation Table

**CRITICAL**: After implementing a new algorithm, you MUST update the implementation status table in README.md:

1. Locate the table under "### Implementations" section
2. Find the row for your language
3. Change ❌ to ✅ for the implemented algorithm column
4. Ensure the change is included in your PR

Example:
```markdown
| Language | collatz/MaxSequence | ... |
|----------|---------------------|-----|
| rust     | ❌ → ✅              | ... |
```

### benchmark.yml Structure

Each language directory must have a `benchmark.yml` file:

```yaml
title: 'Language Name'

strategy:
  matrix:
    versions:
      - version: X.Y
        tags:
          - Optional

    command:
      - title: 'Runtime Variant'
        command: 'executable{version} args --file {file}'

    files:
      - algorithm/Name.ext
```

**Important**:
- List all implemented algorithm files under `files:`
- Use `{version}` placeholder for version substitution
- Use `{file}` placeholder for file path
- Disable JIT/optimizations where they would violate fairness

## Testing Instructions

### Running Benchmarks Locally

#### Full benchmark suite:
```bash
docker-compose run benchmark python3 ./benchmark.py run --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md
```

#### Test specific language only:
```bash
docker-compose run benchmark python3 ./benchmark.py run --lang <language> --output jsonl=./.results/results.jsonl
```

#### Test specific algorithm only:
```bash
docker-compose run benchmark python3 ./benchmark.py run --script <algorithm>/<Name> --output jsonl=./.results/results.jsonl
```

### Validation Checklist

Before submitting a PR, verify:

- [ ] Implementation follows exact logic of reference implementations
- [ ] No language-specific optimizations added
- [ ] File placed in correct directory: `langs/<language>/<algorithm>/<Name>.<ext>`
- [ ] Added to `benchmark.yml` in language directory
- [ ] README.md implementation table updated
- [ ] Tested with Docker locally
- [ ] Code follows language-specific style conventions (when not conflicting with exact implementation requirement)

## Pull Request Guidelines

### PR Title Format

```
Add <algorithm>/<Name> benchmark in <Language>
```

Examples:
- `Add primes/Simple benchmark in Rust`
- `Add linpack/Linpack benchmark in Go`

### PR Description Template

```markdown
## Summary
Implements `<algorithm>/<Name>` benchmark in <Language>.

## Implementation Notes
- Follows exact logic from reference implementations: PHP, C++, Python
- No optimizations added beyond reference implementation
- Tested locally with Docker

## Checklist
- [ ] Exact implementation verified against references
- [ ] Added to benchmark.yml
- [ ] README.md table updated
- [ ] Local tests passing
```

### Commit Message Guidelines

Use conventional commits format:

```
feat(<language>): add <algorithm>/<Name> benchmark

Implements exact replica of reference implementation without optimizations.
```

## Code Style Guidelines

### General Rules

1. **Follow language conventions** for formatting and naming (as long as it doesn't conflict with exact implementation requirement)
2. **Include timing code** matching the pattern used in existing implementations for that language
3. **Print results to stdout** in the same format as reference implementations
4. **Avoid external dependencies** where possible (use standard library)

### Timing Implementation

Each implementation must measure and report execution time. Study existing implementations in the target language to see the pattern used.

Example patterns:
- **PHP**: `microtime(true)` before/after
- **Python**: `time.time()` or `time.perf_counter()`
- **C++**: `std::chrono::high_resolution_clock`
- **Rust**: `std::time::Instant`

## Common Pitfalls to Avoid

1. **❌ Using language-specific optimized libraries** instead of implementing the algorithm
2. **❌ Changing algorithm logic** to "make it more idiomatic"
3. **❌ Forgetting to update README.md** implementation table
4. **❌ Not testing with Docker** before submitting
5. **❌ Using compiler optimization flags** not used in reference implementations
6. **❌ Parallelizing sequential algorithms** for "better performance"
7. **❌ Assuming similar-looking code is equivalent** - verify logic step-by-step

## Getting Help

- Check existing implementations in `langs/` for examples
- Review tracking issues: See issue #65 for language-specific tracking issues
- Each language has sub-issues for individual algorithms with detailed requirements
- Study reference implementations (PHP, C++, Python) carefully before implementing

## Project Philosophy

This benchmark suite exists to provide fair, apples-to-apples comparison of programming language performance. The value comes from **exact replication** of logic across languages, not from showcasing what each language can do when optimized.

When in doubt, prioritize **fairness over performance** and **exact implementation over idiomatic code**.
