from tkinter import *
import time


def copying():
    import os,time #importing modules
    from shutil import copy #importing modules
    index=0
    root1=Tk()
    Label(root1,text="The files with same extentions are: ")
    list1=[] #Empty list
    for root, dirs, files in os.walk(fr"{base_value.get()}", topdown=False): #Listing Directory
        for name in files:
            a=os.path.join(root, name)
            b=a
            c=str(b)
            if extention_value.get() in c: #Selecting files with same Extentions
                d=c
                list2=list1.append(f"{d}") #Appending the File path to list
                index+=1
    if index==0:#If no files are detected
        Label(root1,text=f"No files with '{extention_value.get()}' extention.").pack()
    list_len=len(list1)
    index2=0
    while index2<list_len:#Copying till end of list1
        try:
            Label(root1,text=f"{list1[index2]} | DONE! |").pack()
            copy(list1[index2],destination_value.get())
            index2+=1
        except Exception as e:
            Label(root1,text=f"Error: {e}").pack
            Label(root1,'Oppression completed with errors!').pack


def moving():
    import os,time #importing modules
    from shutil import move #importing modules
    index=0
    root1=Tk()
    Label(root1,text="The files with same extentions are: ")
    list1=[] #Empty list
    for root, dirs, files in os.walk(fr"{base_value.get()}", topdown=False): #Listing Directory
        for name in files:

            a=os.path.join(root, name)
            b=a
            c=str(b)
            if extention_value.get() in c: #Selecting files with same Extentions

                d=c
                list2=list1.append(f"{d}") #Appending the File path to list
                index+=1

    if index==0:#If no files are detected

        Label(root1,text=f"No files with '{extention_value.get()}' extention.").pack()

    list_len=len(list1)
    index2=0
    while index2<list_len:#Copying till end of list1

        try:

            Label(root1,text=f"{list1[index2]} | DONE! |").pack()
            move(list1[index2],destination_value.get())
            index2+=1

        except Exception as e:
            Label(root1,text=f"Error: {e}").pack
            Label(root1,'Oppression completed with errors!').pack


#GUI 
#GUI base

root=Tk()
root.geometry("500x250")
root.maxsize(width=500,height=250)
root.minsize(width=500,height=250)
root.title("Ext File Copier++")

#labels

f1=Label(bg="grey",text="  ").pack(side=LEFT, fill=Y)
main_lable=Label(root,bg="grey",fg="white",text="Welcome To Ext File Copier++",font="DEFALT 20 bold italic").pack(fill=X)
baspath_label=Label(root,text="Enter the Source path: ",font="times 14 bold ").place(x=12,y=60)
baspath_label=Label(root,text="Enter the Destination : ",font="times 14 bold").place(x=12,y=100)

#Values

base_value=StringVar()
destination_value=StringVar()
extention_value=StringVar()

#Entry

baspath_entry=Entry(width=40,textvariable=base_value,background="white",relief=GROOVE).place(x=215,y=68)
destination_entry=Entry(width=40,textvariable=destination_value).place(x=215,y=105)
extention_label=Label(root,text="   Enter the Extention : ",font="times 14 bold").place(x=12,y=140)
extention_entry=Entry(width=40,textvariable=extention_value).place(x=215,y=145)

#Buttons

copy_button=Button(bg="cyan3",text="COPY",padx=15,pady=10,command=copying).place(x=150,y=190)
move_button=Button(bg="cyan3",text="Move",padx=15,pady=10,command=moving).place(x=250,y=190)

#loop

root.mainloop()
