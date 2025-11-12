# Contributing to Complete Benchmark

Thank you for your interest in contributing! This guide will help you add new benchmark implementations.

## Core Principle

This benchmark suite compares programming language performance using **identical algorithm implementations**. All implementations must follow the exact same logic as reference implementations to ensure fair comparison.

## Quick Start

1. Check the [implementation status table](README.md#implementations) in README.md
2. Find reference implementations in `langs/php/`, `langs/c-plus-plus/`, or `langs/python/`
3. Implement the algorithm in your target language following the exact logic
4. Test locally with Docker
5. Submit a pull request

## Implementation Guidelines

### Study Reference Implementations First

Before implementing, **always study the reference implementations**:
- Primary references: `langs/php/<algorithm>/<Name>.php`, `langs/c-plus-plus/<algorithm>/<Name>.cpp`, `langs/python/<algorithm>/<Name>.py`
- Use the EXACT same algorithm logic, loop structures, and data structures
- Match the operation order and mathematical calculations

### What You MUST Match

✅ **Required to match:**
- Loop structures and iteration order
- Mathematical operations in the same sequence
- Data structures (use arrays, not specialized structures)
- Algorithm flow and branching logic
- Variable naming patterns (where possible)

### What You CAN Adapt

✅ **Allowed adaptations:**
- Idiomatic syntax for loops (for vs while)
- Standard library I/O functions
- Type declarations as required by language
- Memory management as required by language
- Standard timing/benchmarking utilities

### What is FORBIDDEN

❌ **Not allowed:**
- SIMD instructions or vectorization
- Parallelizing sequential algorithms
- Specialized data structures not in reference
- Compiler directives or JIT-specific hints
- Library-optimized algorithm replacements
- Any optimizations not present in references

## File Structure

### Location
Place your implementation in:
```
langs/<language>/<algorithm>/<Name>.<ext>
```

For languages with multiple runtimes (Kotlin, Java), use suffixes:
- Example: `Simple-JVM.kt` and `Simple-Native.kt`

### File Naming
- Must match the algorithm name exactly (case-sensitive)
- Examples: `Simple.rs`, `Atkin.go`, `Linpack.java`

## Configuration

### Update benchmark.yml

Add your implementation to `langs/<language>/benchmark.yml`:

```yaml
files:
  - algorithm/Name.ext
```

### Update README.md

Change ❌ to ✅ in the implementation table for your algorithm.

## Testing

Test your implementation locally before submitting:

```bash
# Test specific language
docker-compose run benchmark python3 ./benchmark.py run --lang <language> --output jsonl=./.results/results.jsonl

# Test specific algorithm
docker-compose run benchmark python3 ./benchmark.py run --script <algorithm>/<Name> --output jsonl=./.results/results.jsonl
```

Verify:
- Implementation runs without errors
- Output format matches reference implementations
- Timing measurement works correctly

## Pull Request Process

### Title Format
```
feat(<language>): add <algorithm>/<Name> benchmark
```

Examples:
- `feat(rust): add primes/Simple benchmark`
- `feat(go): add linpack/Linpack benchmark`

### What to Include

Your PR should include:
1. Implementation file in correct directory
2. Update to `benchmark.yml`
3. Update to README.md implementation table
4. Clear description of how you verified exact logic match

## Algorithm Families

The benchmark suite includes:

1. **collatz/MaxSequence** – Find number below limit with longest Collatz sequence
2. **linpack/Linpack** – Solve dense system of linear equations (LINPACK benchmark)
3. **mandelbrot/Simple** – Render ASCII Mandelbrot set
4. **primes/Atkin** – Generate primes using Sieve of Atkin
5. **primes/Simple** – Generate primes via trial division
6. **recursion/Tak** – Compute Tak function (deep recursion test)
7. **treap/Naive** – Treap data structure with inserts/deletes

## Common Mistakes to Avoid

1. ❌ Not studying reference implementations before coding
2. ❌ Using language-specific optimizations
3. ❌ Forgetting to update README.md table
4. ❌ Not testing with Docker before submitting
5. ❌ Changing algorithm logic to be "more idiomatic"

## Getting Help

- Check existing implementations in `langs/` for examples
- Review issue #65 for language-specific tracking issues
- Study reference implementations (PHP, C++, Python) carefully

## Project Philosophy

**Fairness over performance. Exact implementation over idiomatic code.**

This benchmark exists to provide apples-to-apples comparison of programming language performance, not to showcase what each language can do when optimized.
