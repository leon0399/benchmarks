ARG IMAGE=debian:12.0-slim

FROM ${IMAGE}

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
        git \
        curl \
        wget \
	cmake \
        libc6 \
        unzip \
        gnulib \
        gnupg2 \
        tzdata \
        libc-bin \
        uuid-dev \
        libc6-dev \
        pkg-config \
        libicu-dev \
        libssl-dev \
        libxml2-dev \
        libedit-dev \
        libncurses5 \
        lsb-release \
        libyaml-dev \
        binutils-gold \
        libc-devtools \
        libncurses-dev \
        libpython3-dev \
        libsqlite3-dev \
        libc6-dev-i386 \
        build-essential \
        ca-certificates \
        libreadline-dev \
        apt-transport-https \
        libcurl4-openssl-dev \
        software-properties-common

WORKDIR /opt

# C++
RUN apt-get install -y \
        gcc \
        clang

# RUN git clone https://github.com/gsauthof/cgmemtime.git \
#     && make --dir cgmemtime \
#     && ln -s /opt/cgmemtime/cgmemtime /usr/bin/cgmemtime
#     # && cgmemtime --setup -g $(getent group $(id -g) | cut -d: -f1) --perm 775

# Python
RUN apt-get install -y \
        python3 \
        python3-pip \
        python3-full \
        python3-numpy \
        python3-pandas \
        python3-psutil \
        python3-yaml \
        python3-docker \
        pipx \
        python3-venv \
        python3-ipython
RUN pipx install numba && pipx install cython
ENV PATH="/root/.local/bin:${PATH}"

# PyPy
ARG PYPY=v7.3.15
RUN wget --progress=dot:giga -O - \
        https://downloads.python.org/pypy/pypy3.10-$PYPY-linux64.tar.bz2 | tar -xj \
    && ln -s /opt/pypy3.10-$PYPY-linux64/bin/pypy3 /usr/bin/pypy3
RUN wget --progress=dot:giga -O - \
        https://downloads.python.org/pypy/pypy2.7-$PYPY-linux64.tar.bz2 | tar -xj \
    && ln -s /opt/pypy2.7-$PYPY-linux64/bin/pypy /usr/bin/pypy2

# PHP
ARG PHP=8.3
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/sury-php.list \
    && wget -qO - https://packages.sury.org/php/apt.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y \
        php${PHP} \
        php${PHP}-dev \
    && pecl install openswoole

# JavaScript
ARG NODE=20.11.0
RUN wget --progress=dot:giga -O - \
        https://nodejs.org/dist/v$NODE/node-v$NODE-linux-x64.tar.xz | tar -xJ
ENV PATH="/opt/node-v$NODE-linux-x64/bin/:${PATH}"

# Java
ARG JDK=21.0.2
RUN wget --progress=dot:giga -O - \
        https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz | tar -xz
ENV PATH="/opt/jdk-${JDK}/bin:${PATH}"

# Go
ARG GO=1.22.0
RUN wget --progress=dot:giga -O - \
        https://golang.org/dl/go${GO}.linux-amd64.tar.gz | tar -xz
ENV PATH="/opt/go/bin/:${PATH}"

# Rust
ENV CARGO_HOME="/opt/.cargo"
RUN wget -O - https://sh.rustup.rs | sh -s -- -y
ENV PATH="/opt/.cargo/bin:${PATH}"

# Groovy
RUN apt-get install -y \
        groovy

# Kotlin
ARG KOTLIN=1.9.22
RUN wget --progress=dot:giga \
        https://github.com/JetBrains/kotlin/releases/download/v$KOTLIN/kotlin-compiler-$KOTLIN.zip \
	&& unzip kotlin-compiler-$KOTLIN.zip \
	&& rm kotlin-compiler-$KOTLIN.zip
ENV PATH="/opt/kotlinc/bin/:${PATH}"

RUN wget --progress=dot:giga -O - \
        https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN}/kotlin-native-linux-x86_64-${KOTLIN}.tar.gz | tar -xz \
    && ln -s /opt/kotlin-native-linux-x86_64-${KOTLIN}/bin/kotlinc-native /usr/bin/kotlinc-native \
    && ln -s /opt/kotlin-native-linux-x86_64-${KOTLIN}/bin/run_konan /usr/bin/run_konan

# Scala
ARG SCALA=3.3.1
RUN wget --progress=dot:giga -O - \
        https://github.com/lampepfl/dotty/releases/download/$SCALA/scala3-$SCALA.tar.gz | tar -xz
ENV PATH="/opt/scala3-$SCALA/bin/:${PATH}"

# Ruby
ARG RUBY=3.2.3
RUN wget --progress=dot:giga -O - \
        https://cache.ruby-lang.org/pub/ruby/${RUBY%.*}/ruby-${RUBY}.tar.gz | tar -xz \
	&& cd ruby-${RUBY} \
	&& ./configure --prefix=/opt/ruby && make -j && make install \
	&& cd .. && rm -rf ruby-${RUBY}
ENV PATH="/opt/ruby/bin:${PATH}"

# Ruby (JRuby)
ARG JRUBY=9.4.5.0
RUN wget --progress=dot:giga -O - \
        https://repo1.maven.org/maven2/org/jruby/jruby-dist/$JRUBY/jruby-dist-$JRUBY-bin.tar.gz | tar -xz
ENV PATH="/opt/jruby-${JRUBY}/bin:${PATH}"

# GraalVM
ARG GRAALVM=22.3.3
RUN wget --progress=dot:giga -O - \
        https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-$GRAALVM/graalvm-ce-java11-linux-amd64-$GRAALVM.tar.gz | tar -xz \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/gu /usr/bin/gu \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/js /usr/bin/graalvm.js \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/java /usr/bin/graalvm.java \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/javac /usr/bin/graalvm.javac

RUN gu available \
    && gu install \
        js \
        nodejs \
        llvm \
        llvm-toolchain \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/node /usr/bin/graalvm.node \
    && ln -s /opt/graalvm-ce-java11-${GRAALVM}/bin/lli /usr/bin/graalvm.lli \
    && export GRAALVM_LLVM_TOOLCHAIN=$(graalvm.lli --print-toolchain-path)

# Fortran
RUN apt-get install -y \
        gfortran

# Swift
ARG SWIFT=5.10.1
RUN wget --progress=dot:giga -O - \
        https://download.swift.org/swift-${SWIFT}-release/debian12/swift-${SWIFT}-RELEASE/swift-${SWIFT}-RELEASE-debian12.tar.gz | tar -xz
ENV PATH="/opt/swift-${SWIFT}-RELEASE-debian12/usr/bin:${PATH}"

# Lua
RUN apt-get install -y \
        lua5.4 \
        luajit

# C#
RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt update \
    && apt install -y \
        dotnet-sdk-8.0 aspnetcore-runtime-8.0 dotnet-runtime-8.0 mono-complete
        
# Zig
ARG ZIG=0.12.0
RUN wget --progress=dot:giga -O - \
        https://ziglang.org/download/$ZIG/zig-linux-x86_64-$ZIG.tar.xz | tar -xJ
ENV PATH="/opt/zig-linux-x86_64-$ZIG:${PATH}"

WORKDIR /app
