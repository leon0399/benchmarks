SCRIPTS = $(wildcard **/*.cs)

BINARIES =  $(SCRIPTS:%.cs=%-csc.exe) \
			$(SCRIPTS:%.cs=%-mcs.exe)

%-csc.exe: %.cs
	mono-csc $< -out:$@

%-mcs.exe: %.cs
	mcs $< -out:$@

all: $(BINARIES)

.PHONY: clean

clean:
	rm -f $(BINARIES)
