SCRIPTS = $(wildcard **/*.java)

%.class: %.java
	graalvm-javac $<

%.jar: %.class
	jar cfe $@ $* $**.class

all: $(SCRIPTS:%.java=%.jar)

.PHONY: clean
clean:
	$(RM) **/*.class **/*.jar
