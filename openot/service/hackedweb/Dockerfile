FROM ubuntu:latest

RUN apt update && apt install -y apache2 python3 git python3-pip tcpdump # python3-venv

# Add a script to list directory contents
RUN mkdir /var/www/html/captures

# Copy index.html into the container
COPY index.html /var/www/html/

# Copy capture.py into the container
COPY capture.py /var/www/html/

WORKDIR /root

RUN git clone https://github.com/pymodbus-dev/pymodbus

WORKDIR /root/pymodbus

# RUN python3 -m venv .venv
# RUN source .venv/bin/activate
RUN pip install pymodbus

# Copy HoldingRegisters.py into the container

COPY HoldingRegisters.py /root/pymodbus/


# ENTRYPOINT service apache2 start && python3 /var/www/html/capture.py & python3 /root/pymodbus/HoldingRegisters.py
ENTRYPOINT tail -f /dev/null