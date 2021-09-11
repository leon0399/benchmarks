JC = javac
SCRIPTS = $(wildcard **/*.java)

%.class: %.java
	$(JC) $<

%.jar: %.class
	jar cfe $@ $* **/*.class

all: $(SCRIPTS:%.java=%.jar)

.PHONY: clean
clean:
	$(RM) **/*.class **/*.jar
