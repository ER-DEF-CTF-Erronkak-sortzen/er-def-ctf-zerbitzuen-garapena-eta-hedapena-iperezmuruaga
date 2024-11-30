FROM ubuntu:latest

RUN apt update && apt install -y apache2 python3 tcpdump   

# Add a script to list directory contents
RUN mkdir /var/www/html/captures

# Copy index.html into the container
COPY index.html /var/www/html/

# Copy capture.py into the container
COPY capture.py /var/www/html/

# Copy HoldingRegisters.py into the container
COPY HoldingRegisters.py /home/ubuntu/pymodbus/venv/bin

RUN cd home/ubuntu
RUN apt install git -y
RUN git clone https://github.com/pymodbus-dev/pymodbus
RUN cd pymodbus
RUN apt install python3.12-venv -y

RUN cd /home/ubuntu/pymodbus/venv
RUN cd bin
RUN source /home/ubuntu/pymodbus/venv/bin/activate

# RUN python3 HoldingRegisters.py
#ENTRYPOINT ["/bin/bash", "-c", "source ./venv/bin/activate && exec bash"]

ENTRYPOINT service apache2 start && python3 /var/www/html/capture.py & python3 HoldingRegisters.py
