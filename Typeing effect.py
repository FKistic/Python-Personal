import sys
from time import sleep

words = "Hello Friends, Chai Pelo LoL\n"
sleep(10)
while True:
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)
        
