SCRIPTS = $(wildcard **/*.java)

%.class: %.java
	javac $<

%.jar: %.class
	jar cfe $@ $* $**.class

all: $(SCRIPTS:%.java=%.jar)

.PHONY: clean
clean:
	$(RM) **/*.class **/*.jar
