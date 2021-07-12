#simple calcultor using python
import time
time.sleep(1)
print('''||||||||    //\\\    ||      |||||||| ||   || ||        //\\\   |||||||||| |||||||| ||||||\\''')
time.sleep(1)
print('''||         //  \\\   ||      ||       ||   || ||       //  \\\      ||     ||    || ||    ||''')
time.sleep(1)
print('''||        //====\\\  ||      ||       ||   || ||      //====\\\     ||     ||    || ||||||/''')
time.sleep(1)
print('''|||||||| //      \\\ ||||||| |||||||| ||||||| |||||| //      \\\    ||     |||||||| ||   \\\\''')
time.sleep(2)
print("MADE BY FARAAZ!")
name = input("Type your name here: ")
print("Hello and Welcome "+ name +"!")
print()
x = int(input("Please Type the 1st number: "))
y = int(input("Please Type the 2nd number: "))
z = int(input('''What operator you want to use?
Press 1 for +, 
      2 for -, 
      3 for *, 
      4 for /: '''))
a = x+y
b = x-y
c = x*y
d = x/y
if z==3:
      print("IF MULTIPLIED THEN THE ANSWER WILL BE")
      print(c)
if z==1:
      print("IF ADDED THEN ANSWER WILL BE")
      print(a)
if z==2:
      print("IF SUBTRACTED THEN THE ANSWER WILL BE")
      print(b)
if z==4:
      print("IF DEVIDED THEN THE ANSWER WILL BE")
      print(d)
print()
print("Thank you "+ name +" for using this CALCULATOR LITE, LOL!!")
if input("Do you want to repeat (y/n): ") =='n':
      exit()
while True:
            x = int(input("Please Type the 1st number: "))
            y = int(input("Please Type the 2nd number: "))
            z = int(input('''What operator you want to use?
            Press 1 for +,
                  2 for -, 
                  3 for *, 
                  4 for /: '''))
            a = x+y
            b = x-y
            c = x*y
            d = x/y
            if z==3:
                  print("IF MULTIPLIED THEN THE ANSWER WILL BE")
                  print(c)
            if z==1:
                  print("IF ADDED THEN ANSWER WILL BE")
                  print(a)
            if z==2:
                  print("IF SUBTRACTED THEN THE ANSWER WILL BE")
                  print(b)
            if z==4:
                  print("IF DEVIDED THEN THE ANSWER WILL BE")
                  print(d)
            print()
            print("Thank you "+ name +" for using this CALCULATOR LITE, LOL!!")
            if input("Do you want to repeat (y/n): ") =='n':
                  break
print('''HOPE TO SEE YOU AGAIN,
SEE YA''')
input("Press ENTER to exit this program: ")
