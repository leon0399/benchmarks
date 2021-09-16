LANGS = \
	c-plus-plus \
	go \
	java \
	kotlin \
	rust \

.PHONY: all $(LANGS) clean

all: $(LANGS)

$(LANGS):
	$(MAKE) --directory ./$@

clean-%:
	$(MAKE) --directory ./$* clean

clean: $(LANGS:%=clean-%)