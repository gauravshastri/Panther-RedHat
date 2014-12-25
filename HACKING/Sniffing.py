#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
import commands

def main_sniffing():
	p=1
	os.system("touch hackfiles/temp")
	try:
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'SNIFFING/PACKET CAPTURING' --menu  'Select an Option' 10 50 2 1 'Using TCPDUMP' 2 'Using TSHARK'  2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				tcpdump()
			elif int(ch)==2:
				tshark()
			else:
				infobox("****Instructions*****","Some Unknown **********Error!!********** Program will terminate now. Please Contact Developer","25"," 40")
				time.sleep(5)
				sys.exit()
	except:
		pass

def interface():
	inputbox("Enter the name of Interface e.g. wlan0:-","15","60","hackfiles/temp")
	fh=open("hackfiles/temp", "r")
	interface= fh.read().strip()
	fh.close()
	return interface

def wait():
	raw_input("\n*************************Press Enter to Continue************************\n")

def tcpdump():
	p=1
	os.system("touch hackfiles/temp")
	try:
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'SNIFFING/PACKET CAPTURING' --title 'TCPDUMP' --menu  'Select an Option' 25 70 9 1 'Capture packets from a particular ethernet interface' 2 'Capture only N number of packets ' 3 'Display Captured Packets in ASCII' 4 'Display Captured Packets in HEX and ASCII' 5 'Capture the packets and write into a file ' 6 'Read packets longer than N bytes' 7 'Read packets lesser than N bytes' 8  'Receive only the packets of a specific protocol type' 9 'Receive packets flows on a particular port' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				inter = interface()
				if inter!="":
					os.system("tcpdump -i " + inter)
					wait()
				continue
			elif int(ch)==2:
				inter = interface()
				inputbox("Enter the Number of packets :-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				N=fh.read().strip()
				fh.close()
				if inter!="" and N!="" and N.isdigit():		
					os.system("tcpdump -c "+N+" -i "+inter)
					wait()
				continue
			elif int(ch)==3:
				inter = interface()
				if inter!="":
					os.system("tcpdump -A -i "+inter)
					wait()
				continue
			elif int(ch)==4:
				inter =interface()
				if inter!="":
					os.system("tcpdump -XX -i "+inter)
					wait()
				continue
			elif int(ch)==5:
				inter = interface()
				if inter!="":
					inputbox("Enter the Full Path of the File:-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					filename=fh.read().strip()
					os.system("tcpdump -i "+inter+" -XX > "+filename)
					wait()
				continue
			elif int(ch)==6:
				inter=interface()
				if inter!="":
					inputbox("Enter the Minimum size of packets :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					size=fh.read().strip()
					fh.close()
					if size.isdigit():
						os.system("tcpdump -i "+inter+" -XX greater "+size)
						wait()
				continue
			elif int(ch)==8:
				inter=interface()
				if inter!="":
					inputbox("Enter the name of Protocols :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					proto=fh.read().strip()
					fh.close()
					if proto!="":
						os.system("tcpdump -i "+inter+" "+proto)
						wait()
				continue
			elif int(ch)==7:
				inter=interface()
				if inter!="":
					inputbox("Enter the Maximum size of packets :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					size=fh.read().strip()
					fh.close()
					if size.isdigit():
						os.system("tcpdump -i "+inter+" -XX less "+size)
						wait()
				continue
			elif int(ch)==9:
				inter=interface()
				if inter!="":
					inputbox("Enter Port No. :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					port=fh.read().strip()
					fh.close()
					if size.isdigit():
						os.system("tcpdump -i "+inter+" port "+port)
						wait()
				continue
			else:
				msgbox("Something wrong went this time!! \nPress OK to Continue...","15"," 40")
				pass
	except:		
		retard()	
		pass

def tshark():
	p=1
	os.system("touch hackfiles/temp")
	try:
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'SNIFFING/PACKET CAPTURING' --title 'TSHARK' --menu  'Select an Option' 25 70 9 1 'Open WIRESHARK--GUI based Network Analyzer' 2 'Capture only N number of packets ' 3 'Capture packets over a Port' 4 'Enable MAC address resolution in Capturing' 5 'Version of tshark' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				os.system("wireshark &> /dev/null")
			elif int(ch)==2:
				inter=interface()
				if inter!="":
					inputbox("Enter the Number of packets :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					N=fh.read().strip()
					fh.close()
					if size.isdigit():
						os.system("tshark -c "+N+" -i "+inter)
						wait()
				continue			
			elif int(ch)==3:
				inter=interface()
				if inter!="":
					inputbox("Enter Port No. :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					portno=fh.read().strip()
					fh.close()
					if size.isdigit():
						os.system("tshark port "+portno+" -i "+inter)
						wait()
				continue
			elif int(ch)==4:
				inter=interface()
				if inter!="":
					os.system("tshark -Nm -i "+inter)
					wait()
			elif int(ch)==5:
				os.system("tshark -v &> hackfiles/temp")
				textbox("hackfiles/temp","25","100")
				wait()
			else:
				msgbox("Something wrong went this time!! \nPress OK to Continue...","15"," 40")
				pass
	except:
		retard()	
		pass
		
#main_sniffing()
