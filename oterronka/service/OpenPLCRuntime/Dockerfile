FROM ubuntu:latest
#Clonar el repositorio de OpenPLC:
RUN [ "executable" ]h git clone https://github.com/thiagoralves/OpenPLC_v3.git
RUN cd OpenPLC_v3
#Construir la imagen Docker:
RUN docker build -t OpenPLCRuntime .
#Ejecutar el contenedor Docker:
#RUN docker run --name OpenPLRuntime -d -p 8080:8080 -p 502:502 -v /home/isard/Descargas/ctf-gameserver-services/oterronka/service/OpenPLCRuntime/Scripts:/home/openplc/scripts OpenPLCRuntime







