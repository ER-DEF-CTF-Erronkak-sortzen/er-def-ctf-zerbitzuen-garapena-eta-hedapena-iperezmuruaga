FROM debian:bullseye-20240722

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /workdir

# Download and install OpenPLC
RUN wget https://github.com/thiagoralves/OpenPLC_v3/archive/refs/heads/master.zip -O openplc.zip \
    && unzip openplc.zip \
    && rm openplc.zip \
    && mv OpenPLC_v3-master/* . \
    && rm -r OpenPLC_v3-master \
    && ./install.sh docker

# Expose the port OpenPLC runs on
EXPOSE 8080

ENTRYPOINT ["./start_openplc.sh"]

# ENTRYPOINT ["tail", "-f", "/dev/null"]