ARG BASE_IMAGE=ghcr.io/leon0399/benchmarks-base:latest
FROM $BASE_IMAGE

# OpenJDK
# OpenJDK
RUN mkdir openjdk-21 && \
    wget --progress=dot:giga -O - https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz \
    | tar -xz --strip-components=1 -C openjdk-21 \
 && mkdir openjdk-22 && \
    wget --progress=dot:giga -O - https://download.java.net/java/GA/jdk22.0.2/c9ecb94cd31b495da20a27d4581645e8/9/GPL/openjdk-22.0.2_linux-x64_bin.tar.gz \
    | tar -xz --strip-components=1 -C openjdk-22 \
 && mkdir openjdk-23 && \
    wget --progress=dot:giga -O - https://download.java.net/java/GA/jdk23.0.2/6da2a6609d6e406f85c491fcb119101b/7/GPL/openjdk-23.0.2_linux-x64_bin.tar.gz \
    | tar -xz --strip-components=1 -C openjdk-23 \
 && ln -s /opt/openjdk-21/bin/java /usr/bin/openjdk21.java && ln -s /opt/openjdk-21/bin/javac /usr/bin/openjdk21.javac && ln -s /opt/openjdk-21/bin/jar /usr/bin/openjdk21.jar \
 && ln -s /opt/openjdk-22/bin/java /usr/bin/openjdk22.java && ln -s /opt/openjdk-22/bin/javac /usr/bin/openjdk22.javac && ln -s /opt/openjdk-22/bin/jar /usr/bin/openjdk22.jar \
 && ln -s /opt/openjdk-23/bin/java /usr/bin/openjdk23.java && ln -s /opt/openjdk-23/bin/javac /usr/bin/openjdk23.javac && ln -s /opt/openjdk-23/bin/jar /usr/bin/openjdk23.jar

# Oracle JDK
RUN mkdir jdk-21 && \
    wget --progress=dot:giga -O - https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz \
    | tar -xz --directory jdk-21 --strip-components 1 \
 && mkdir jdk-23 && \
    wget --progress=dot:giga -O - https://download.oracle.com/java/23/latest/jdk-23_linux-x64_bin.tar.gz \
    | tar -xz --directory jdk-23 --strip-components 1 \
 && ln -s /opt/jdk-21/bin/java /usr/bin/oracle-jdk21.java && ln -s /opt/jdk-21/bin/javac /usr/bin/oracle-jdk21.javac && ln -s /opt/jdk-21/bin/jar /usr/bin/oracle-jdk21.jar \
 && ln -s /opt/jdk-23/bin/java /usr/bin/oracle-jdk23.java && ln -s /opt/jdk-23/bin/javac /usr/bin/oracle-jdk23.javac && ln -s /opt/jdk-23/bin/jar /usr/bin/oracle-jdk23.jar

# Mark latest version as primary
ENV PATH="/opt/jdk-23/bin:${PATH}"

# GraalVM
RUN mkdir graalvm-jdk-21 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/21/latest/graalvm-jdk-21_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-21 --strip-components 1 \
 && mkdir graalvm-jdk-23 && wget --progress=dot:giga -O - https://download.oracle.com/graalvm/23/latest/graalvm-jdk-23_linux-x64_bin.tar.gz | tar -xz --directory graalvm-jdk-23 --strip-components 1 \
 && ln -s /opt/graalvm-jdk-21/bin/java /usr/bin/oracle-graalvm21.java && ln -s /opt/graalvm-jdk-21/bin/javac /usr/bin/oracle-graalvm21.javac && ln -s /opt/graalvm-jdk-21/bin/jar /usr/bin/oracle-graalvm21.jar \
 && ln -s /opt/graalvm-jdk-23/bin/java /usr/bin/oracle-graalvm23.java && ln -s /opt/graalvm-jdk-23/bin/javac /usr/bin/oracle-graalvm23.javac && ln -s /opt/graalvm-jdk-23/bin/jar /usr/bin/oracle-graalvm23.jar \
 # Mark latest version as primary
 && ln -s /opt/graalvm-jdk-23/bin/java /usr/bin/oracle-graalvm.java && ln -s /opt/graalvm-jdk-23/bin/javac /usr/bin/oracle-graalvm.javac && ln -s /opt/graalvm-jdk-23/bin/jar /usr/bin/oracle-graalvm.jar \
 && ln -s /opt/graalvm-jdk-23/bin/java /usr/bin/graalvm.java && ln -s /opt/graalvm-jdk-23/bin/javac /usr/bin/graalvm.javac && ln -s /opt/graalvm-jdk-23/bin/jar /usr/bin/graalvm.jar

WORKDIR /app
