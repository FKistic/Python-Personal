import os,shutil,sys
from time import sleep
def dot_finder(name):
    dot_finder.matches = [match for match in name if "." in match]
    dot_finder.not_matches=[item for item in name if item not in dot_finder.matches]
def dot_extfinder(name,ext):
    dot_extfinder.matches = [match for match in name if ext in match]
    dot_extfinder.not_matches=[item for item in name if item not in dot_extfinder.matches]
def dot_extention_finder(name,ext):
    preprefix, suffix, _ = name.partition(ext)
    *_, prefix = preprefix.split(",")
    with open("files_sorted.txt",'a') as files:
        files.write(f"{prefix}{suffix}/")

words = "Welcome to EXT File Copier\nThis program is made by Faraaz Kurawle.\n"
sleep(1)
for char in words:
    sleep(0.1)
    print(char, end='', flush=True)
print('''******************************************************************
Known bugs:
Your file or folder should not contain ',' '/' '\\' or this program wont work!
This program wont copy all your files with same extention but has a succes rate of 90%!

******************************************************************''')
class getDetails:
    basepath=input("Enter the path from where files to be copied: ")
    basepath=basepath.replace('\\',"/")
    destination=input("Enter the Destination: ")
    destination=destination.replace('\\',"/")
    extention=input("Eeter the extention with dot: ")
    extention=extention.replace('\\',"/")

class getDirectory(getDetails):
    confirm_sub=input("Does your path contails sub_folders? (y/n): ")
    confirm_dot=input("Does your folder and sub-folders contain '.' dot (y/n): ")
    directory=os.listdir(getDetails.basepath)
    directory=str(directory)
    directory=directory.replace('[',"")
    directory=directory.replace(']',"")
    directory=directory.replace("'","")
    directory=directory.replace(", ",",")
    if confirm_sub=='n':
        index=0
        directory=directory.split(',')
        print(f"***{directory}***")
        dot_extfinder(directory,getDetails.extention)
        print(dot_extfinder.matches)
        lennn=dot_extfinder.matches
        lennn=len(lennn)
        lenn=int(lennn)
        lennn=lennn-1
        while index<=lennn:
            final_dir=f'{getDetails.basepath}/{dot_extfinder.matches[index]}'
            print(final_dir)
            shutil.copy(final_dir,getDetails.destination)
            index+=1
    if confirm_sub=='y':
        for_sub_dir=directory.split(",")
        if confirm_dot=='n':
            dot_finder(for_sub_dir)
            not_in_matches=dot_finder.not_matches
            lenthing=len(not_in_matches)
            lenthing=int(lenthing)
            lenthing=lenthing-1
            index_for_sub=0
            while index_for_sub<lenthing:
                sub_directory=os.listdir(f'{getDetails.basepath}/{not_in_matches[index_for_sub]}')
                sub_directory=str(sub_directory)
                sub_directory=sub_directory.replace('[',"")
                sub_directory=sub_directory.replace(']',"")
                sub_directory=sub_directory.replace("'","")
                sub_directory=sub_directory.replace(", ",",")
                print(sub_directory)
                sub_directory1=f'{getDetails.basepath}/{not_in_matches[index_for_sub]}/{sub_directory}'
                print(sub_directory1)
                shutil.copy(sub_directory1,getDetails.destination)
                index_for_sub+=1
        if confirm_dot=='y':
            for entry in os.listdir(getDetails.basepath):
                if os.path.isdir(os.path.join(getDetails.basepath, entry)):
                    entry=str(entry)
                    with open("folder.txt",'a') as folder:
                        folder.write(f'{entry},')
            with open("folder.txt") as folder:
                folders=folder.read()
            folders=str(folders)
            folders=folders.split(',')
            len_folders=len(folders)
            len_folders=int(len_folders)
            len_folders=len_folders-1
            index_for_sub=0
            while index_for_sub<=len_folders:
                sub_directory=os.listdir(f'{getDetails.basepath}/{folders[index_for_sub]}')
                sub_directory=str(sub_directory)
                with open("files.txt",'a') as files:
                    files.write(f'{sub_directory}/')
                index_for_sub+=1
            with open("files.txt") as files:
                files=files.read()
            files=files.replace('[',"")
            files=files.replace(']',"")
            files=files.replace("'","")
            files=files.replace(", ",",")
            files=files.split('/')
            lenn=len(files)
            lenn=int(lenn)
            lenn=lenn-2
            index=0
            while index<=lenn:
                final_files=files[index]
                final_files1=str(final_files)
                dot_extention_finder(final_files1,getDetails.extention)
                index+=1
            with open("files_sorted.txt") as files_sort:
                files_sorted=files_sort.read()
            files_sorted=str(files_sorted)
            print(files_sorted)
            files_sorted=files_sorted.split('/')
            print(files_sorted)
            index=0
            index_for_sub=0
            while index<=lenn:
                final_files=files[index]
                final_sub_directory=f'{getDetails.basepath}/{folders[index_for_sub]}/{files_sorted[index]}'
                print(final_sub_directory)
                shutil.copy(final_sub_directory,getDetails.destination)
                index_for_sub+=1
                index+=1
    with open("files.txt",'w') as files:
        files.write("")
    with open("folder.txt",'w') as files1:
        files1.write('')
    with open("files_sorted.txt",'w') as files11:
        files11.write('')
    print('Coping Done!')       
    input('Press Enter to exit')