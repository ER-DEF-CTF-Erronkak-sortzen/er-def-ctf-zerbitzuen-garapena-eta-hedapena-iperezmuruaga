FROM ubuntu:latest

# Instalar las dependencias
RUN sudo apt-get update && sudo apt-get install -y \
    xvfb \
    chromium-browser \
    && rm -rf /var/lib/apt/lists/*

# Crear un script para iniciar el navegador
RUN echo '#!/bin/bash\n' \
    'export DISPLAY=:99\n' \
    'Xvfb :99 -screen 0 1024x768x16 &\n' \
    'chromium-browser --no-sandbox --disable-gpu "$@"\n' \
    > /usr/local/bin/start-browser && chmod +x /usr/local/bin/start-browser

# Comando para abrir una URL específica
CMD ["start-browser", "http://localhost:8080"]
# Construir la imagen Docker
RUN docker build -t OpenPLCWebBrowser
# Ejecutar el contenedor Docker
#RUN docker run --rm OpenPLCWebBrowser





