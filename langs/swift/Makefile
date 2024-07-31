SCRIPTS = $(wildcard **/*.swift)

BINARIES =  $(SCRIPTS:%.swift=%)

%: %.swift
	swiftc -O -o $@ $<

all: $(BINARIES)

.PHONY: clean

clean:
	rm -f $(BINARIES)