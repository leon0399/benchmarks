ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

RUN apt-get install -y \
        python3 \
        python3-pip \
        python3-full \
        python3-numpy \
        python3-pandas \
        python3-psutil \
        python3-yaml \
        python3-docker \
        pipx \
        python3-venv \
        python3-ipython \
    && pipx install numba \
    && pipx install cython
ENV PATH="/root/.local/bin:${PATH}"

# Different Python Versions
ENV PATH="/root/.pyenv/bin:${PATH}"
RUN curl -fsSL https://pyenv.run | bash \
    && echo 'eval "$(pyenv init --path)"' >> ~/.bashrc \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc \
    && pyenv install \ 
        3.6 \
        3.7 \
        3.8 \
        3.9 \
        3.10 \
        3.11 \
        3.12 \
        3.13

# PyPy
RUN wget --progress=dot:giga -O - https://downloads.python.org/pypy/pypy3.9-v7.3.16-linux64.tar.bz2 | tar -xj \
 && wget --progress=dot:giga -O - https://downloads.python.org/pypy/pypy3.10-v7.3.17-linux64.tar.bz2 | tar -xj \
 && ln -s /opt/pypy3.9-v7.3.16-linux64/bin/pypy3 /usr/bin/pypy3.9 \
 && ln -s /opt/pypy3.10-v7.3.17-linux64/bin/pypy3 /usr/bin/pypy3.10 \
 # Mark latest version as primary
 && ln -s /opt/pypy3.10-v7.3.17-linux64/bin/pypy3 /usr/bin/pypy3

WORKDIR /app
