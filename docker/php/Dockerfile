ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/sury-php.list \
    && wget -qO - https://packages.sury.org/php/apt.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y \
        php5.6 \
        php7.0 \
        php7.1 \
        php7.2 \
        php7.3 \
        php7.4 \
        php8.0 \
        php8.1 \
        php8.2 \
        php8.3 \
        php8.4

WORKDIR /app
