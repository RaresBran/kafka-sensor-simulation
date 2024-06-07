FROM storm:2.6.2

# Install OpenJDK 21
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk && \
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-21-openjdk-amd64
