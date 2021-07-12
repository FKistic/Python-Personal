import pyautogui,time
msg = input("HELLO BOT CHECK 123 : ")
T = int(input("TIMES :  "))
for i in range(T+1):
	pyautogui.typewrite(msg)
	pyautogui.press("enter")
	
