import subprocess
import sys

# Example input (for demonstration, replace with actual changed files list)
# changed_files = ["rust/collatz/MaxSequence.rs", "python/primes/Atkin.py"]
changed_files = sys.argv[1:]  # Accepting changed files as command-line arguments

# Parsing changed files to find unique language-script pairs
benchmark_commands = set()
for file_path in changed_files:
    parts = file_path.split('/')
    if len(parts) < 3:
        continue  # Skip invalid paths
    language, category, script = parts[0], parts[1], parts[2]
    script_name = script.split('.')[0]  # Extract script name without extension
    # Assuming the benchmark script supports language and script parameters
    command = f"python3 ./benchmark.py --languages {language} --scripts {category}/{script_name} --times 1"
    benchmark_commands.add(command)

# Executing benchmark commands
for command in benchmark_commands:
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)