import pyautogui, time, datetime, os
msg = input("Please type the texr: ")
n = input("how much times ? :")
time.sleep(5)

while True:
	
	# to display the time at which the message is sent
	print(datetime.datetime.now())
	for i in range(0,int(n)):
                pyautogui.typewrite(msg + '\n')
	time.sleep(0)


