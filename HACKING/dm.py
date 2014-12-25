#!/usr/bin/python2
import os
import time
import sys
import commands

def retard():
	os.system("eog --fullscreen retard.png & sleep 3; pkill eog")

def error():
	infobox("**********Error!!**********","Either you provided wrong input or some unknown error occurred.\n\n\nPlease Contact Developer","25"," 50")
	time.sleep(3)

def install(package):
	os.system("yum install "+ package +" -y &> /dev/null")

def restart(service_name):
	os.system("service "+service_name+" restart &> /dev/null")

def infobox(title,text,h,w):
	os.system("dialog --ascii-lines   --title '"+title+"' --infobox '"+ text +"' "+h+" "+w)
	time.sleep(3)

def msgbox(text,h,w):
	os.system("dialog --ascii-lines  --msgbox '"+ text +"' "+h+" "+w)
	
def inputbox(text,h,w,filepath):
	os.system("dialog --ascii-lines --max-input 40 --inputbox '"+text+"' "+h+" "+w+" 2> "+filepath)

def passwdbox(h,w,filepath):
	os.system("dialog --ascii-lines --cancel-label 'QUIT' --title 'User Authentication' --clear --insecure --passwordbox 'Enter password' "+h+" "+w+" 2> "+filepath)

def progressbar(h,w):
	os.system("for i in $(seq 0 4 100) ; do sleep 0.05; echo $i | dialog --ascii-lines  --gauge 'Please wait' "+h+" "+w+" 0; done")

def yesnobox(text,h,w,filepath):
	x=os.system("dialog --ascii-lines   --yesno '"+text+"' "+h+" "+w+" ; echo $? > "+filepath )

def dirbox(init_dir_path, filepath):
	os.system("dialog --ascii-lines  --title 'Select a Directory' --dselect "+init_dir_path+" 10 60 2> "+filepath)

def filebox(init_dir_path, filepath):
	os.system("dialog --ascii-lines  --title 'Select a File' --fselect "+init_dir_path+" 10 60 2> "+filepath)

def editbox(filepath,h,w):
	os.system("dialog --ascii-lines  --fselect "+filepath+" 25 60 2> "+filepath)

def tailbox(filepath,h,w):
	os.system("dialog --exit-label 'CONTINUE' --ascii-lines  --tailbox "+filepath+" "+h+" "+w)

def textbox(filepath,h,w):
	os.system("dialog --exit-label 'CONTINUE' --ascii-lines  --textbox "+filepath+" "+h+" "+w)
