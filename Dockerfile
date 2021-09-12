ARG IMAGE=debian:11

FROM ${IMAGE}

RUN apt update \
    && apt install -y \
        curl \
        wget \
        gnupg2 \
        lsb-release \
        ca-certificates \
        apt-transport-https \
        software-properties-common

WORKDIR /opt

# Python
RUN apt install -y \
        python3 \
        python3-pip \
        python3-numpy \
    && pip install pyyaml docker psutil

# PHP
ARG PHP=8.0
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/sury-php.list \
    && wget -qO - https://packages.sury.org/php/apt.gpg | apt-key add - \
    && apt update \
    && apt install -y \
        php${PHP}

# JavaScript
ARG NODE=v16.9.0
RUN wget --progress=dot:giga -O - \
	https://nodejs.org/dist/$NODE/node-$NODE-linux-x64.tar.xz \
	| tar -xJ
ENV PATH="/opt/node-$NODE-linux-x64/bin/:${PATH}"

# Java
ARG JDK=16.0.2
RUN wget --progress=dot:giga -O - \
    https://download.java.net/java/GA/jdk16.0.2/d4a915d82b4c4fbb9bde534da945d746/7/GPL/openjdk-${JDK}_linux-x64_bin.tar.gz \
    | tar -xz
ENV PATH="/opt/jdk-${JDK}/bin:${PATH}"

# Go
ARG GO=1.17.1
RUN wget --progress=dot:giga -O - \
    https://golang.org/dl/go${GO}.linux-amd64.tar.gz \
    | tar -xz
ENV PATH="/opt/go/bin/:${PATH}"

WORKDIR /app