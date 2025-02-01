ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

ENV CARGO_HOME="/opt/.cargo"
RUN wget -O - https://sh.rustup.rs | sh -s -- -y
ENV PATH="/opt/.cargo/bin:${PATH}"

WORKDIR /app
