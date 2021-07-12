import os,time,webbrowser
from datetime import datetime
def listdirec(dir_name):
    global l1
    global file_path,file_name,a
    file_path=[]
    file_name=[]
    for root,dir,files in os.walk(dir_name):
        for dir_name in files:
            a=os.path.join(root,dir_name)
            file_path.append(a)
            file_name.append(dir_name)
class Student_front_end:
    this_dir=os.path.dirname(os.path.realpath(__file__))
    this_dir=str(this_dir)
    this_dir_final=this_dir+'\\books'
    listdirec(this_dir_final)
    index=1
    len_list=len(file_name)
    print("Student Library")
    index=0
class Student_back_end:
    date=[]
    while True:
        for index1 in file_name:
            print(f'Use {str(Student_front_end.index)}. for {str(file_name[Student_front_end.index])} ''')
            Student_front_end.index+=1
        select=int(input(f'''Please select the Python book you want to borrow: '''))
        for i in range(1,Student_front_end.len_list+1):
            book_date=[]
            if i==select:
                webbrowser.open(file_path[select])
                now = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = now.strftime("Date: %d/%m/%Y, Time: %H:%M:%S")
                book_date_time=(f"The book {file_name[select]} is taken at", dt_string)
                book_date.append(book_date_time)
                print(book_date_time)
                del file_name[select]	
                del file_path[select]
        Student_front_end.index=0
        if input("Do you want to borrow more books: ")=='n':
            break
        print()
        print()


    
    

