ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-java:latest
FROM $BASE_IMAGE

COPY --chmod=744 ./install-kotlin-v1.x ./install-kotlin-v2.x /usr/local/bin/ 

RUN install-kotlin-v1.x 1.9.25 /opt/kotlin-1.9 /opt/kotlin-1.9-native \
 && install-kotlin-v2.x 2.0.10 /opt/kotlin-2.0 /opt/kotlin-2.0-native \
 && install-kotlin-v2.x 2.1.10 /opt/kotlin /opt/kotlin-native \
 && ln -s /opt/kotlin-1.9/bin/kotlinc /usr/bin/kotlinc-1.9 \
 && ln -s /opt/kotlin-1.9-native/bin/kotlinc-native /usr/bin/kotlinc-1.9-native \
 && ln -s /opt/kotlin-2.0/bin/kotlinc /usr/bin/kotlinc-2.0 \
 && ln -s /opt/kotlin-2.0-native/bin/kotlinc-native /usr/bin/kotlinc-2.0-native \
 && ln -s /opt/kotlin/bin/kotlinc /usr/bin/kotlinc-2.1 \
 && ln -s /opt/kotlin-native/bin/kotlinc-native /usr/bin/kotlinc-2.1-native

# Mark latest version as default
ENV PATH="/opt/kotlinc/bin/:/opt/kotlin-native/bin/:${PATH}"

WORKDIR /app
