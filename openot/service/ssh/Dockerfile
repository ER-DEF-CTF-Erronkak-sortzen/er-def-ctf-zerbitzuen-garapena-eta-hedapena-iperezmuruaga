# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Install OpenSSH server
RUN apt update && apt install -y openssh-server tcpdump

# Create the SSH directory and set up the root password
RUN mkdir /var/run/sshd && echo 'root:rootpassword' | chpasswd

# Allow root login via SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose the SSH port
EXPOSE 22

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]