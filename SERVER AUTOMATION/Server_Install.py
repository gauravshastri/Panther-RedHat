#!/usr/bin/python2
import os
import time
import sys
from dm import *


def main_server_install():
	p=1
	os.system("touch confiles/config")
	os.system("setenforce 0")
	os.system("iptables -F")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --backtitle 'SERVER SIDE SOFTWARE INSTALLATION' --menu  'Install Server Side Requirements for :-' 25 60 10 1 'Telnet' 2 'FTP' 3 'SSH' 4 'Apache' 5 'Mail' 6 'NIS' 7 'NFS' 8 'Samba' 9 'Install All at once' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			os.system("cat clear > confiles/servers_status &> /dev/null")
			if ch=="":
				break
			elif int(ch)==1:
				telnet_install()
			elif int(ch)==2:
				ftp_install()
			elif int(ch)==3:
				ssh_install()
			elif int(ch)==4:
				web_install()
			elif int(ch)==5:
				mail_install()
			elif int(ch)==6:
				nis_install()
			elif int(ch)==7:
				nfs_install()
			elif int(ch)==8:
				samba_install()
			elif int(ch)==9:
				AllAtOneGo()
			else:
				pass
		except:
			error()
			pass

def AllAtOneGo():	
	os.system("cat clear > confiles/servers_status &> /dev/null")
	telnet_install()
	ftp_install()
	web_install()
	mail_install()
	ssh_install()
	nis_install()
	nfs_install()
	samba_install()
	textbox("confiles/servers_status","40","60")

def ftp_install():
	try:
		var=os.system("rpm -q vsftpd &> /dev/null")
		if var!=0:
			install("vsftpd")
		restart("vsftpd")
		os.system("echo '\nFTP Server:-' >> confiles/servers_status")
		os.system("service vsftpd status >> confiles/servers_status")
		os.system("chkconfig vsftpd on")
		msgbox("Successfully Installed FTP server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def telnet_install():
	try:
		var=os.system("rpm -q telnet-server &> /dev/null")+os.system("rpm -q telnet &> /dev/null")
		if var!=0:
			install("telnet")
			install("telnet-server")
		restart("xinetd")
		restart("telnet")
		os.system("echo '\nTelnet Server:-' >> confiles/servers_status")
		os.system("service xinetd status >> confiles/servers_status")
		os.system("chkconfig telnet on")
		os.system("chkconfig xinetd on")
		msgbox("Successfully Installed Telnet server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def samba_install():
	try:
		var=os.system("rpm -q samba* &> /dev/null")
		if var!=0:
			install("samba")
		restart("smb")
		os.system("echo '\nSamba Server:-' >> confiles/servers_status")
		os.system("service smb status >> confiles/servers_status")
		os.system("chkconfig smb on")
		msgbox("Successfully Installed Samba server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def ssh_install():
	try:
		var=os.system("rpm -q openssh-server &> /dev/null")
		if var!=0:
			install("openssh-server")
		restart("sshd")
		os.system("echo '\nSSH Server:-' >> confiles/servers_status")
		os.system("service sshd status >> confiles/servers_status")
		os.system("chkconfig sshd on")
		msgbox("Successfully Installed SSH server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def web_install():
	try:
		var=os.system("rpm -q http* &> /dev/null")
		if var!=0:
			install("httpd")
			install("httpd-devel")
		restart("httpd")
		os.system("echo '\nWEB Server:-' >> confiles/servers_status")
		os.system("service httpd status >> confiles/servers_status")
		os.system("chkconfig httpd on")
		msgbox("Successfully Installed Apache Web server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def mail_install():
	try:
		var=os.system("rpm -q postfix &> /dev/null")
		if var!=0:
			install("postfix")
		restart("postfix")
		restart("network")
		os.system("echo '\nMail Server:-' >> confiles/servers_status")
		os.system("service postfix status >> confiles/servers_status")
		os.system("chkconfig postfix on")
		msgbox("Successfully Installed Mail server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def nis_install():
	try:
		var=os.system("rpm -q ypserv &> /dev/null")
		if var!=0:
			install("ypserv")
		restart("ypserv")
		os.system("echo '\nNIS Server:-' >> confiles/servers_status")
		os.system("service ypserv status  >> confiles/servers_status")
		os.system("chkconfig ypserv on")
		msgbox("Successfully Installed NIS server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def nfs_install():
	try:
		var=os.system("rpm -q nfs-utils &> /dev/null")
		if var!=0:
			install("nfs")
		restart("nfs")
		os.system("echo '\nNFS Server:-' >> confiles/servers_status")
		os.system("service nfs status >> confiles/servers_status")
		os.system("chkconfig nfs on")
		msgbox("Successfully Installed NFS server on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

#main_server_install()
