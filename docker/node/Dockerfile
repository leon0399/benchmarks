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
 && nvm install 24 \
 && nvm install 25 \
 # Mark latest version as primary
 && nvm alias default 25 \
 && nvm use default

RUN --mount=type=cache,target=/var/cache/downloads \
    mkdir bun1.2 && wget --progress=dot:giga -O /var/cache/downloads/bun1.2.zip https://github.com/oven-sh/bun/releases/download/bun-v1.2.23/bun-linux-aarch64.zip && unzip /var/cache/downloads/bun1.2.zip -d bun1.2 \
 && mkdir bun1.3 && wget --progress=dot:giga -O /var/cache/downloads/bun1.3.zip https://github.com/oven-sh/bun/releases/download/bun-v1.3.1/bun-linux-aarch64.zip && unzip /var/cache/downloads/bun1.3.zip -d bun1.3 \
 && ln -s /opt/bun1.2/bun /usr/bin/bun1.2 \
 && ln -s /opt/bun1.3/bun /usr/bin/bun1.3 \
 # Mark latest version as primary
 && ln -s /opt/bun1.3/bun /usr/bin/bun

RUN --mount=type=cache,target=/var/cache/downloads \
    mkdir deno2.4 && wget --progress=dot:giga -O /var/cache/downloads/deno2.4.zip https://github.com/denoland/deno/releases/download/v2.4.5/deno-x86_64-unknown-linux-gnu.zip && unzip /var/cache/downloads/deno2.4.zip -d deno2.4 \
 && mkdir deno2.5 && wget --progress=dot:giga -O /var/cache/downloads/deno2.5.zip https://github.com/denoland/deno/releases/download/v2.5.4/deno-x86_64-unknown-linux-gnu.zip && unzip /var/cache/downloads/deno2.5.zip -d deno2.5 \
 && ln -s /opt/deno2.4/deno /usr/bin/deno2.4 \
 && ln -s /opt/deno2.5/deno /usr/bin/deno2.5 \
 # Mark latest version as primary
 && ln -s /opt/deno2.5/deno /usr/bin/deno

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
