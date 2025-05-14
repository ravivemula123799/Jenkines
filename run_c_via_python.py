import subprocess
import sys

# Step 1: Compile the C program
compile_cmd = ['gcc', 'main.c', '-o', 'main_elf']
print("🔧 Compiling C program...")
compile_proc = subprocess.run(compile_cmd, capture_output=True, text=True)

if compile_proc.returncode != 0:
    print("❌ Compilation failed:\n", compile_proc.stderr)
    sys.exit(1)

print("✅ Compilation successful.")

# Step 2: Run the compiled ELF binary
print("▶️ Running the program...")
run_proc = subprocess.run(['./main_elf'], capture_output=True, text=True)

if run_proc.returncode == 0:
    print("✅ Output:\n", run_proc.stdout)
else:
    print("❌ Runtime Error:\n", run_proc.stderr)
