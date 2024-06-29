CXXFLAGS = -std=c99 -s -Wall

SCRIPTS = $(wildcard **/*.c)

BINARIES =  $(SCRIPTS:%.c=%-clang) \
			$(SCRIPTS:%.c=%-clang-static) \
			$(SCRIPTS:%.c=%-gcc) \
			$(SCRIPTS:%.c=%-gcc-static) \

%-clang: %.c
	clang -O3 $(CXXFLAGS) -o $@ $<

%-clang-static: %.c
	clang -O3 $(CXXFLAGS) -static -o $@ $<

%-gcc : %.c
	gcc -O3 $(CXXFLAGS) -o $@ $<

%-gcc-static : %.c
	gcc -O3 $(CXXFLAGS) -static -o $@ $<

all: $(BINARIES)

.PHONY: clean

clean:
	rm -f $(BINARIES)