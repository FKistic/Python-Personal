def list_large(a):
    print(f"The list is {a}")
    b=a.sort()
    b=a.reverse()
    print(f"The largest number in the above list is {a[0]}")
def large(num1,num2,num3):
    if (num1>num3):
        if (num1>num2):
            print(num1)
        else:
            print(num2)
    else:
        if (num3>num2):
            if (num3>num1):
                print(num3)