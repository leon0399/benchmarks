ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

ARG NVM_VERSION=0.40.1

ENV NVM_DIR=/usr/local/nvm
RUN mkdir $NVM_DIR \
 && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v${NVM_VERSION}/install.sh | bash \
 && . $NVM_DIR/nvm.sh \
 && nvm install 16 \
 && nvm install 17 \
 && nvm install 18 \
 && nvm install 19 \
 && nvm install 20 \
 && nvm install 21 \
 && nvm install 22 \
 && nvm install 23 \
 # Mark latest version as primary
 && nvm alias default 23 \
 && nvm use default

# GraalVM
# RUN mkdir graalvm-jdk-21 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-21 --strip-components 1 \
#  && mkdir graalvm-jdk-23 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/23/latest/graalvm-jdk-23_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-23 --strip-components 1 \
#  && ln -s /opt/graalvm-jdk-21/bin/gu /usr/bin/graalvm21.gu \
#  && ln -s /opt/graalvm-jdk-23/bin/gu /usr/bin/graalvm23.gu \
#  && graalvm21.gu install js nodejs \
#  && graalvm23.gu install js nodejs \
#  && ln -s /opt/graalvm-jdk-21/bin/node /usr/bin/graalvm21.node \
#  && ln -s /opt/graalvm-jdk-23/bin/node /usr/bin/graalvm23.node \
#  # Mark latest version as primary
#  && ln -s /opt/graalvm-jdk-23/bin/node /usr/bin/graalvm.node

WORKDIR /app
