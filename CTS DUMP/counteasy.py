import pyautogui,pickle,time,webbrowser,getpass
from countdown import countdown
with open("path.txt", "rb" ) as mypath:
    path1 = pickle.load(mypath)
print("Please go and pray, next command will execute after 10 mins\nDO NOT CLOSE THIS WINDOW!")
time.sleep(600)
pyautogui.alert(text='I hope you have prayed?', title='Come To Succes', button='Yess!,i have prayed')
cmd_path="C:/Users/username/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk"
user=getpass.getuser()
cmd_path=cmd_path.replace("username",user)
time.sleep(1)
webbrowser.open(cmd_path)
time.sleep(1)
pyautogui.typewrite('cd "'+path1+'"')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite("start mode_selector.py")
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite('exit')
time.sleep(1)
pyautogui.press('enter')
