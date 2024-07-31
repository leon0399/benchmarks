SCRIPTS = $(wildcard **/*.zig)

BINARIES =  $(SCRIPTS:%.zig=%) \

%: %.zig
	zig build-exe -O ReleaseFast -femit-bin=$@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)
