ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

# JDK
RUN mkdir jdk-21 && wget --progress=dot:giga -O - https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz | tar -xz --directory jdk-21 --strip-components 1 \
 && mkdir jdk-23 && wget --progress=dot:giga -O - https://download.oracle.com/java/23/latest/jdk-23_linux-x64_bin.tar.gz | tar -xz --directory jdk-23 --strip-components 1 \
 && ln -s /opt/jdk-21/bin/java /usr/bin/java21 \
 && ln -s /opt/jdk-23/bin/java /usr/bin/java23

# Mark latest version as primary
ENV PATH="/opt/jdk-23/bin:${PATH}"

# GraalVM
RUN mkdir graalvm-jdk-21 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-21 --strip-components 1 \
 && mkdir graalvm-jdk-23 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/23/latest/graalvm-jdk-23_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-23 --strip-components 1 \
 && ln -s /opt/graalvm-jdk-21/bin/java /usr/bin/graalvm21.java \
 && ln -s /opt/graalvm-jdk-23/bin/java /usr/bin/graalvm23.java \
 # Mark latest version as primary
 && ln -s /opt/graalvm-jdk-23/bin/java /usr/bin/graalvm.java 

WORKDIR /app