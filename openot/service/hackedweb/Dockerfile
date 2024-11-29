FROM ubuntu:latest

RUN apt update && apt install -y apache2 python3 tcpdump   

# Add a script to list directory contents
RUN mkdir /var/www/html/captures

# Copy index.html into the container
COPY index.html /var/www/html/

# Copy capture.py into the container
COPY capture.py /var/www/html/

ENTRYPOINT service apache2 start && python3 /var/www/html/capture.py
RUN apt install git
RUN git clone https://github.com/pymodbus-dev/pymodbus
RUN cd pymodbus
RUN sudo python3 -m venv .venv
RUN source .venv/bin/actívate

RUN python3 HoldingRegisters.py


