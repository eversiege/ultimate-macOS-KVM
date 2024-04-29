#!/usr/bin/env python3
# pylint: disable=C0301,C0116,C0103,R0903

"""
This script was created by Coopydood as part of the ultimate-macOS-KVM project.

https://github.com/user/Coopydood
https://github.com/Coopydood/ultimate-macOS-KVM
Signature: 4CD28348A3DD016F

"""


import os
import time
import subprocess
import re 
import json
import argparse
import platform
import datetime
import cpuinfo
import psutil
import sys
sys.path.append('./resources/python')
import distro
from datetime import datetime

detectChoice = 1
latestOSName = "Sonoma"
latestOSVer = "14"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   GRAY = '\u001b[38;5;245m'

scriptName = "System Profile Tool"
script = "sysprofiler.py"
scriptID = "SPT"
scriptVendor = "Coopydood"
scriptVer = 1.0
branch = "dev"

version = open("./.version")
version = version.read()

versionDash = version.replace(".","-")

def clear(): print("\n" * 150)

cS = 5

clear()

for x in range(1,1):
    print("\nThis script will check your system to ensure it is ready for basic KVM. \nChecks will begin in",cS,"seconds. \nPress CTRL+C to cancel.")
    cS = cS - 1
    time.sleep(1)
    clear()

clear()

print("\n\n   "+color.BOLD+color.BLUE+"SYSTEM PROFILE TOOL"+color.END,"")
print("   Gathering system information")
print("\n   Please wait while the tool gathers info\n   about your system. No personal data is\n   included in the report.\n\n\n\n\n\n   ")
def progressUpdate(progressVal,*args):
    progress = progressVal
    if progress <= 5:
        progressGUI = (color.BOLD+""+color.GRAY+"━━━━━━━━━━━━━━━━━━━━")
    elif progress > 5 and progress <= 10:
        progressGUI = (color.BOLD+"━"+color.GRAY+"━━━━━━━━━━━━━━━━━━━")
    elif progress > 10 and progress <= 20:
        progressGUI = (color.BOLD+"━━"+color.GRAY+"━━━━━━━━━━━━━━━━━━")
    elif progress > 20 and progress <= 25:
        progressGUI = (color.BOLD+"━━━"+color.GRAY+"━━━━━━━━━━━━━━━━━")
    elif progress > 25 and progress <= 30:
        progressGUI = (color.BOLD+"━━━━"+color.GRAY+"━━━━━━━━━━━━━━━━")
    elif progress > 30 and progress <= 35:
        progressGUI = (color.BOLD+"━━━━━"+color.GRAY+"━━━━━━━━━━━━━━━")
    elif progress > 35 and progress <= 40:
        progressGUI = (color.BOLD+"━━━━━━"+color.GRAY+"━━━━━━━━━━━━━━")
    elif progress > 40 and progress <= 45:
        progressGUI = (color.BOLD+"━━━━━━━"+color.GRAY+"━━━━━━━━━━━━━")
    elif progress > 45 and progress <= 50:
        progressGUI = (color.BOLD+"━━━━━━━━"+color.GRAY+"━━━━━━━━━━━━")
    elif progress > 50 and progress <= 55:
        progressGUI = (color.BOLD+"━━━━━━━━━"+color.GRAY+"━━━━━━━━━━━")
    elif progress > 55 and progress <= 60:
        progressGUI = (color.BOLD+"━━━━━━━━━━"+color.GRAY+"━━━━━━━━━━")
    elif progress > 60 and progress <= 65:
        progressGUI = (color.BOLD+"━━━━━━━━━━━"+color.GRAY+"━━━━━━━━━")
    elif progress > 65 and progress <= 70:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━"+color.GRAY+"━━━━━━━━")
    elif progress > 70 and progress <= 75:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━"+color.GRAY+"━━━━━━━")
    elif progress > 75 and progress <= 80:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━"+color.GRAY+"━━━━━━")
    elif progress > 80 and progress <= 85:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━━"+color.GRAY+"━━━━━")
    elif progress > 85 and progress <= 90:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━━━"+color.GRAY+"━━━━")
    elif progress > 90 and progress <= 95:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━━━━"+color.GRAY+"━━━")
    elif progress > 95 and progress <= 98:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━━━━━━"+color.GRAY+"━")
    elif progress > 98 and progress <= 99:
        progressGUI = (color.BOLD+"━━━━━━━━━━━━━━━━━━━━"+color.GRAY+"")
    elif progress >= 100:
        progressGUI = (color.BOLD+color.GREEN+"━━━━━━━━━━━━━━━━━━━━"+color.GRAY+"")
    sys.stdout.write('\033[F\033[F\033[F\033[F\033[2K\033[1G')
    print('   \r    {0}                 '.format((progressGUI+"  "+color.END+color.BOLD+str(progress)+"% "+color.END),('')), end='\n\n\n\n')
    

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", " K", " M", " G", " T", " P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

global logTime
global logFile
logTime = str(datetime.today().strftime('%d-%m-%Y_%H-%M-%S'))

if not os.path.exists("./logs"):
    os.system("mkdir ./logs")

   
os.system("echo ULTMOS SYSTEM REPORT "+str(datetime.today().strftime('%d-%m-%Y %H:%M:%S'))+" > ./logs/SPT_"+logTime+".log")
os.system("echo ───────────────────────────────────────────────────────────────────"+" >> ./logs/SPT_"+logTime+".log")
os.system("echo This report was generated by user request, and includes basic "+" >> ./logs/SPT_"+logTime+".log")
os.system("echo information about your system hardware, as well as your current"+" >> ./logs/SPT_"+logTime+".log")
os.system("echo ULTMOS software environment. "+" >> ./logs/SPT_"+logTime+".log")
os.system("echo "+" >> ./logs/SPT_"+logTime+".log")
os.system("echo This information may help project developers"+" >> ./logs/SPT_"+logTime+".log")
os.system("echo in assisting you in any issues you might have."+" >> ./logs/SPT_"+logTime+".log")




logFile = open("./logs/SPT_"+logTime+".log", "a")

def cpydProfile(logMsg):
    entryLine = ("   "+str(logMsg)+"\n")
    logFile.write(entryLine)
cpydProfile(" ")
cpydProfile(("Name       : "+scriptName))
cpydProfile(("File       : "+script))
cpydProfile(("Identifier : "+scriptID))
cpydProfile(("Version    : "+str(scriptVer)))
cpydProfile(("Vendor     : "+scriptVendor))
cpydProfile(" ")
cpydProfile("Date       : "+str(datetime.today().strftime('%d/%m/%Y')))
cpydProfile("Time       : "+str(datetime.today().strftime('%H:%M:%S')))
cpydProfile(" \n")
progressUpdate(7)
time.sleep(2)
cpydProfile("ULTMOS")
cpydProfile("────────────────────────────────────────────────────────")
cpydProfile(("Version    : "+version))
cpydProfile(("Branch     : "+branch))
cpydProfile((" \n"))
cpydProfile("OPERATING SYSTEM")
cpydProfile("────────────────────────────────────────────────────────")

progressUpdate(16)
time.sleep(1)
cpydProfile("OS         : "+platform.system())
progressUpdate(18)
cpydProfile("Distro     : "+distro.name())
progressUpdate(24)
cpydProfile("Release    : "+distro.version())
progressUpdate(27)
cpydProfile("Kernel     : "+platform.release())
progressUpdate(29)
cpydProfile(" \n")
time.sleep(1)
progressUpdate(33)
cpydProfile("PROCESSOR")
cpydProfile("────────────────────────────────────────────────────────")
cpydProfile("Model      : "+f"{cpuinfo.get_cpu_info()['brand_raw']}")
progressUpdate(35)
cpydProfile("Pysical    : "+str(psutil.cpu_count(logical=False)))
progressUpdate(38)
cpydProfile("Logical    : "+str(psutil.cpu_count(logical=True)))
progressUpdate(41)
cpydProfile("Arch       : "+platform.machine())
progressUpdate(46)
cpydProfile(" \n")
time.sleep(1)
cpydProfile("MEMORY")
cpydProfile("────────────────────────────────────────────────────────")
svmem = psutil.virtual_memory()
progressUpdate(48)
cpydProfile("Total      : "+f"{get_size(svmem.total)}")
progressUpdate(49)
cpydProfile("Used       : "+f"{get_size(svmem.used)}")
progressUpdate(51)
cpydProfile("Free       : "+f"{get_size(svmem.free)}")
progressUpdate(53)
time.sleep(1)
logFile.close()
