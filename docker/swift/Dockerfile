ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

ARG SWIFT=5.10.1
RUN wget --progress=dot:giga -O - \
        https://download.swift.org/swift-${SWIFT}-release/debian12/swift-${SWIFT}-RELEASE/swift-${SWIFT}-RELEASE-debian12.tar.gz | tar -xz
ENV PATH="/opt/swift-${SWIFT}-RELEASE-debian12/usr/bin:${PATH}"

WORKDIR /app