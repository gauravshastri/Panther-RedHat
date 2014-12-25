#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *

def main_server_config():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'SERVER SIDE SOFTWARE CONFIGURATION' --menu  'Which Server Do you want to Configure?' 25 60 15 1 'Telnet' 2 'FTP' 3 'SSH' 4 'Apache' 5 'Mail' 6 'NIS' 7 'NFS' 8 'Samba' 9 'NIS+NFS' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			os.system("setenforce 0")
			os.system("iptables -F")
			if ch=="":
				break
			elif int(ch)==1:
				telnet_conf()
			elif int(ch)==2:
				ftp_conf()
			elif int(ch)==3:
				ssh_conf()
			elif int(ch)==4:
				web_conf()
			elif int(ch)==5:
				mail_conf()
			elif int(ch)==6:
				nis_conf()
			elif int(ch)==7:
				nfs_conf()
			elif int(ch)==8:
				samba_conf()
			elif int(ch)==9:
				nisnfs_conf()
			else:
				pass
		except:
			error()
			pass
	

def repl(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def nisnfs_conf():
	try:
		infobox("NIS+NFS SERVER CONFIGURATION","******Welcome User!!******","25","30")
		os.system("touch confiles/config")
		inputbox("Enter name of Directory in which user data will be saved:- ","15","60","confiles/config")
		fhdir=open("confiles/config", "r")
		direc=fhdir.read().strip()
		fhdir.close()
		os.system("mkdir /"+direc)
		msgbox("Enter name of Users for which you want to setup NFS service","15","50")		
		inputbox("Enter No. of users ","15","60","confiles/config")
		fhcnt=open("confiles/config", "r")
		cnt=int(fhcnt.read())
		fhcnt.close()
		for i in range(cnt):
			i=i+1
			inputbox("Enter user "+str(i),"15","60","confiles/config")
			fhusr=open("confiles/config", "r")
			user=fhusr.read().strip()
			fhusr.close()
			os.system("mkdir /"+direc+"/"+user)
			os.system("cp -rf /etc/skel /"+direc+"/"+user) 
		install("nfs-utils")
		os.system("setenforce 0; iptables -F")
		os.system("chmod o+w /"+direc+"/ -R")
		os.system("echo  '/'"+direc+" '*(sync,rw)' >> /etc/exports")		
		restart("nfs")	
	except:
		error()
		pass

def samba_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'SAMBA SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Share your Directory to all ' 2 'Share directory with a user' 3 'Allow only certain No.of IPs' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			os.system("setenforce 0")
			os.system("iptables -F")
			if ch=="":
				break
			elif int(ch)==1:
				infobox("Instructions","Choose a Directory now ","15","60")
				dirbox("/","confiles/config")
				fhdir=open("confiles/config", "r")
				direc=fhdir.read().strip()
				fhdir.close()
				os.system("chmod 777 "+direc)
				inputbox("Give a short Section Name to your Directory:- ","15","60","confiles/config")
				fhdir=open("confiles/config", "r")
				secname=fhdir.read().strip()
				fhdir.close()
				os.system("echo '['"+secname+"']' >> /etc/samba/smb.conf ")
				os.system("echo 'path = '"+direc+" >> /etc/samba/smb.conf ")
				os.system("echo 'public = yes'  >> /etc/samba/smb.conf ")
				os.system("echo 'writeable = yes'  >> /etc/samba/smb.conf ")
				restart("smb")
			elif int(ch)==2:
				infobox("Instructions","Choose a Directory now ","15","60")
				dirbox("/","confiles/config")
				direc=fhdir.read().strip()
				fhdir.close()
				os.system("chmod 777 "+direc)
				inputbox("Give a short Section Name to your Directory:- ","15","60","confiles/config")
				fhdir=open("confiles/config", "r")
				secname=fhdir.read().strip()
				fhdir.close()
				inputbox("Enter name of the User:- ","15","60","confiles/config")
				fhusr=open("confiles/config", "r")
				user=fhusr.read().strip()
				fhusr.close()
				os.system("useradd "+user+" &>/dev/null")
				yesnobox("Do you want a password based Security??","15","50","confiles/config")
				fhyes=open("confiles/config", "r")
				status=fhyes.read().strip()
				fhyes.close()
				if status=="0":
					os.system("echo '['"+secname+"']' >> /etc/samba/smb.conf ")
					os.system("echo 'path = '"+direc+" >> /etc/samba/smb.conf ")
					os.system("echo 'public = no'  >> /etc/samba/smb.conf ")
					os.system("echo 'writeable = yes'  >> /etc/samba/smb.conf ")
					os.system("echo 'valid users = '"+user+"  >> /etc/samba/smb.conf ")
					os.system("smbpasswd -a "+user )
				else: 
					os.system("echo '['"+secname+"']' >> /etc/samba/smb.conf ")
					os.system("echo 'path = '"+direc+" >> /etc/samba/smb.conf ")
					os.system("echo 'public = no'  >> /etc/samba/smb.conf ")
					os.system("echo 'writeable = yes'  >> /etc/samba/smb.conf ")
					os.system("echo 'valid users = '"+user+"  >> /etc/samba/smb.conf ")
				restart("smb")
			elif int(ch)==3:
				inputbox("Enter No. of IPs to only Allow them ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				os.system("cat '' > confiles/iplist")
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					os.system("echo -n ' '"+ip+"' ' >> confiles/iplist") 
				fhip=open("confiles/iplist", "r")
				ips=fhip.read().strip()
				fhip.close()
				os.system("`sed -i '80s/.*hosts allow.*/        hosts allow = "+ips+"/' /etc/samba/smb.conf`")
				restart("smb")
			else:
				pass
		except:
			error()
			pass

def nfs_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'NFS SERVER CONFIGURATION' --menu 'Select Your Choice:-' 35 100 5 1 'Share your Directory on many IPs' 2 'Give access to all IPs on the web ' 3 'Change Permission to (read & write) for a particular shared directory for a particular IP' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			os.system("setenforce 0")
			os.system("iptables -F")
			if ch=="":
				break
			elif int(ch)==1:
				infobox("Instructions","Choose a Directory now ","15","50")
				dirbox("/","confiles/config")
				fhdir=open("confiles/config", "r")
				direc=fhdir.read().strip()
				fhdir.close()
				os.system("chmod 777 "+direc) 
				inputbox("With how many IPs do you want to share?? :- ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					os.system("echo  "+direc+" "+ip+"'(sync)' >> /etc/exports") 
				restart("nfs")
			elif int(ch)==2:
				infobox("Instructions","Choose a Directory now ","15","60")
				dirbox("/","confiles/config")
				fhdir=open("confiles/config", "r")
				direc=fhdir.read().strip()
				fhdir.close()
				os.system("chmod 777 "+direc) 
				os.system("echo  "+direc+" *'(sync)' >> /etc/exports")
				restart("nfs")
			elif int(ch)==3:
				infobox("Instructions","Choose a Directory now ","15","60")
				dirbox("/","confiles/config")
				fhdir=open("confiles/config", "r")
				direc=fhdir.read().strip()
				fhdir.close()
				os.system("chmod 777 "+direc) 
				inputbox("For how many IPs do you want to change permission to read and write?? :- ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					str1=direc+" "+ip+"(sync)"
					str2=direc+" "+ip+"(sync,rw)"
					repl("/etc/exports",str1,str2)
				restart("nfs")		
			else:
				pass
		except:
			error()
			pass

def nis_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'NIS SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Set DomainName of NIS server ' 2 'Add User Accounts' 3 'Update NIS Database' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch)==1:
				inputbox("Enter Domain Name ","15","60","confiles/config")
				fhydn=open("confiles/config", "r")
				ydn=fhydn.read().strip()
				fhydn.close()
				os.system("ypdomainname "+ydn)
				restart("ypserv")	
			elif int(ch)==2:
				inputbox("Enter No. of users to Add them ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				for i in range(cnt):
					i=i+1
					inputbox("Enter user "+str(i),"15","60","confiles/config")
					fhusr=open("confiles/config", "r")
					user=fhusr.read().strip()
					fhusr.close()
					os.system("useradd "+user) 
				os.system("cd /var/yp/ ; make ")
				restart("ypserv")				
			elif int(ch)==3:
				os.system("cd /var/yp/ ; make ")
				restart("ypserv")		
			else:
				pass
		except:
			error()
			pass

def web_conf():
	p=1 
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'WEB SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Enter your html code for testing' 2 'Name based Virtual Hosting' 3 'Serve Web pages to All' 4 'Serve Web Pages to certain no.of IPs' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch) == 1:
				inputbox("Enter your HTML Code here","15","50","/var/www/html/index.html")
				os.system("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' &> confiles/config ")#hostname -I
				fhip=open("confiles/config","r")
				ip1=fhip.read()
				ip=ip1.strip()
				fhip.close()
				os.system("firefox "+`ip`+" & sleep 5; pkill firefox")
				msgbox("Your website is now running at IP:- "+ip,"15","50")
			elif int(ch)==2:
				os.system("iptables -F; setenforce 0")
				restart("httpd")
				os.system("hostname -I &> confiles/config ")
				fhip=open("confiles/config","r")
				ip=fhip.read().strip()
				fhip.close()
				os.system(" `sed -i 's/NameVirtualHost.*/NameVirtualHost "+ip+":80/g' /etc/httpd/conf/httpd.conf` ")
				os.system(" `sed -i 's/#NameVirtualHost.*/NameVirtualHost "+ip+":80/g' /etc/httpd/conf/httpd.conf` ")
				inputbox("How many websites do you want to host on IP "+ip+" virtually?","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				for i in range(cnt):
					i=i+1
					inputbox("Enter Website Name ","15","60","confiles/config")
					fhweb=open("confiles/config", "r")
					web=fhweb.read().strip()
					fhweb.close()
					#os.system("rm -rf /var/www/"+web+"/ &> /dev/null") 
					#infobox("hi","","25","50")
					os.system("mkdir /var/www/"+web+'/'" &> /dev/null")
					os.system("`cp index.html /var/www/"+web+"/`")
					#os.system("echo 'WELCOME TO MY ARENA' >> /var/www/"+web+"/index.html")
					#os.system("sed -i 's/''/WELCOME TO '"+web+"'/g' /var/www/"+web+"/index.html") 
					os.system("echo '<'VirtualHost "+web+"'>' >> /etc/httpd/conf/httpd.conf") 
					os.system("echo '	DocumentRoot /var/www/'"+web+" >> /etc/httpd/conf/httpd.conf")
					os.system("echo '	ServerName '"+ip+" >> /etc/httpd/conf/httpd.conf") 
					os.system("echo '<'/VirtualHost'>' >> /etc/httpd/conf/httpd.conf")
					os.system("echo  "+ip+" "+web+" >> /etc/hosts")
					restart("httpd")
					os.system("firefox "+`web`+" & sleep 5; pkill firefox")
					msgbox("Your website "+web+" is now running at IP:- "+ip,"15","50")
			elif int(ch)==3:
				os.system("`sed -i '344s/Allow from.*/Allow from all/' /etc/httpd/conf/httpd.conf`")
				restart("httpd")			
			elif int(ch)==4:
				inputbox("Enter No. of IPs to only Allow them ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				os.system("cat '' *> confiles/iplist")
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					os.system("echo -n ' '"+ip+"' ' >> confiles/iplist") 
				fhip=open("confiles/iplist", "r")
				ips=fhip.read().strip()
				fhip.close()
				os.system("`sed -i '344s/.*Allow from.*/    Allow from "+ips+"/' /etc/httpd/conf/httpd.conf`")
				restart("httpd")	
			else:
				pass
		except:
			error()
			pass

def telnet_conf():
	p=1
	progressbar("25","30")
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'TELNET SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Allow Telnet only from certain no. of IPs' 2 'Restrict Some IPs' 3 'Allow Root Login from Telnet' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch) == 1:
				inputbox("Enter No. of IPs","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				os.system("echo -n 'only_from = ' >> /etc/xinetd.conf") 
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP Address "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					os.system("echo -n "+ip+"' ' >> /etc/xinetd.conf") 
				restart("xinetd")
			elif int(ch)==2:
				inputbox("Enter No. of IPs","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				os.system("echo -n 'no_access = ' >> /etc/xinetd.conf") 
				for i in range(cnt):
					i=i+1
					inputbox("Enter IP Address "+str(i),"15","60","confiles/config")
					fhip=open("confiles/config", "r")
					ip=fhip.read().strip()
					fhip.close()
					os.system("echo -n "+ip+"' ' >> /etc/xinetd.conf") 
				restart("xinetd")
			elif int(ch)==3:
				inputbox("Enter No. of Telnet Sessions as root that you want:-","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				if cnt<=15:
					for i in range(cnt):
						os.system("echo pts/"+str(i)+" >> /etc/securetty") 
					restart("xinetd")
				else:
					msgbox("Maximum Root Sessions Limit reached..Please enter a number less than or equal to 15","15","60")
			else:
				pass
		except:
			error()
			pass


def ftp_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'FTP SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Allow Anonymous users to Login' 2 'Allow Local Users to Login' 3 'Allow Root Login' 4 'Deny some users' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch) == 1:
				os.system("`sed -i 's/#anonymous_enable=.*/anonymous_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				os.system("`sed -i 's/anonymous_enable=.*/anonymous_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				restart("vsftpd")
			elif int(ch)==2:
				os.system("`sed -i 's/#local_enable=.*/local_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				os.system("`sed -i 's/local_enable=.*/local_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				restart("vsftpd")
			elif int(ch)==3:
				os.system("`sed -i 's/#local_enable=.*/local_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				os.system("`sed -i 's/local_enable=.*/local_enable=YES/g' /etc/vsftpd/vsftpd.conf`")
				os.system("`sed -i 's/root//g' /etc/vsftpd/ftpusers`")
				os.system("`sed -i 's/root//g' /etc/vsftpd/user_list`")
				restart("vsftpd")			
			elif int(ch)==4:
				inputbox("Enter No. of users to deny them ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				for i in range(cnt):
					i=i+1
					inputbox("Enter user "+str(i),"15","60","confiles/config")
					fhusr=open("confiles/config", "r")
					user=fhusr.read().strip()
					fhusr.close()
					os.system("echo  "+user+"' ' >> /etc/vsftpd/ftpusers")
					os.system("echo  "+user+"' ' >> /etc/vsftpd/user_list")
				restart("vsftpd")				
			else:
				pass
		except:
			error()
			pass

def ssh_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'SSH SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 15 1 'Block Root Login through SSH' 2 'Permit Empty Passwords' 3 'Enable Password Authentification' 4 'Set Maximum Authentication Limit' 5 'Deny some users' 6 'Set Login Grace Time' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch) == 1:
				os.system("`sed -i 's/#PermitRootLogin.*/PermitRootLogin no/g' /etc/ssh/sshd_config`")
				os.system("`sed -i 's/PermitRootLogin.*/PermitRootLogin no/g' /etc/ssh/sshd_config`")
				restart("sshd")
			elif int(ch)==2:
				os.system("`sed -i 's/#PermitEmptyPasswords.*/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config`")
				os.system("`sed -i 's/PermitEmptyPasswords.*/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config`")
				restart("sshd")
			elif int(ch)==3:
				os.system("`sed -i 's/#PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config`")
				os.system("`sed -i 's/PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config`")
				restart("sshd")			
			elif int(ch)==4:
				inputbox("Enter No. of Maximum Tries ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=fhcnt.read().strip()
				fhcnt.close()
				os.system("`sed -i 's/#MaxAuthTries.*/MaxAuthTries "+cnt+"/g' /etc/ssh/sshd_config`")
				os.system("`sed -i 's/MaxAuthTries.*/MaxAuthTries "+cnt+"/g' /etc/ssh/sshd_config`")
				restart("sshd")
			elif int(ch)==5:
				inputbox("Enter No. of users to deny them ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=int(fhcnt.read())
				fhcnt.close()
				os.system("echo -n DenyUsers >> /etc/ssh/sshd_config") 
				for i in range(cnt):
					i=i+1
					inputbox("Enter user "+str(i),"15","60","confiles/config")
					fhusr=open("confiles/config", "r")
					user=fhusr.read().strip()
					fhusr.close()
					os.system("echo -n ' '"+user+"' ' >> /etc/ssh/sshd_config") 
				restart("sshd")	
			elif int(ch)==6:
				inputbox("Enter time in minutes ","15","60","confiles/config")
				fhcnt=open("confiles/config", "r")
				cnt=fhcnt.read().strip()
				fhcnt.close()
				os.system("`sed -i 's/#LoginGraceTime.*/LoginGraceTime "+cnt+"m/g' /etc/ssh/sshd_config`")
				os.system("`sed -i 's/LoginGraceTime.*/LoginGraceTime "+cnt+"m/g' /etc/ssh/sshd_config`")
				restart("sshd")			
			else:
				pass
		except:
			error()
			pass

def mail_conf():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --title 'MAIL SERVER CONFIGURATION' --menu 'Select Your Choice:-' 25 60 5 1 'Change Hostname' 2 'Allow Mail incoming from All Interfaces' 3 'Allow mail from Local machine' 4 'Mail Forwarding from Root Account' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			elif int(ch) == 1:
				inputbox("Enter Hostname","15","60","confiles/config")
				fhost=open("confiles/config", "r")
				hostname=fhost.read().strip()
				fhost.close()
				os.system("hostname "+hostname)
				restart("postfix")
			elif int(ch)==2:
				os.system("`sed -i 's/#inet_interfaces = all/inet_interfaces = all/g' /etc/postfix/main.cf`")
				os.system("`sed -i 's/inet_interfaces = localhost/#inet_interfaces = localhost/g' /etc/postfix/main.cf`")
				restart("postfix")
			elif int(ch)==3:
				os.system("`sed -i 's/#inet_interfaces = localhost/inet_interfaces = localhost/g' /etc/postfix/main.cf`")
				restart("postfix")			
			elif int(ch)==4:
				inputbox(" Enter the name of User ","15","60","confiles/config")
				fhusr=open("confiles/config", "r")
				user=fhusr.read().strip()
				fhusr.close()
				os.system("`sed -i 's/#root:		.*/root:		"+user+"/g' /etc/aliases`")
				os.system("`sed -i 's/root:		.*/root:		"+user+"/g' /etc/aliases`")
				os.system("newaliases")
				restart("postfix")	
			else:
				pass
		except:
			error()
			pass

#main_server_config()
