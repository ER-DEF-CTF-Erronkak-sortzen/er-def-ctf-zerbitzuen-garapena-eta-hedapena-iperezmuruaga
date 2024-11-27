FROM httpd:2.4.50

# Add a script to list directory contents
RUN echo '<html><body><h1>Directory </h1><ul>' > /usr/local/apache2/htdocs/index.html && \
    ls -1 /usr/local/apache2/htdocs | while read file; do echo "<li><a href=\"$file\">$file</a></li>"; done >> /usr/local/apache2/htdocs/index.html && \
    echo '</ul></body></html>' >> /usr/local/apache2/htdocs/index.html