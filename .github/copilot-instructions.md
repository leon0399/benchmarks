# GitHub Copilot Instructions for Complete Benchmark Project

## Project Overview

This is a comprehensive programming language benchmark suite comparing performance across 16+ languages using **identical algorithm implementations**. The core principle is exact logical implementation across all languages to ensure fair performance comparison.

## Critical: Always Reference AGENTS.md

**BEFORE implementing or reviewing any benchmark code, you MUST read and follow the guidelines in `/AGENTS.md`.**

Key requirements from AGENTS.md:
- All implementations must follow the **exact same logic** as reference implementations (PHP, C++, Python)
- Study reference implementations in `langs/php/`, `langs/c-plus-plus/`, and `langs/python/` before implementing
- Verify algorithmic equivalence: same loop structures, data structures, and operation order
- NO language-specific optimizations (SIMD, vectorization, parallelization, specialized data structures)
- Implementations must be as similar as possible across languages for fair comparison

## Architecture

```
benchmarks/
├── langs/                    # Language-specific implementations
│   ├── <language>/
│   │   ├── benchmark.yml     # Benchmark configuration
│   │   ├── <algorithm>/      # Algorithm implementations
│   │   │   └── <Name>.<ext>  # Must match exact algorithm name
├── .github/                  # CI/CD workflows
├── AGENTS.md                 # **PRIMARY** implementation guidelines
├── README.md                 # Implementation status table
├── RESULTS.md                # Benchmark results
└── benchmark.py              # Main benchmark runner
```

## Algorithm Families

1. **collatz/MaxSequence** – Longest Collatz sequence below limit
2. **linpack/Linpack** – LINPACK dense linear equation solver
3. **mandelbrot/Simple** – ASCII Mandelbrot set renderer
4. **primes/Atkin** – Sieve of Atkin prime generation
5. **primes/Simple** – Trial division prime generation
6. **recursion/Tak** – Tak function deep recursion test
7. **treap/Naive** – Treap data structure operations

## Implementation Verification Steps

When implementing or reviewing benchmark code:

1. **Study Reference First**: Read `langs/php/<algorithm>/<Name>.php`, `langs/c-plus-plus/<algorithm>/<Name>.cpp`, and `langs/python/<algorithm>/<Name>.py`

2. **Verify Exact Logic Match**:
   - Same variable naming patterns
   - Same loop iteration order (for/while/do-while)
   - Same mathematical operations in same sequence
   - Same data structures (arrays, not specialized collections)
   - Same algorithm flow and branching logic

3. **Check for Forbidden Optimizations**:
   - ❌ SIMD instructions or vectorization
   - ❌ Parallelization of sequential code
   - ❌ Language-specific specialized data structures
   - ❌ Compiler directives or JIT hints
   - ❌ Library-optimized algorithm replacements

4. **Allowed Adaptations Only**:
   - ✅ Idiomatic loop syntax
   - ✅ Standard library I/O
   - ✅ Required type declarations
   - ✅ Language-required memory management
   - ✅ Standard timing utilities

5. **Update Configuration**:
   - Add file to `benchmark.yml` in language directory
   - Update README.md implementation table (❌ → ✅)
   - Follow file naming: `langs/<language>/<algorithm>/<Name>.<ext>`

## Testing

Test implementations locally before submission:

```bash
# Full benchmark suite
docker-compose run benchmark python3 ./benchmark.py run --output jsonl=./.results/results.jsonl --output markdown=./RESULTS.md

# Specific language
docker-compose run benchmark python3 ./benchmark.py run --lang <language> --output jsonl=./.results/results.jsonl

# Specific algorithm
docker-compose run benchmark python3 ./benchmark.py run --script <algorithm>/<Name> --output jsonl=./.results/results.jsonl
```

## Code Review Focus

When reviewing pull requests or generating code reviews:

1. **Primary Check**: Does implementation follow reference implementations exactly?
2. **Compare Side-by-Side**: Check the actual reference implementation files
3. **Flag Optimizations**: Identify any language-specific optimizations not in references
4. **Verify Timing**: Ensure timing code follows language-specific pattern
5. **Check Updates**: Verify README.md table and benchmark.yml are updated

## Project Philosophy

**Fairness over performance. Exact implementation over idiomatic code.**

This benchmark compares language performance with identical algorithms, not developer optimization skills or language-specific features. When in doubt, prioritize exact replication of reference logic.

## Additional Resources

- Reference implementations: `langs/php/`, `langs/c-plus-plus/`, `langs/python/`
- Detailed guidelines: `/AGENTS.md` (always reference this first)
- Implementation tracking: Issue #65 and sub-issues
- Results: `RESULTS.md`
