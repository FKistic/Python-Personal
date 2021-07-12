# Function to list only one directory
def list_one_dir(name,ext):
    import os,time,shutil
    list1=[]
    print("The files in current directory are: ")
    for files in os.listdir(name):
        if ext in files:
            list1.append(files)
    sel=input("Select the mode:\n1. Copy\n2. Move ")
    if sel==1:
        for i in list1:
            try:
                shutil.copy(list1[i],getDetails.destination)
            except Exception as e:
                print(e)
                print("Opression Completed with errors.")
            print("Done!")
    if sel==2:
        for i in list1:
            try:
                shutil.move(list1[i],getDetails.destination)
            except Exception as e:
                print(e)
                print("Opression Completed with errors.")
            print("Done!")
#Function to Copy
def copying(name,ext):
    import os,time #importing modules
    from shutil import copy #importing modules
    index=0
    print("The files with same extentions are: ")
    list1=[] #Empty list
    for root, dirs, files in os.walk(fr"{name}", topdown=False): #Listing Directory
        for name in files:
            a=os.path.join(root, name)
            b=a
            c=str(b)
            if ext in c: #Selecting files with same Extentions
                d=c
                list2=list1.append(f"{d}") #Appending the File path to list
                index+=1
    if index==0:#If no files are detected
        print(f"No files with '{ext}' extention.")
    list_len=len(list1)
    index2=0
    while index2<list_len:#Copying till end of list1
        try:
            time.sleep(1)
            print(f"{list1[index2]} | DONE! |")
            copy(list1[index2],getDetails.destination)
            index2+=1
        except Exception as e:
            print(f"Error: {e}")
            print('Oppression completed with errors!')
    input("Press Enter to exit...")
# Function to Paste
def moveing(name,ext):
    import os,time
    from shutil import move
    index=0
    print("The files with same extentions are: ")
    list1=[]
    for root, dirs, files in os.walk(fr"{name}", topdown=False):
        for name in files:
            a=os.path.join(root, name)
            b=a
            c=str(b)
            if ext in c:
                global d
                d=c
                list2=list1.append(f"{d}")
                index+=1
    if index==0: 
        print(f"No files with '{ext}' extention.")
    list_len=len(list1)
    index2=0
    while index2<list_len:
        try:
            time.sleep(1)
            print(f"{list1[index2]} | DONE! |")
            move(list1[index2],getDetails.destination)
            index2+=1
        except Exception as e:
            print(f"Error: {e}")
            print('Oppression completed with errors!')
    input("Press Enter to exit...")

if __name__=='__main__':
#To take file details
    class getDetails:
        basepath=input("Enter the path from where files to be copied: ")
        basepath=basepath.replace('\\',"\\")
        destination=input("Enter the Destination: ")
        destination=destination.replace('\\',"\\")
        extention=input("Enter the extention with dot: ")
    #Applying the details and Processing the Function
    class Process:
        mode1=input("Please select the method:\n1. Search Only in the main directory\n2. Search Whole Directory: ")
        if mode1==1:
            list_one_dir(getDetails.basepath,getDetails.extention)
        else:
            mode=input("Please select the method:\n1. copy\n2. move: ")
            if mode=='copy':
                #Calling function
                copying(getDetails.basepath,getDetails.extention)
            if mode=='move':
                #Calling function
                moveing(getDetails.basepath,getDetails.extention)