from translate import Translator
from playsound import playsound
import os, subprocess, sys, shutil
from gtts import gTTS



def get_version():
    try:
        return open(".version","r").read().strip()
    except:
        return '5.5'
def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def bann_text():
    clr()
    logo="""
████████╗██╗  ██╗ █████╗ ██╗  ██╗██╗   ██╗██████╗   
╚══██╔══╝██║  ██║██╔══██╗██║ ██╔╝██║   ██║██╔══██╗  
   ██║   ███████║███████║█████╔╝ ██║   ██║██████╔╝  
   ██║   ██╔══██║██╔══██║██╔═██╗ ██║   ██║██╔══██╗  
   ██║   ██║  ██║██║  ██║██║  ██╗╚██████╔╝██║  ██║  
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         
     """
    version="Version: "+__VERSION__
    contributors="MADE BY: "+" ".join(__CONTRIBUTOR__)
    print(logo)
    
  
    
def do_zip_update():
    success=False

    # Download Zip from git
    # Unzip and overwrite the current folder

    if success:
        mesgdcrt.SuccessMessage("Thakurx was updated to the latest version")
        mesgdcrt.GeneralMessage("Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update Thakurx.")
        mesgdcrt.WarningMessage("Grab The Latest one From https://github.com/Hackersthakur/THAKURX.git")

    sys.exit()

def do_git_update():
    success=False
    try:
        print(ALL_COLORS[0]+"UPDATING "+RESET_ALL,end='')
        process = subprocess.Popen("git checkout . && git pull ", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while process:
            print(ALL_COLORS[0]+'.'+RESET_ALL,end='')
            time.sleep(1)
            returncode = process.poll()
            if returncode is not None:
                break
        success = not process.returncode
    except:
        success = False
    print("\n")

    if success:
        mesgdcrt.SuccessMessage("Thakurx was updated to the latest version")
        mesgdcrt.GeneralMessage("Please run the script again to load the latest version")
    else:
        mesgdcrt.FailureMessage("Unable to update Thakurx.")
        mesgdcrt.WarningMessage("Make Sure To Install 'git' ")
        mesgdcrt.GeneralMessage("Then run command:")
        print("git checkout . && git pull https://github.com/Hackersthakur/THAKURX HEAD")
    sys.exit()

def update():
    if shutil.which('git'):
        do_git_update()
    else:
        do_zip_update()
def check_for_updates():
    mesgdcrt.SectionMessage("Checking for updates")
    fver = requests.get("https://raw.githubusercontent.com/Hackersthakur/THAKURX/main/.version").text.strip()
    if fver != __VERSION__:
        mesgdcrt.WarningMessage("An update is available")
        mesgdcrt.GeneralMessage("Starting update...")
        update()
    else:
        mesgdcrt.SuccessMessage("THAKURX is up-to-date")
        mesgdcrt.GeneralMessage("Starting THAKURX\n")
        
 
 
if sys.version_info[0]!=3:
    mesgdcrt.FailureMessage("THAKURX will work only in Python v3")
    sys.exit()




__VERSION__ = get_version()
__CONTRIBUTOR__ = ['HACKERSTHAKUR']



description="""THAKURBOMBER - Your Friendly Spammer Application

THAKURBOMBERcan be used for many purposes which incudes - 
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

THAKURBOMBER is not intented for malicious uses.
""" 


clr()
bann_text()

text = input("enter text : " )
files = text



audio = files + ".m4a"

ts = text
language ="hi"
shu = gTTS(text=ts,lang=language,slow=False)
print(ts)
shu.save(audio)
playsound(audio)
