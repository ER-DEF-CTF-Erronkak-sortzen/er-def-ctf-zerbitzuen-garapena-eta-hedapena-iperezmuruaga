FROM ubuntu:latest
RUN sudo apt install python3.10-venv
RUN python3 -m venv /home/isard/Descargas/ctf-gameserver-services/oterronka/service/PLCBezeroa/VirtualPath
RUN source .venv/bin/activate
RUN get checkout master

RUN git clone git://github.com/pymodbus-dev/pymodbus.git
RUN cd pymodbus
RUN sudo pip3 install -r requirements.txt

RUN python3 bezeroa.py
RUN docker build -t PLCBezeroa
# Ejecutar el contenedor Docker
#RUN docker run --rm PLCBezeroa






