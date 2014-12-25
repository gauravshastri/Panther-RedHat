#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
import commands

def wait():
	raw_input("\n*************************Press Enter to Continue************************\n")

def main_network_info():
	try:
		p=1
		os.system("touch hackfiles/temp")
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'NETWORK INFORMATION' --menu  'Select an Option' 25 60 15 1 'Know your IP Address' 2 'Know your MAC Address' 3 'Know your Gateway/Router info ' 4 'Network Information Of All Interfaces' 5 'Ping a certain IP with customization' 6 'Trace Route to a Destination IP'  2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				ip()
			elif int(ch)==2:
				mac()
			elif int(ch)==3:
				gateway()
			elif int(ch)==4:
				ifconfig()
			elif int(ch)==5:
				ping()
			elif int(ch)==6:
				traceroute()
			else:
				pass
	except:
		error()

def ip():
	try:
		ip= commands.getoutput("hostname -I").strip()
		iplist=ip.split()
		if ip=="":
			msgbox("Your system does not have any IP other than LocalHost","15","30")
			return
		ip_string="Your System has "+str(len(iplist))+" IP\n"
		for i in iplist:
			ip_string+=i+"\n"
		msgbox(ip_string,"15","50")		
	except:
		error()
		pass
		
def mac():
	try:
		inputbox("Enter the name of the Interface:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		interface=fh.read().strip()
		fh.close()
		mac=commands.getoutput("/sbin/ifconfig | grep "+interface+" | tr -s ' ' | cut -d ' ' -f5")
		if mac=="":
			msgbox("The "+interface+" interface does not have any MAC Address or the interface itself does not exist","15","30")
			return
		msgbox("The MAC Address of "+interface+" interface is "+mac,"15","60")
		time.sleep(4)
	except:
		error()
		pass

def gateway():
	try:
		os.system("route -n &> hackfiles/temp")
		textbox("hackfiles/temp","15","85")
	except:
		error()
		pass

def ifconfig():
	try:
		os.system("ifconfig &> hackfiles/temp")
		textbox("hackfiles/temp","40","80")
	except:
		error()
		pass

def traceroute():
	try:
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		ip=fh.read().strip()
		fh.close()
		if ip!="":
			os.system("traceroute "+ip+" &> hackfiles/temp")
			textbox("hackfiles/temp","30","150")
	except:
		error()
		pass

def ping():
	p=1
	os.system("touch hackfiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'PING an IP/Website' --menu  'Select an Option' 25 70 7 1 'Increase or Decrease the Time Interval Between Packets' 2 'Send N packets and stop' 3 'Flood the network' 4 'Audible ping: Give beep when the peer is reachable' 5 'Change Ping Packet Size'  2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				ip=fh.read().strip()
				fh.close()
				inputbox("Enter the time interval b/w the packets (in sec):-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				time=fh.read().strip()
				fh.close()
				if ip!="" and time.isdigit():
					os.system("ping -i "+time+" "+ip)
					wait()
			elif int (ch)==2:
				inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				ip=fh.read().strip()
				fh.close()
				inputbox("Enter the No. of Packets which you want to send:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				N=fh.read().strip()
				fh.close()
				if ip!="" and N.isdigit():
					os.system("ping -c "+N+" "+ip)
					wait()
			elif int (ch)==3:
				inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				ip=fh.read().strip()
				fh.close()
				if ip!="":
					os.system("ping -f "+ip)
					wait()
			elif int (ch)==4:
				inputbox("Enter the IP/Website Name which you want to flood:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				ip=fh.read().strip()
				fh.close()
				if ip!="":
					os.system("ping -a "+ip)
					wait()
			elif int(ch)==5:
				inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				ip=fh.read().strip()
				fh.close()
				inputbox("Enter the size of packet data:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				size=fh.read().strip()
				fh.close()
				if ip!="" and size.isdigit():
					os.system("ping -s "+size+" "+ip)
					wait()
			else:
				pass
		except:
			error()
			pass
#main_network_info()