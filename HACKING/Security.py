#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
import socket
import commands

def showrules():
	os.system("iptables -L -n -v --line-numbers &> hackfiles/temp")
	textbox("hackfiles/temp","40","120")

def chain():
	inputbox("Enter the Chain Code:-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	chain=fh.read().strip()
	fh.close()
	if chain=="I":
		return "INPUT"
	elif chain=="O":
		return "OUTPUT"
	elif chain=="F":
		return "FORWARD"
	
def getip():
	inputbox("Enter IP :-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	ip=fh.read().strip()
	fh.close()
	return ip

def getweb():
	inputbox("Enter Website Name:-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	web=fh.read().strip()
	fh.close()
	return web

def getport():
	inputbox("Enter the Port no:-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	port=fh.read().strip()
	fh.close()
	return port

def getuser():
	inputbox("Enter UserName/UserId:-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	user=fh.read().strip()
	fh.close()
	return user


def getfile():
	infobox("****File Selection****","\nPlease Select a file","15","50")
	filebox("/","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	filepath=fh.read().strip()
	fh.close()
	return filepath

def main_security():
	p=1
	os.system("touch hackfiles/temp")
	try:
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'SECURITY IMPLEMENTATION' --menu  'Select an Option' 20 50 6 1 'Access Control List' 2 'Firewall' 3 'SeLinux' 4 'TCP Wrapper' 5 'Permissions' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				acl()
			elif int(ch)==2:
				firewall()
			elif int(ch)==3:
				selinux()
			elif int(ch)==4:
				tcpwrapper()
			elif int(ch)==5:
				permissions()
			else:
				pass
	except:
		error()
		pass

def acl():
	p=1
	os.system("touch hackfiles/temp")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'ACL SECURITY IMPLEMENTATION' --menu  'Select an Option' 20 50 5 1 'Give read/write permissions via username/userid' 2 'Remove all permissions for a file/folder' 3 'Setting default ACLs for directories' 4 'Retrieving ACLs' 5 'Remove all permissions' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				#Give permissions via username/userid
				user=getuser()
				filepath=getfile()
				if user!="" and filepath!="":
					os.system("setfacl -m u:"+user+":rw "+filepath)
					msgbox("*****ACL Security Implemented*****","15","50")
			elif int(ch)==2:
				#Remove all permissions
				filepath=getfile()
				if filepath!="":
					os.system("setfacl -x u:500 "+filepath)
					msgbox("*******Removed All Permissions for the file*******","15","50")
			elif int(ch)==3:
				#Setting default ACLs
				infobox("****Directory Selection****","\nPlease Select a Directory","15","50")
				dirbox("/","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				directory=fh.read().strip()
				fh.close()
				if directory!="":
					os.system("setfacl -m d:o:rx "+directory)
					msgbox("*******Set Default ACLs for the Directory*******","15","50")
			elif int(ch)==4:
				#Retrieving ACLs
				filepath=getfile()
				if filepath!="":
					os.system("getfacl "+filepath+" &> hackfiles/temp")
					textbox("hackfiles/temp","40","90")
			elif int(ch)==5:
				#Remove all permissions:
				os.system("setfacl -b")
				msgbox("*******Removed All ACL permissions*******","15","50")
			else:
				pass
		except:
			error()
			pass
	
def firewall():
	p=1
	os.system("touch hackfiles/temp")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'FIREWALL SECURITY IMPLEMENTATION' --menu  'Select an Option' 25 70 13 1 'Displaying the Status of Your Firewall' 2 'Restart the Firewall' 3 'Flush Firewall--Delete All rules' 4 'Delete a particular line number in the rules' 5 'Delete Input Chain DROP rules for a host' 6 'Block an IP/host' 7 'Save Firewall Rules' 8 'Restore Firewall Rules' 9 'Drop Private Network Address On Public Interface' 10 'Block Incoming TCP Port Requests (BLOCK PORT)' 11 'Block Outgoing IP Address' 12 'Block outgoing Website' 13 'Block ICMP Ping Request' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				showrules()
			elif int(ch)==2:
				os.system("service iptables restart")
				msgbox("**********Done***********","15","30")
			elif int(ch)==3:
				os.system("iptables -F")
				msgbox("**********Done***********","15","30")
			elif int(ch)==4:
				msgbox("*****CHAIN CODES******\n\nI:-INPUT Chain\nO:-OUTPUT Chain\nF:-FORWARD Chain","20","40")
				chn=chain()
				if (chn=='INPUT' or chn=='OUTPUT' or chn=='FORWARD'):
					inputbox("Enter the line no.:-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					lineno=fh.read().strip()
					fh.close()
					if lineno.isdigit(): 
						os.system("iptables -D "+chn+" "+lineno)
						showrules()
				else:
					error()
			elif int(ch)==5:
				ip=getip()
				try:
					xx=socket.inet_aton(ip)
				except:
					retard()
					continue
				os.system("iptables -D INPUT -s "+ip+" -j DROP")
				msgbox("**********Done***********","15","30")
				showrules()
			elif int(ch)==6:
				ip=getip()
				try:
					xx=socket.inet_aton(ip)
				except:
					retard()
					continue
				os.system("iptables -I INPUT -s "+ip+" -j DROP")
				msgbox("**********Done***********","15","30")
				showrules()
			elif int(ch)==7:
				os.system("service iptables save")
				msgbox("**********Firewall Rules Saved***********","15","50")
			elif int(ch)==8:
				infobox("****Firewall Rules Restore****","\nPlease Select a file which contains firewall rules","15","50")
				filebox("/","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				filepath=fh.read().strip()
				fh.close()
				if filepath!="":
					os.system("iptables-restore < "+filepath)
					os.system("service iptables restart &> /dev/null")
					msgbox("**********Rules Restored***********","15","50")
					showrules()
			elif int(ch)==9:
				inputbox("Enter full Private Network name e.g. 10.0.0.0/8 or 192.168.0.0/24 :-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				network=fh.read().strip()
				fh.close()
				IP = network.split("/")[0]
				try:
					xx=socket.inet_aton(IP)
				except:
					retard()
					continue
				os.system("iptables -A INPUT -s "+network+" -j DROP")
				msgbox("**********Private Network filtered***********","15","50")
				showrules()
			elif int(ch)==10:
				portno=getport()
				if portno!="" and portno.isdigit():
					os.system("iptables -I INPUT -p tcp --dport "+portno+" -j DROP")
					msgbox("**********Port "+portno+" Blocked***********","15","50")
					showrules()
			elif int(ch)==11:
				ip=getip()
				try:
					xx=socket.inet_aton(ip)
				except:
					retard()
					continue
				os.system("iptables -I OUTPUT -d "+ip+" -j DROP")
				msgbox("**********Blocked Access to "+ip+" ***********","15","50")
				showrules()
			elif int(ch)==12:
				web=getweb()
				if web!="":
					os.system("iptables -I OUTPUT -p tcp -d "+web+" -j DROP")
					msgbox("**********Blocked Access to "+web+" ***********","15","50")
					showrules()
			elif int(ch)==13:
				os.system("iptables -I INPUT -p icmp --icmp-type echo-request -j DROP")
				msgbox("**********Blocked ICMP ping request  ***********","15","60")
				showrules()
			else:
				pass
		except:
			error()
			pass

def selinux():
	p=1
	os.system("touch hackfiles/temp")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'SELINUX SECURITY' --menu  'Select an Option' 25 70 13 1 'Display Current Status of SELINUX' 2 'Turn on Security for some service' 3 'Turn on Security for some service' 4 'Change SELINUX to Enforcing Mode' 5 'Change SELINUX to Permissive Mode' 6 'Disable SELINUX' 7 'Enable MLS-Multi Level Security Protection' 8 'Change SELINUXTYPE to targeted' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				os.system("getsebool -a &> hackfiles/temp")
				textbox("hackfiles/temp","50","60")
			elif int(ch)==2:
				infobox("********SELINUX SECURITY********","Get the name of the service by checking current status of SELINUX!!","15","30")
				inputbox("Enter Name of the service:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				service=fh.read().strip()
				fh.close()
				if service!="":
					os.system("setsebool "+service+" on &> hackfiles/temp")
					os.system("getsebool -a &> hackfiles/temp")
					textbox("hackfiles/temp","50","60")
			elif int(ch)==3:
				infobox("********SELINUX SECURITY********","Get the name of the service by checking current status of SELINUX!!","15","30")
				inputbox("Enter Name of the service:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				service=fh.read().strip()
				fh.close()
				if service!="":
					os.system("setsebool "+service+" off &> hackfiles/temp")
					os.system("getsebool -a &> hackfiles/temp")
					textbox("hackfiles/temp","50","60")
			elif int(ch)==4:
				os.system(" `sed -i 's/SELINUX=.*/SELINUX=enforcing/g' /etc/selinux/config` ")
				msgbox("**********DONE***********","15","40")
			elif int(ch)==5:
				os.system(" `sed -i 's/SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config` ")
				msgbox("**********DONE***********","15","40")
			elif int(ch)==6:
				os.system("setenforce 0")
				os.system("`sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config`")
				msgbox("**********DONE***********","15","40")
			elif int(ch)==7:
				os.system("setenforce 0")
				os.system("`sed -i 's/SELINUXTYPE=.*/SELINUXTYPE=mls/g' /etc/selinux/config`")
				msgbox("**********DONE***********","15","40")
			elif int(ch)==8:
				os.system("setenforce 0")
				os.system("`sed -i 's/SELINUXTYPE=.*/SELINUXTYPE=targeted/g' /etc/selinux/config`")
				msgbox("**********DONE***********","15","40")
			else:	
				pass
		except:
			error()
			pass

def tcpwrapper():
	p=1
	os.system("touch hackfiles/temp")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'TCP WRAPPER' --menu  'Select an Option' 10 50 4 1 'ALLOW Hosts' 2 'DENY Hosts' 2> hackfiles/temp")
			fh=open("hackfiles/temp","r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				infobox("********TCP WRAPPER SECURITY********","\nIf you want to apply security over all services, use service name=ALL\n\nIf you want to allow all hosts, then use hostname=ALL ","20","80")
				inputbox("Enter Daemon/Service e.g. sshd,vsftpd,ALL:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				service=fh.read().strip()
				fh.close()	
				inputbox("Enter Host IP/Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				host=fh.read().strip()
				fh.close()
				if service!="" and host!="":
					os.system("echo "+service+": "+host+" >> /etc/hosts.allow")				
			elif int(ch)==2:
				infobox("********TCP WRAPPER SECURITY********","\nIf you want to apply security over all services, use service name=ALL\n\nIf you want to deny all hosts, then use hostname=ALL ","20","80")
				inputbox("Enter Daemon/Service e.g. sshd,vsftpd,ALL:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				service=fh.read().strip()
				fh.close()	
				inputbox("Enter Host IP/Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				host=fh.read().strip()
				fh.close()
				if service!="" and host!="":
					os.system("echo "+service+": "+host+" >> /etc/hosts.deny")
		except:
			error()
			pass

def permissions():
	p=1
	os.system("touch hackfiles/temp")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'FILE AND DIRECTORY PERMISSIONS' --menu  'Select an Option' 15 50 6 1 'View Permissions of a File' 2 'View Permissions of a Directory' 3 'Change Permission of a File' 4 'Change Permission of a Directory' 2> hackfiles/temp")
			fh=open("hackfiles/temp","r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				filepath=getfile()
				if filepath!="":
					os.system("ls -l "+filepath+" &> hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					info=fh.read().strip()
					fh.close()
					msgbox("******Current Permissions******\n\n"+info,"10","110")
			elif int(ch)==2:
				infobox("****Directory Selection****","\nPlease Select a Directory","15","50")
				dirbox("/","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				directory=fh.read().strip()
				fh.close()
				if directory!="":
					os.system("ls -ld "+directory+" &> hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					info=fh.read().strip()
					fh.close()
					msgbox("******Current Permissions******\n\n"+info,"10","110")	
			elif int(ch)==3:
				filepath=getfile()
				if filepath!="":
					os.system("ls -l "+filepath+" &> hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					info=fh.read().strip()
					fh.close()
					msgbox("******Current Permissions******\n\n"+info,"10","110")
					inputbox("Enter the permission code e.g. 777,755 700:-","10","40","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					code=fh.read().strip()
					if code.isdigit() and code!="":
						os.system("chmod "+code+" "+filepath)
						os.system("ls -l "+filepath+" &> hackfiles/temp")
						fh=open("hackfiles/temp", "r")
						info=fh.read().strip()
						fh.close()
						msgbox("******Changed Permissions******\n\n"+info,"10","110")
			elif int(ch)==4:
				infobox("****Directory Selection****","\nPlease Select a Directory","15","50")
				dirbox("/","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				directory=fh.read().strip()
				fh.close()
				if directory!="":
					os.system("ls -ld "+directory+" &> hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					info=fh.read().strip()
					fh.close()
					msgbox("******Current Permissions******\n\n"+info,"10","110")
					inputbox("Enter the permission code e.g. 777,755 700:-","15","40","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					code=fh.read().strip()
					fh.close()
					if code.isdigit() and code!="":
						os.system("chmod "+code+" "+directory)
						os.system("ls -ld "+directory+" &> hackfiles/temp")
						fh=open("hackfiles/temp", "r")
						info=fh.read().strip()
						fh.close()
						msgbox("******Changed Permissions******\n\n"+info,"10","110")
			else:	
				pass
		except:
			error()
			pass

#main_security()
