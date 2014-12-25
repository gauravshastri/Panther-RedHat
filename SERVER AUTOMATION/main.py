#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
from ClientConfig import *
from ServerConfig import *
from Client_Install import *
from Server_Install import *
import crypt

def main_server():
	
	os.system("touch confiles/passwd.txt") 
	infobox("**** USER AUTHENTICATION ****","\n\nPlease Enter your name & the Root Password to access the tool","10","45")	
	os.system("dialog --title '********LOGIN PROMPT********' --backtitle 'USER AUTHENTICATION' --insecure --mixedform 'Enter Your Credentials :' 15 48 0 'Your name       : ' 1 2 '' 1 20 20 0 0 'Root Password   :' 2 2 '' 2 20 20 0 1 'Retype Password :' 3 2 '' 3 20 20 0 1 2> confiles/passwd.txt")
	fh=open("confiles/passwd.txt", "r")
	user=fh.readline().strip()
	userpasswd=fh.readline().strip()
	retypeduserpasswd=fh.readline().strip()
	fh.close()
	if userpasswd!="" and retypeduserpasswd!="" and userpasswd==retypeduserpasswd:
		os.system("cat /etc/shadow | grep root &> confiles/password/passwd")
		os.system("cut -d: -f2 confiles/password/passwd > confiles/password/passwdhash ")
		os.system("cut -d$ -f2 confiles/password/passwdhash > confiles/password/method")
		os.system("cut -d$ -f3 confiles/password/passwdhash > confiles/password/salt")
		os.system("cut -d$ -f4 confiles/password/passwdhash > confiles/password/mainhash")
		fh=open("confiles/password/passwdhash", "r")
		roothash=fh.read().strip()
		fh.close()	
		fh=open("confiles/password/method", "r")
		method=fh.read().strip()
		fh.close()
		fh=open("confiles/password/salt", "r")
		salt=fh.read().strip()
		fh.close()
		fh=open("confiles/password/mainhash", "r")
		phash=fh.read().strip()
		fh.close()
		userhash=crypt.crypt(userpasswd,"$"+method+"$"+salt+"$")
		if roothash==userhash:
			infobox("******LOGIN SUCCESSFUL*****","\n\nYou are now authorised to use this tool","10","45")
			os.system("echo Hi "+user+", WELCOME TO REDHAT SERVER AUTOMATION TOOL | festival --tts")
			infobox("REDHAT SERVER AUTOMATION","\n************ A Piece of Advice ************ \n\nUse this tool wisely!!\n\nContact Developer in case of any bug/glitch","30","50")
			p=1
			os.system("touch confiles/config")
			while p!=0:
			 	os.system("dialog --ascii-lines --backtitle 'REDHAT SERVER AUTOMATION TOOL' --menu  'Choose from options' 25 60 15 1 'Server Side Installation' 2 'Server Side Configuration' 3 'Client Side Installation' 4 'Client Side Configuration' 2> confiles/config")
				fhch=open("confiles/config", "r")
				ch=fhch.read()
				fhch.close()
				if ch=="":
					os.system("clear;tput setaf 1;figlet -l -c -f banner -t  'BYE \n THANK YOU';tput setaf 0")
					os.system("sl")
					break
				elif int(ch)==1:
					main_server_install()
				elif int(ch)==2:
					main_server_config()

				elif int(ch)==3:
					main_client_install()
				elif int(ch)==4:
					main_client_config()
				else:
					infobox("Instructions","Some Unknown Error!! Program will terminate now. Please Contact Developer","25","30")
					time.sleep(3)
					sys.exit()
		else:
			msgbox("******* INCORRECT PASSWORD ********\n\nYou are not Authenticated as ROOT\n\n The tool will terminate now","20","40")
			main_server()
	elif userpasswd!="" and retypeduserpasswd!="" and userpasswd!=retypeduserpasswd:
		msgbox("*******PASSWORD MISMATCHING ********\n\nThe Password did not match\n\nThe tool will restart now","20","40")
		main_server()
	else:
		os.system("clear;tput setaf 1;figlet -l -c -f banner -t  'BYE \n THANK YOU';tput setaf 0")
		os.system("sl")
		sys.exit()
main_server()
