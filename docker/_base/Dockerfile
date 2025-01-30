FROM debian:12.0-slim

LABEL org.opencontainers.image.source=https://github.com/leon0399/benchmarks

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
        # Common Tools
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
        software-properties-common \
        # Python Tools for running benchmarks scripts
        python3 \
        python3-pip \
        python3-full \
        python3-venv \
        python3-yaml \
        python3-numpy \
        python3-pandas \
        python3-psutil

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /opt