#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *

def main_client_config():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --backtitle 'CLIENT SIDE SOFTWARE Configuration' --menu  'Which Client/Software Do you want to Configure/Use?' 25 60 10 1 'Telnet' 2 'FTP' 3 'SSH' 4 'Web Browser' 5 'Mail' 6 'NIS' 7 'NFS' 8 'Samba' 9 'Autofs' 10 'NTP' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			os.system("setenforce 0")
			os.system("iptables -F")
			if ch=="":
				break
			elif int(ch)==1:
				telnet_client()
			elif int(ch)==2:
				ftp_client()
			elif int(ch)==3:
				ssh_client()
			elif int(ch)==4:
				web_client()
			elif int(ch)==5:
				mail_client()
			elif int(ch)==6:
				nis_client()
			elif int(ch)==7:
				nfs_client()
			elif int(ch)==8:
				samba_client()
			elif int(ch)==9:
				autofs_client()
			elif int(ch)==10:
				ntp_client()
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

def telnet_client():
	try:
		var=os.system("rpm -q telnet &> /dev/null")
		if var!=0:
			install("telnet")
		inputbox("Enter IP for Telnet connection ","15","40","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read().strip()
		fhip.close()
		msgbox("You Can Close Connection By Pressing Ctrl+D key","15","40")
		os.system("telnet "+ip)
	except:
		error()

def ssh_client():
	try:
		inputbox("Enter IP for SSH connection ","15","40","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read().strip()
		fhip.close()
		msgbox("You Can Close Connection By Pressing Ctrl+D key","15","40")
		os.system("ssh "+ip)
	except:
		error()
		pass

def ftp_client():
	try:
		var=os.system("rpm -q ftp &> /dev/null")
		if var!=0:
			install("ftp")
		inputbox("Enter IP for FTP connection ","15","40","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read().strip()
		fhip.close()
		msgbox("You Can Close Connection By Pressing Ctrl+D key","15","40")
		os.system("ftp "+ip)
	except:
		error()
		pass

def web_client():
	try:
		var=os.system("rpm -q firefox &> /dev/null")
		if var!=0:
			install("firefox")
		inputbox("Enter IP/URL of Website ","15","40","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read().strip()
		fhip.close()
		os.system("firefox "+ip)
	except:
		error()
		pass

def mail_client():
	p=1
	while p!=0:
		try:
			os.system("dialog --ascii-lines  --menu 'Select your Choice' 20 50 5 1 'Send Mail' 2 'Check All Received Mails' 2> confiles/config")
			fhch=open("confiles/config", "r")
			ch=fhch.read()
			fhch.close()
			var=os.system("rpm -q postfix &> /dev/null")
			if var!=0:
				install("postfix")
			if ch=="":
				break
			elif int(ch) == 1:
				inputbox("Enter Email Id/User to which you want to send mail ","15","40","confiles/config")
				fhip=open("confiles/config", "r")
				ip=fhip.read().strip()
				fhip.close()
				yesnobox("Do you want to attach a file??","10","40","confiles/config")
				fhyes=open("confiles/config", "r")
				status=fhyes.read().strip()
				fhyes.close()
				if status=="0":
					filebox("/root/Desktop/","confiles/config")
					fhfp=open("confiles/config", "r")
					fp=fhfp.read().strip()
					fhfp.close()
					os.system("mail -a "+fp+" "+ip)
				else:
					os.system("mail "+ip)
			elif int(ch) == 2:
				os.system("mail")	
			else:
				pass
		except:
			error()
			pass	

def nis_client():
	try:
		var=os.system("rpm -q ypbind &> /dev/null")
		if var!=0:
			install("ypbind")
		inputbox("Enter No. of users to Make their separate Directory where they can work","15","50","confiles/config")
		fhcnt=open("confiles/config", "r")
		cnt=int(fhcnt.read())
		fhcnt.close()
		for i in range(cnt):
			i=i+1
			inputbox("Enter user "+str(i),"10","50","confiles/config")
			fhusr=open("confiles/config", "r")
			user=fhusr.read().strip()
			fhusr.close()
			os.system("cp -rf /etc/skel /home/"+user)
		os.system("authconfig--tui")
	except:
		error()
		pass

def samba_client():
	try:
		var=os.system("rpm -q samba-client &> /dev/null")
		if var!=0:
			install("samba-client")
		inputbox("Enter ip address of samba server","15","50","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read()
		fhip.close()
		os.system("setenforce 0; iptables -F")
		inputbox("Enter Share Name ","15","50","confiles/config")
		fhsh=open("confiles/config", "r")
		sh=fhsh.read()
		fhsh.close()
		os.system("smbclient //"+ip+"/"+sh) 
	except:
		error()
		pass

def nfs_client():
	try:
		var=os.system("rpm -q nfs-utils &> /dev/null")
		if var!=0:
			install("nfs-utils")
		msgbox("Choose directory for mounting NFS folder","15","50")
		dirbox("/","confiles/config")
		fhdir=open("confiles/config", "r")
		direc=fhdir.read()
		fhdir.close()
		os.system("setenforce 0; iptables -F")
		inputbox("Enter ip address of nfs server","15","50","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read()
		fhip.close()
		inputbox("Enter Share Path ","15","50","confiles/config")
		fhsh=open("confiles/config", "r")
		sh=fhsh.read()
		fhsh.close()
		os.system("mkdir /media/"+direc)
		os.system("mount -t nfs "+ip+":"+sh+" /media/"+direc)
	except:
		error()
		pass

def autofs_client():
	try:
		var=os.system("rpm -q autofs &> /dev/null")
		if var!=0:
			install("autofs")
		inputbox("Enter Path of the directory for mounting user's workspace","15","50","confiles/config")
		fhdir=open("confiles/config", "r")
		direc=fhdir.read()
		fhdir.close()
		inputbox("Enter Name of the user for autofs","15","50","confiles/config")
		fhusr=open("confiles/config", "r")
		user=fhusr.read()
		fhusr.close()
		os.system("setenforce 0; iptables -F")
		inputbox("Enter ip address of nfs server","15","50","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read()
		fhip.close()
		inputbox("Enter Share Path ","15","50","confiles/config")
		fhsh=open("confiles/config", "r")
		sh=fhsh.read()
		fhsh.close()
		os.system("echo "+user+"	"+ip+":"+sh+"/"+user+" >> /etc/auto.misc")
		repl("/etc/auto.master",".*/etc/auto.misc",direc+"	/etc/auto.misc")	
		restart("autofs")
	except:
		error()
		pass

def ntp_client():
	try:
		var=os.system("rpm -q ntp &> /dev/null")
		if var!=0:
			install("ntp")
		inputbox("Enter ip address of ntp server","15","50","confiles/config")
		fhip=open("confiles/config", "r")
		ip=fhip.read()
		fhip.close()
		os.system("echo 'server '"+ip+" >> /etc/ntp.conf")
		restart("ntpd")
		os.system("ntpdate -b "+ip)
		msgbox("Time synchronised with the NTP Server","15","40") 
	except:
		error()
		pass
#main_client_config()
