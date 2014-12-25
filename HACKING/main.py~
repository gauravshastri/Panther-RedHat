#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
import crypt
import socket
from Network_Information import *
from Website_Information import *
from NetworkScanning import *
from Security import *
from Sniffing import *
from BasicCommands import *

def main_hacking():
	install("dialog")
	os.system("touch hackfiles/passwd.txt") 
	infobox("**** USER AUTHENTICATION ****","\n\nPlease Enter your name & the Root Password to access the pentesting tool","10","45")	
	os.system("dialog --title '********LOGIN PROMPT********' --backtitle 'USER AUTHENTICATION' --insecure --mixedform 'Enter Your Credentials :' 15 48 0 'Your name       : ' 1 2 '' 1 20 20 0 0 'Root Password   :' 2 2 '' 2 20 20 0 1 'Retype Password :' 3 2 '' 3 20 20 0 1 2> hackfiles/passwd.txt")
	fh=open("hackfiles/passwd.txt", "r")
	user=fh.readline().strip()
	userpasswd=fh.readline().strip()
	retypeduserpasswd=fh.readline().strip()
	fh.close()
	if userpasswd!="" and retypeduserpasswd!="" and userpasswd==retypeduserpasswd:
		os.system("cat /etc/shadow | grep root &> hackfiles/password/passwd")
		os.system("cut -d: -f2 hackfiles/password/passwd > hackfiles/password/passwdhash ")
		os.system("cut -d$ -f2 hackfiles/password/passwdhash > hackfiles/password/method")
		os.system("cut -d$ -f3 hackfiles/password/passwdhash > hackfiles/password/salt")
		os.system("cut -d$ -f4 hackfiles/password/passwdhash > hackfiles/password/mainhash")
		fh=open("hackfiles/password/passwdhash", "r")
		roothash=fh.read().strip()
		fh.close()	
		fh=open("hackfiles/password/method", "r")
		method=fh.read().strip()
		fh.close()
		fh=open("hackfiles/password/salt", "r")
		salt=fh.read().strip()
		fh.close()
		fh=open("hackfiles/password/mainhash", "r")
		phash=fh.read().strip()
		fh.close()
		userhash=crypt.crypt(userpasswd,"$"+method+"$"+salt+"$")
		if roothash==userhash:
			infobox("******LOGIN SUCCESSFUL*****","\n\nYou are now authorised to use this tool","10","45")
			infobox("******RESOLVING DEPENDENCIES*****","\n\nKindly wait for some time...","10","40")
			package_installer()		
			os.system("echo Hi "+user+", WELCOME TO THE PANTHER, A BASIC PENTESTING TOOL | festival --tts")
			infobox("---------ThE PaNtHeR---------","\n************ A Piece of Advice ************ \n\nUse this tool wisely and ethically!!\n\nContact Developer in case of any bug/glitch","30","50")
			p=1
			os.system("touch hackfiles/temp")
			while p!=0:
				try:
				 	os.system("dialog --cancel-label 'QUIT' --ascii-lines --backtitle 'ThE PaNtHeR :- A BASIC PENTESTING TOOL' --title 'MAIN MENU' --menu  'Choose from options' 25 60 10 1 'Information Gathering' 2 'Network Scanning' 3 'Packet Capturing' 4 'Security Implementation' 5 'PaNtHeR Attacks and Exploits' 6 'Miscellaneous-Basic Commands' 2> hackfiles/temp")
					fhch=open("hackfiles/temp", "r")
					ch=fhch.read()
					fhch.close()
					if ch=="":
						os.system("clear;tput setaf 1;figlet -l -c -f banner -t  'BYE \n THANK YOU';tput setaf 0")
						os.system("sl")
						break
					elif ch=="1":
						info_gather()
					elif ch=="2":
						main_network_scan()
					elif ch=="3":
						main_sniffing()
					elif ch=="4":
						main_security()
					elif ch=="5":
						pass
					elif ch=="6":
						basic()
					else:	
						pass
				except:
					error()
					pass
		else:
			msgbox("******* INCORRECT PASSWORD ********\n\nYou are not Authenticated as ROOT\n\n The tool will restart now","20","40")
			main_hacking()
	elif userpasswd!="" and retypeduserpasswd!="" and userpasswd!=retypeduserpasswd:
		msgbox("*******PASSWORD MISMATCHING ********\n\nThe Password did not match\n\nThe tool will restart now","20","40")
		main_hacking()
	else:
		os.system("clear;tput setaf 1;figlet -l -c -f banner -t  'BYE \n THANK YOU';tput setaf 0")
		os.system("sl")
		sys.exit()

def info_gather():
	os.system("touch hackfiles/temp")
	while True:
			try:
			 	os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title 'INFORMATION GATHERING' --menu  'Choose from options' 25 60 15 1 'Network Information' 2 'Website Information' 2> hackfiles/temp")
				fhch=open("hackfiles/temp", "r")
				ch=fhch.read()
				fhch.close()
				if ch=="":
					break
				if ch=="1":
					main_network_info()
				if ch=="2":
					main_website_info()
				else:
					pass
			except:
				error()
				pass

def package_installer():
	install("jwhois")
	install("festival")
	install("hping3")
	install("wireshark-gnome")
	install("nmap")
	install("traceroute")
	install("tcpdump")
	install("dsniff")
	install("sl")
	install("figlet")
	install("mplayer")
	install("wget")
	return
	
main_hacking()
