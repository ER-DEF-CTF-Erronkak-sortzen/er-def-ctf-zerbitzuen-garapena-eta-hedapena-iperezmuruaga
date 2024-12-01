# Service definition:
- We have three dockers: 
1. HackedWeb An Ubuntu (latest version) one which contains pcap captures of OT communications. 
2. OpenPLC An debian:bullseye-20240722 one which has installed an OpenPLC Runtime service.
3. SSH An Ubuntu (latest version) one which permits tcmdump captures get achived in HackedWeb.

The attacker has access to a web page (Hacked Web) and has to look for information that can help him accessing the other docker.
The flags are trasmited as a concatenation in the OT communication registers and the attacker has to let them in his T-Submission machine. The flag is 2024113.

# Service implementation:
HackedWeb docker is configured to:
  - Start an apache service which saves OT communications.
  - Run in loop a OT communication client which connects to OpenPLC docker to read OT registers.

OpenPLC docker which is configured as an OT server for OT data register transmission in port 502 running the OpenPLCRuntime App. The data trasmitted is configured in OTErronka.st programm, developed with OpenPLCEditor in an external endpoint. The client of HackedWeb will be connected to this server in port 502.
In OpenPLCRuntime App the logging remember is disables in order to avoid participants viewing directly the registers and force them to analyze the information with Wireshark. In case of being needed, the login is: 
- user: openplc
- password: cybererronkaot

SSH docker which allows the .pcap sniffing between different dockers (HackedWeb and OpenPLC).

 
-Flags: 
    Flags will be stored in 'pasapasa_ssh_1' docker's '/tmp/flags.txt' file. 

# About exploting:

- The attacker has to inspect the index.html document in HackedWeb connecting for example to http://10.0.1.101:8889/. Inside, there is a clue. They should go to captures folder and download them to analyze with Wireshark. http://10.0.1.101:8889/captures.

- Once inside Wireshark, the attacker should go to a Modbus Response data and realize that in Register 1024, 1025 and 1026 is data inside. If the attacker concats the data, the attacker will discover a date. This is the flag.

- Defender should realize that there is a process running on port 502 that kill it. With this operation the defender will be killing the modbus client.

  
  #Attack performed by Team1 against Team 4. 
  #Inspect web page in 10.0.0.104
      #We find 'dev1/w3ar3h4ck3r2' credentials.
  #ssh -p 8822 dev1@10.0.0.104
        #Enter 'w3ar3h4ck3r2' as password
  #cat /tmp/flags.txt
     #Copy last flags
     #Exit
  #'ssh -i /home/urko/Deskargak/keyak/team2-sshkey root@10.0.1.1'
  #nano /root/xxx.flag
    #Paste copied flags. 

  #Defense performed by Team4
     #'ssh root@10.0.0.104'
     #docker exec -it pasapasa_ssh_1 /bin/bash
     #passwd dev1
     

# Checker checks:
- Ports to reach dockers are open (WEB:8889; SSH 8822; OPEPLC:8890)
- Port 502 is open in OpenPLC docker
- Port 502 is open in HackedWeb
- HoldingRegisters.py is not running in HackedWeb container


Checks done: 
- TEAM 0. Stop the container: 'root@team0-services:~# docker stop pasapasa_web_1' It works OK, service's status becomes DOWN. 
- TEAM 1. Stop the container: 'root@team0-services:~# docker stop pasapasa_ssh_1' It works OK, service's status becomes DOWN.
- TEAM 2. 'userdel dev1'. It works OK, service's status becomes faulty. 
- TEAM 3. Change '/etc/sshd_config' file from 'pasapasa_ssh' docker. It works OK, service's status becomes faulty.
- TEAM 4. Change '/usr/local/apache2/htdocs/index.html' file from 'pasapasa_web' docker. It works OK, service's status becomes faulty.
- TEAM 5. 'ssh service stop'. It works OK, service's status becomes faulty. 
- TEAM 0. apt update apache2
# License notes
Parts from:
https://github.com/kristianvld/SQL-Injection-Playground



