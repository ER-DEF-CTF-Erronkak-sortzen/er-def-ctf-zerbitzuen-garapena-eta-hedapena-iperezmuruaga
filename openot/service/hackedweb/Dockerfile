FROM ubuntu:latest

RUN apt-get update && apt-get install -y apache2 && apt-get clean

# Copy capture.py into the container
COPY capture.py /usr/local/apache2/htdocs/

# Add a script to list directory contents
RUN echo '<html><body><h1>Directory </h1><ul>' > /var/www/html/index.html && \
    ls -1 /usr/local/apache2/htdocs | while read file; do echo "<li><a href=\"$file\">$file</a></li>"; done >> /var/www/htmlindex.html && \
    echo '</ul></body></html>' >> //var/www/html/index.html && \
    /etc/init.d/apache2 start

# Run capture.py
ENTRYPOINT ["sh", "-c", "python /usr/local/apache2/htdocs/capture.py"]