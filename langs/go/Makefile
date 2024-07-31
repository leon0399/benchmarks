SCRIPTS = $(wildcard **/*.go)

BINARIES = $(SCRIPTS:%.go=%)

%: %.go
	GO111MODULE=off go build -o $@ $<
	strip -s $@
	chmod u+x $@

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)
