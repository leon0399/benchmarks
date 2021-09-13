ARG IMAGE=debian:11

FROM ${IMAGE}

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y \
        curl \
        wget \
        unzip \
        gnupg2 \
        libssl-dev \
        lsb-release \
        ca-certificates \
        apt-transport-https \
        software-properties-common

WORKDIR /opt

# Python
RUN apt install -y \
        python3 \
        python3-pip \
        python3-numpy \
    && pip install pyyaml docker psutil

# PHP
ARG PHP=8.0
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/sury-php.list \
    && wget -qO - https://packages.sury.org/php/apt.gpg | apt-key add - \
    && apt update \
    && apt install -y \
        php${PHP}

# JavaScript
ARG NODE=16.9.0
RUN wget --progress=dot:giga -O - \
	    https://nodejs.org/dist/v$NODE/node-v$NODE-linux-x64.tar.xz | tar -xJ
ENV PATH="/opt/node-v$NODE-linux-x64/bin/:${PATH}"

# Java
ARG JDK=16.0.2
RUN wget --progress=dot:giga -O - \
        https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-${JDK}_linux-x64_bin.tar.gz | tar -xz
ENV PATH="/opt/jdk-${JDK}/bin:${PATH}"

# Go
ARG GO=1.17.1
RUN wget --progress=dot:giga -O - \
        https://golang.org/dl/go${GO}.linux-amd64.tar.gz | tar -xz
ENV PATH="/opt/go/bin/:${PATH}"

# C++
RUN apt install -y \
        gcc \
        clang

# Rust
ENV CARGO_HOME="/opt/.cargo"
RUN wget -O - https://sh.rustup.rs | sh -s -- -y
ENV PATH="/opt/.cargo/bin:${PATH}"

# Groovy
RUN apt install -y \
        groovy

# Kotlin
ARG KOTLIN=1.5.30
RUN wget --progress=dot:giga \
	    https://github.com/JetBrains/kotlin/releases/download/v$KOTLIN/kotlin-compiler-$KOTLIN.zip \
	&& unzip kotlin-compiler-$KOTLIN.zip \
	&& rm kotlin-compiler-$KOTLIN.zip
ENV PATH="/opt/kotlinc/bin/:${PATH}"

# Scala
ARG SCALA=3.0.2
RUN wget --progress=dot:giga -O - \
        https://github.com/lampepfl/dotty/releases/download/$SCALA/scala3-$SCALA.tar.gz | tar -xz
ENV PATH="/opt/scala3-$SCALA/bin/:${PATH}"

# Ruby
ARG RUBY=3.0.2
RUN wget --progress=dot:giga -O - \
	    https://cache.ruby-lang.org/pub/ruby/3.0/ruby-${RUBY}.tar.gz | tar -xz \
	&& cd ruby-${RUBY} \
	&& ./configure --prefix=/opt/ruby && make -j && make install \
	&& cd .. && rm -rf ruby-${RUBY}
ENV PATH="/opt/ruby/bin:${PATH}"

# Ruby (JRuby)
ARG JRUBY=9.2.19.0
RUN wget --progress=dot:giga -O - \
	    https://repo1.maven.org/maven2/org/jruby/jruby-dist/$JRUBY/jruby-dist-$JRUBY-bin.tar.gz | tar -xz \
    && ln -s /opt/jruby-${JRUBY}/bin/jruby /usr/bin/jruby

# Graalvm
ARG GRAALVM=21.2.0
RUN wget --progress=dot:giga -O - \
	    https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-$GRAALVM/graalvm-ce-java11-linux-amd64-$GRAALVM.tar.gz | tar -xz \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/gu /usr/bin/gu \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/ruby /usr/bin/graalvm-ruby \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/java /usr/bin/graalvm-java

# Truffle
RUN gu install ruby \
	&& /opt/graalvm-ce-java11-${GRAALVM}/languages/ruby/lib/truffle/post_install_hook.sh \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/truffleruby /usr/bin/truffleruby

WORKDIR /app
