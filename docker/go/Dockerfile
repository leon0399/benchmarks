ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

RUN mkdir go1.21 && wget --progress=dot:giga -O - https://golang.org/dl/go1.21.13.linux-amd64.tar.gz | tar -xz --directory go1.21 --strip-components 1 \
 && mkdir go1.22 && wget --progress=dot:giga -O - https://golang.org/dl/go1.22.11.linux-amd64.tar.gz | tar -xz --directory go1.22 --strip-components 1 \
 && mkdir go1.23 && wget --progress=dot:giga -O - https://golang.org/dl/go1.23.5.linux-amd64.tar.gz | tar -xz --directory go1.23 --strip-components 1 \
 && ln -s /opt/go1.21/bin/go /usr/bin/go1.21 \
 && ln -s /opt/go1.22/bin/go /usr/bin/go1.22 \
 && ln -s /opt/go1.23/bin/go /usr/bin/go1.23

# Mark latest version as primary
ENV PATH="/opt/go1.23/bin/:${PATH}"