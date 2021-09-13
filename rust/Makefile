RUSTC_FLAGS := -C opt-level=3 -C target-cpu=native -C llvm-args=--x86-branches-within-32B-boundaries

SCRIPTS = $(wildcard **/*.rs)

BINARIES = $(SCRIPTS:%.rs=%)

%: %.rs
	rustc $(RUSTC_FLAGS) -C lto -C codegen-units=1 -o $@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)