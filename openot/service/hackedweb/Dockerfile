FROM ubuntu:latest

RUN apt update && apt install -y apache2

# Add a script to list directory contents
RUN mkdir /var/www/html/captures

# Copy index.html into the container
COPY index.html /var/www/html/

# Copy capture.py into the container
COPY capture.py /var/www/html/

# Run capture.py
ENTRYPOINT ["sh", "-c", "python /var/www/html/capture.py"]