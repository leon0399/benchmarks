ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

# Ruby
ARG RUBY=3.2.3
RUN wget --progress=dot:giga -O - \
        https://cache.ruby-lang.org/pub/ruby/${RUBY%.*}/ruby-${RUBY}.tar.gz | tar -xz \
	&& cd ruby-${RUBY} \
	&& ./configure --prefix=/opt/ruby \
    && make -j \
    && make install \
	&& cd .. \
    && rm -rf ruby-${RUBY}
ENV PATH="/opt/ruby/bin:${PATH}"

# Ruby (JRuby)
ARG JRUBY=9.4.5.0
RUN wget --progress=dot:giga -O - \
        https://repo1.maven.org/maven2/org/jruby/jruby-dist/$JRUBY/jruby-dist-$JRUBY-bin.tar.gz | tar -xz
ENV PATH="/opt/jruby-${JRUBY}/bin:${PATH}"

WORKDIR /app