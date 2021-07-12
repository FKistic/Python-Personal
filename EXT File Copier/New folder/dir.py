import os
basepath=input("Enter the path from where files to be copied: ")
basepath=basepath.replace('\\',"/")
no=""
def full_dir(name):
    a=os.path.join(name)
    a=str(a)
    print(a)
    for entry in a:
        if os.path.isdir(os.path.join(a, entry)):
            str(entry)
            print(entry)
    a=str(a)
    print(a)
full_dir(basepath)
