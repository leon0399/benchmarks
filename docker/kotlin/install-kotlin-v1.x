#!/bin/bash

set -euxo pipefail

download_copiler() {
    local VERSION=$1
    local FILE=$2

    local URL="https://github.com/JetBrains/kotlin/releases/download/v${VERSION}/kotlin-compiler-${VERSION}.zip"

    wget --progress=dot:giga ${URL} -O ${FILE}
}

install_compiler() {
    local VERSION=$1
    local TARGET_PATH=$2 # e.g. /opt/kotlin or /usr/local/kotlin

    local FILE="kotlin-compiler-${VERSION}.zip"

    download_copiler ${VERSION} ${FILE}
    unzip -q ${FILE} -d /tmp/kotlin-compiler-${VERSION}
    rm ${FILE}

    mkdir -p ${TARGET_PATH}
    mv /tmp/kotlin-compiler-${VERSION}/kotlinc/* ${TARGET_PATH}
}

install_native() {
    local VERSION=$1
    local TARGET_PATH=$2 # e.g. /opt/kotlin-native or /usr/local/kotlin-native

    local URL="https://github.com/JetBrains/kotlin/releases/download/v${VERSION}/kotlin-native-linux-x86_64-${VERSION}.tar.gz"

    mkdir -p ${TARGET_PATH}
    wget --progress=dot:giga -O - ${URL} | tar -xz --strip-components=1 --directory=${TARGET_PATH}
}

install_compiler $1 $2
install_native $1 $3