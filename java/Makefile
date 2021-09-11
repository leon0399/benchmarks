JC = javac
CLASSES = $(wildcard **/*.java)

%.class: %.java
	$(JC) $<

%.jar: %.class
	jar cfe $@ $* **/*.class

all: $(CLASSES:%.java=%.jar)

.PHONY: clean
clean:
	$(RM) **/*.class **/*.jar
