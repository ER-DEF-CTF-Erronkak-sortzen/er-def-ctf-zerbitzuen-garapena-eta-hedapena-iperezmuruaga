#!/usr/bin/env python3

from ctf_gameserver import checkerlib
import logging
import http.client
import socket
import paramiko
import hashlib
#PORT_WEB = 9797
PORT_SSH = 8822
PORT_HACKEDWEB = 8889
PORT_OPENPLC = 8890
PORT_MODBUS = 502

def ssh_connect():
    def decorator(func):
        def wrapper(*args, **kwargs):
            # SSH connection setup
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            rsa_key = paramiko.RSAKey.from_private_key_file(f'/keys/team{args[0].team}-sshkey')
            client.connect(args[0].ip, username = 'root', pkey=rsa_key)

            # Call the decorated function with the client parameter
            args[0].client = client
            result = func(*args, **kwargs)

            # SSH connection cleanup
            client.close()
            return result
        return wrapper
    return decorator

class MyChecker(checkerlib.BaseChecker):

    def __init__(self, ip, team):
        checkerlib.BaseChecker.__init__(self, ip, team)
        self._baseurl = f'http://[{self.ip}]:{PORT_WEB}'
        logging.info(f"URL: {self._baseurl}")

    @ssh_connect()
    def place_flag(self, tick):
        flag = checkerlib.get_flag(tick)
        creds = self._add_new_flag(self.client, flag)
        if not creds:
            return checkerlib.CheckResult.FAULTY
        logging.info('created')
        checkerlib.store_state(str(tick), creds)
        checkerlib.set_flagid(str(tick))
        return checkerlib.CheckResult.OK

    def check_service(self):
        # check if ports are open
        if not self._check_port_web(self.ip, PORT_HACKEDWEB) or not self._check_port_ssh(self.ip, PORT_SSH) or not self._check_port_web(self.ip, PORT_OPENPLC) or not self._check_port_ssh(self.ip.PORT_MODBUS):
            return checkerlib.CheckResult.DOWN
        #else
        # check if server is Apache 2.4.50
        #if not self._check_apache_version():
            #return checkerlib.CheckResult.FAULTY
        
        #file_path_web = '/usr/local/apache2/htdocs/index.html'/var/www/html/
        file_path_web = '/var/www/html/index.html'
        # check if index.hmtl from openot_hackedweb has been changed by comparing its hash with the hash of the original file
        if not self._check_web_integrity(file_path_web):
            return checkerlib.CheckResult.FAULTY            
        file_path_ssh = '/etc/ssh/sshd_config'
        # check if /etc/sshd_config from openot_pasapasa_ssh has been changed by comparing its hash with the hash of the original file
        if not self._check_ssh_integrity(file_path_ssh):
            return checkerlib.CheckResult.FAULTY            
        return checkerlib.CheckResult.OK
    
    def check_flag(self, tick):
        if not self.check_service():
            return checkerlib.CheckResult.DOWN
        flag = checkerlib.get_flag(tick)
        #creds = checkerlib.load_state("flag_" + str(tick))
        # if not creds:
        #     logging.error(f"Cannot find creds for tick {tick}")
        #     return checkerlib.CheckResult.FLAG_NOT_FOUND
        flag_present = self._check_flag_present(flag)
        if not flag_present:
            return checkerlib.CheckResult.FLAG_NOT_FOUND
        return checkerlib.CheckResult.OK
                  
    @ssh_connect()
    def _check_web_integrity(self, path):
        ssh_session = self.client
        command = f"docker exec openot_hackedweb_1 sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False
        
        output = stdout.read().decode().strip()
        return hashlib.md5(output.encode()).hexdigest() == 'f4f79cccf2b936a9a04bbe8a82bc441a'
    
    @ssh_connect()
    def _check_ssh_integrity(self, path):
        ssh_session = self.client
        command = f"docker exec pasapasa_ssh_1 sh -c 'cat {path}'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False
        output = stdout.read().decode().strip()
        print (hashlib.md5(output.encode()).hexdigest())

        return hashlib.md5(output.encode()).hexdigest() == 'ba55c65e08e320f1225c76f810f1328b'
  
    # Private Funcs - Return False if error
    def _add_new_flag(self, ssh_session, flag):
        # Execute the file creation command in the container
        command = f"docker exec openot_ssh_1 sh -c 'echo {flag} >> /tmp/flag.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)

        # Check if the command executed successfully
        if stderr.channel.recv_exit_status() != 0:
            return False
        
        # Return the result
        return {'flag': flag}

    @ssh_connect()
    def _check_flag_present(self, flag):
        ssh_session = self.client
        command = f"docker exec openot_ssh_1 sh -c 'grep {flag} /tmp/flag.txt'"
        stdin, stdout, stderr = ssh_session.exec_command(command)
        if stderr.channel.recv_exit_status() != 0:
            return False

        #we check if the flag is the correct one
        output = stdout.read().decode().strip()
       
        return flag == output
    
    def _check_port_web(self, ip, port):
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5)
            conn.request("GET", "/")
            response = conn.getresponse()
            return response.status == 200
        except (http.client.HTTPException, socket.error) as e:
            print(f"Exception: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def _check_port_ssh(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            return result == 0
        except socket.error as e:
            print(f"Exception: {e}")
            return False
        finally:
            sock.close()

    @ssh_connect()
    def _check_apache_version(self):
        ssh_session = self.client
        command = f"docker exec openot_web_1 sh -c 'httpd -v | grep \"Apache/2.4.50\'"
        stdin, stdout, stderr = ssh_session.exec_command(command)

        if stdout:
            return True
        else:
            return False
  
if __name__ == '__main__':
    checkerlib.run_check(MyChecker)




