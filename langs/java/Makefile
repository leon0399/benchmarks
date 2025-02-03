# Collect all .java files recursively
SCRIPTS := $(wildcard **/*.java)

# Define each JVM flavor you want to build with
FLAVORS := openjdk21 openjdk22 openjdk23 oracle-jdk21 oracle-jdk23 oracle-graalvm21 oracle-graalvm23

# The default `all` target builds a .jar for EACH compiler flavor
all: $(foreach flavor,$(FLAVORS),$(SCRIPTS:%.java=%.$(flavor).jar)) $(SCRIPTS:%.java=%.jar)


# ---------------------------------------------------------------------------
# Pattern rules for each flavor
# 
# 1) Compile .java => .class in a separate "classes/<flavor>" folder
# 2) Jar up into MyScript.<flavor>.jar, with the main class = MyScript

%.jar: %.java
	mkdir -p classes/java && \
	javac -d classes/java $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	jar cfe $@ $$MAIN_CLASS -C classes/java .

%.openjdk21.jar: %.java
	mkdir -p classes/openjdk21 && \
	openjdk21.javac -d classes/openjdk21 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	openjdk21.jar cfe $@ $$MAIN_CLASS -C classes/openjdk21 .

%.openjdk22.jar: %.java
	mkdir -p classes/openjdk22 && \
	openjdk22.javac -d classes/openjdk22 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	openjdk22.jar cfe $@ $$MAIN_CLASS -C classes/openjdk22 .

%.openjdk23.jar: %.java
	mkdir -p classes/openjdk23 && \
	openjdk23.javac -d classes/openjdk23 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	openjdk23.jar cfe $@ $$MAIN_CLASS -C classes/openjdk23 .

%.oracle-jdk21.jar: %.java
	mkdir -p classes/oracle-jdk21 && \
	oracle-jdk21.javac -d classes/oracle-jdk21 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	oracle-jdk21.jar cfe $@ $$MAIN_CLASS -C classes/oracle-jdk21 .

%.oracle-jdk23.jar: %.java
	mkdir -p classes/oracle-jdk23 && \
	oracle-jdk23.javac -d classes/oracle-jdk23 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	oracle-jdk23.jar cfe $@ $$MAIN_CLASS -C classes/oracle-jdk23 .

%.oracle-graalvm21.jar: %.java
	mkdir -p classes/oracle-graalvm21 && \
	oracle-graalvm21.javac -d classes/oracle-graalvm21 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	oracle-graalvm21.jar cfe $@ $$MAIN_CLASS -C classes/oracle-graalvm21 .

%.oracle-graalvm23.jar: %.java
	mkdir -p classes/oracle-graalvm23 && \
	oracle-graalvm23.javac -d classes/oracle-graalvm23 $< && \
	MAIN_CLASS=$(shell echo "$<" | sed 's/\.java$$//' | sed 's/\//\./g'); \
	oracle-graalvm23.jar cfe $@ $$MAIN_CLASS -C classes/oracle-graalvm23 .

# ---------------------------------------------------------------------------
# Cleanup
.PHONY: clean
clean:
	rm -rf classes
	rm -f **/*.jar
