CXXFLAGS = -std=c99 -s -Wall
LDFLAGS = -lm

SCRIPTS = $(wildcard **/*.c)

BINARIES =  $(SCRIPTS:%.c=%-clang) \
			$(SCRIPTS:%.c=%-clang-static) \
			$(SCRIPTS:%.c=%-gcc) \
			$(SCRIPTS:%.c=%-gcc-static) \

%-clang: %.c
	clang -O3 $(CXXFLAGS) -o $@ $< $(LDFLAGS)

%-clang-static: %.c
	clang -O3 $(CXXFLAGS) -static -o $@ $< $(LDFLAGS)

%-gcc : %.c
	gcc -O3 $(CXXFLAGS) -o $@ $< $(LDFLAGS)

%-gcc-static : %.c
	gcc -O3 $(CXXFLAGS) -static -o $@ $< $(LDFLAGS)

all: $(BINARIES)

.PHONY: clean

clean:
	rm -f $(BINARIES)