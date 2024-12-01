FROM ubuntu:latest

RUN apt update && apt install -y apache2 python3 tcpdump   

# Add a script to list directory contents
RUN mkdir /var/www/html/captures

# Copy index.html into the container
COPY index.html /var/www/html/

# Copy capture.py into the container
COPY capture.py /var/www/html/

RUN cd /home/ubuntu
RUN apt install git -y
RUN git clone https://github.com/pymodbus-dev/pymodbus
RUN cd pymodbus
RUN apt install python3.12-venv -y

# Copy HoldingRegisters.py into the container
#COPY HoldingRegisters.py /home/ubuntu/


ENTRYPOINT service apache2 start && python3 /var/www/html/capture.py && python3 /home/ubuntu/pymodbus/HoldingRegisters.py
