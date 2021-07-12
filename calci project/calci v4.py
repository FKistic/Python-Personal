#simple calcultor using python
name = input("Type your name here: ")
print("Hello and Welcome "+ name +"!")
print()

x = int(input("Please Type the 1st number: "))
y = int(input("Please Type the 2nd number: "))
z = int(input("Please select the opreator\nPress 1 for +, 2 for -, 3 for *, 4 for /: "))
opp = input("PRESS ENTER TO CONTINUE: ")
a = x+y
b = x-y
c = x*y
d = x/y
print()
if z==1:
    print("IF ADDED THEN ANSWER WILL BE")
    print(a)
if z==2:
    print("IF SUBTRACTED THEN THE ANSWER WILL BE")
    print(b)
if z==3:
    print("IF MULTIPLIED THEN THE ANSWER WILL BE")
    print(c)
if z==4:
    print("IF DEVIDED THEN THE ANSWER WILL BE")
    print(d)
print("Thank you "+ name +" for using this CALCULATOR LITE, LOL!!")
input("PRESS ENTER TO EXIT THE PROGRAM")

