SCRIPTS = $(wildcard **/*.kt)

BINARIES =	$(SCRIPTS:%-JVM.kt=%.jar) \
			$(SCRIPTS:%-Native.kt=%.kexe) \
			$(SCRIPTS:%-JVM.kt=%.1.9.jar) \
			$(SCRIPTS:%-Native.kt=%.1.9.kexe) \
			$(SCRIPTS:%-JVM.kt=%.2.0.jar) \
			$(SCRIPTS:%-Native.kt=%.2.0.kexe) \
			$(SCRIPTS:%-JVM.kt=%.2.1.jar) \
			$(SCRIPTS:%-Native.kt=%.2.1.kexe) \

%.jar: %-JVM.kt
	kotlinc -include-runtime -d $@ $<

%.1.9.jar: %-JVM.kt
	kotlinc-1.9 -include-runtime -d $@ $<

%.2.0.jar: %-JVM.kt
	kotlinc-2.0 -include-runtime -d $@ $<

%.2.1.jar: %-JVM.kt
	kotlinc-2.1 -include-runtime -d $@ $<

%.kexe: %-Native.kt
	kotlinc-native -opt-in=kotlin.time.ExperimentalTime -opt-in=kotlinx.cinterop.ExperimentalForeignApi -opt -linker-options -s -output $@ $<

%.1.9.kexe: %-Native.kt
	/opt/kotlin-1.9-native/bin/kotlinc-native -opt-in=kotlin.time.ExperimentalTime -opt-in=kotlinx.cinterop.ExperimentalForeignApi -opt -linker-options -s -output $@ $<

%.2.0.kexe: %-Native.kt
	/opt/kotlin-2.0-native/bin/kotlinc-native -opt-in=kotlin.time.ExperimentalTime -opt-in=kotlinx.cinterop.ExperimentalForeignApi -opt -linker-options -s -output $@ $<

%.2.1.kexe: %-Native.kt
	/opt/kotlin-native/bin/kotlinc-native -opt-in=kotlin.time.ExperimentalTime -opt-in=kotlinx.cinterop.ExperimentalForeignApi -opt -linker-options -s -output $@ $<

all: $(BINARIES)

.PHONY: clean
clean:
	rm -f $(BINARIES)
