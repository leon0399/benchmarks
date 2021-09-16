SCRIPTS = $(wildcard **/*.kt)

BINARIES =  $(SCRIPTS:%-JVM.kt=%.jar) \
			$(SCRIPTS:%-Native.kt=%.kexe) \

%.jar: %-JVM.kt
	kotlinc -include-runtime -d $@ $<

%.kexe: %-Native.kt
	kotlinc-native -opt -linker-options -s -output $@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)
