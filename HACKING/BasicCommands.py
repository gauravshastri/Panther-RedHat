import time
import sys
from dm import *
 
def basic():
	os.system("touch hackfiles/temp")
	try:
		while True:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title '*****BASIC COMMANDS*****' --menu 'Select your Choice' 30 50 12 1 'Show list of All TCP and UDP Ports' 2 'Calender' 3 'Linux Train' 4 'Browse Web using Mozilla Firefox' 5 'Hard Disk Status' 6 'Check CPU Load Status' 7 'List of All Users' 8 'Show all Mounted Devices' 9 'CPU Information' 10 'To see list of allowed ports for services' 11 'Show Computer Architecture' 2> hackfiles/temp")
			fhch=open("hackfiles/temp", "r")
			ch=fhch.read()
			fhch.close()
			if ch=="":
				break
			if ch == "1":
				os.system("netstat -ntulp &> hackfiles/temp")
				textbox("hackfiles/temp","50","100")		
			elif ch == "2":
				os.system("cal &> hackfiles/temp")
				textbox("hackfiles/temp","15","30")
			elif ch=="3":
				install("sl")
				os.system("sl")
			elif ch=="4":
				inputbox("Enter Website URL/IP Address here","10","40","hackfiles/temp")
				fhbasic=open("hackfiles/temp", "r")
				ip=fhbasic.read().strip()
				fhbasic.close()
				os.system("firefox "+ip)
			elif ch=="5":
				os.system("fdisk -cul &> hackfiles/temp")
				textbox("hackfiles/temp","40","100")
			elif ch=="6":
				os.system("uptime &> hackfiles/temp")
				textbox("hackfiles/temp","40","80")
			elif ch=="7":
				os.system("w &> hackfiles/temp")
				textbox("hackfiles/temp","40","60")
			elif ch=="8":
				os.system("df -h &> hackfiles/temp")
				textbox("hackfiles/temp","40","60")
			elif ch=="9":
				os.system("lscpu &> hackfiles/temp")
				textbox("hackfiles/temp","40","70")
			elif ch=="10":
				os.system("yum install -y policycoreutils-python &> /dev/null")
				os.system("semanage port -l &> hackfiles/temp")
				textbox("hackfiles/temp","50","50")
			elif ch=="11":
				os.system("uname -a &> hackfiles/temp")
				textbox("hackfiles/temp","30","100")		
			else:
				pass
	except:
		error()
		pass

