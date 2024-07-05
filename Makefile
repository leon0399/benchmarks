LANGS = \
    c \
	c-plus-plus \
	c-sharp \
	fortran \
	go \
	java \
	kotlin \
	rust \
	swift \
	zig \

.PHONY: all $(LANGS) clean

all: $(LANGS)

$(LANGS):
	$(MAKE) --directory ./$@

clean-%:
	$(MAKE) --directory ./$* clean

clean: $(LANGS:%=clean-%)