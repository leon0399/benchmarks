ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
 && dpkg -i packages-microsoft-prod.deb \
 && rm packages-microsoft-prod.deb \
 && apt update \
 && apt install -y \
        dotnet-sdk-8.0 aspnetcore-runtime-8.0 dotnet-runtime-8.0 mono-complete

WORKDIR /app
