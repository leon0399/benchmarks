ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-java:latest
FROM $BASE_IMAGE

COPY --chmod=744 install-kotlin-v1.x.sh /usr/local/bin/install-kotlin-v1.x
COPY --chmod=744 install-kotlin-v2.x.sh /usr/local/bin/install-kotlin-v2.x

RUN install-kotlin-v1.x 1.9.25 /opt/kotlinc-1.9 /opt/kotlin-1.9-native \
 && install-kotlin-v2.x 2.0.10 /opt/kotlinc-2.0 /opt/kotlin-2.0-native \
 && install-kotlin-v2.x 2.1.10 /opt/kotlinc /opt/kotlin-native \
 && ln -s /opt/kotlinc-1.9/bin/kotlinc /opt/kotlinc/bin/kotlinc-1.9 \
 && ln -s /opt/kotlinc-1.9-native/bin/kotlinc-native /opt/kotlinc/bin/kotlinc-1.9-native \
 && ln -s /opt/kotlinc-2.0/bin/kotlinc /opt/kotlinc/bin/kotlinc-2.0 \
 && ln -s /opt/kotlinc-2.0-native/bin/kotlinc-native /opt/kotlinc/bin/kotlinc-2.0-native

# Mark latest version as default
ENV PATH="/opt/kotlinc/bin/:/opt/kotlin-native/bin/:${PATH}"

WORKDIR /app
