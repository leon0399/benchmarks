ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

ARG ZIG=0.12.0
RUN wget --progress=dot:giga -O - \
        https://ziglang.org/download/$ZIG/zig-linux-x86_64-$ZIG.tar.xz | tar -xJ
ENV PATH="/opt/zig-linux-x86_64-$ZIG:${PATH}"

WORKDIR /app