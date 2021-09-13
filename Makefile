LANGS = \
	c-plus-plus \
	java \
	rust \

.PHONY: all $(LANGS) clean

all: $(LANGS)

$(LANGS):
	$(MAKE) --directory ./$@

clean-%:
	$(MAKE) --directory ./$* clean

clean: $(LANGS:%=clean-%)