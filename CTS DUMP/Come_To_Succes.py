import pickle,pyautogui,time,webbrowser
import getpass
USER_NAME = getpass.getuser()#to get user name
print("Come to Salah, Come to succes")
print("This program is made by Faraaz Kurawle")
print('''This program is made to notify you about salah timings
Different modes in this programs are:
1. Easy mode - ONLY NOTIFICATIONS AND ALERTS.
2. Mediam mode - FULL SCREEN NOTIFICATION WITH TIMER
3. Hard mode - This mode will remind you 5 mins before the azan time to let yousave all your work, AND WILL SHUT DOWN THE COMPUTER AT AZAN TIME!.
NOTE:- use 1,2,3 only!''')
mode= int(input("Which mode you want to chose: "))#To save the mode
with open("mode.txt", "wb" ) as mymode:
    pickle.dump(mode, mymode)
path=input("Please Enter the path where you have extracted this programs: ")
path=path.replace("\\","/")
with open("path.txt", "wb" ) as mypath:#To save the path
    pickle.dump(path, mypath)
with open("path.txt", "rb" ) as mypath:#to open the path
    path1 = pickle.load(mypath)
if input('Have opened this program for the first time?(y/n)?: ')=='y':
    print("Oh,ok so now this program make it self to run at start up")#From Here it use pyautogui to copy and paste the mode_selector file along with mode.txt and path.txt
    file_path=path1
    start_path="C:\\Users\\use\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    start_path=start_path.replace('use',USER_NAME)
    webbrowser.open(file_path+"/startup!")
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('ctrl','w')
    time.sleep(2)
    webbrowser.open(start_path)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('ctrl','w')
from subprocess import call
call(["python",path1+"/mode_selector.py"])