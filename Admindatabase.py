from sqlite3 import *
from tkinter import messagebox
db=connect("pizza.db")
cur=db.cursor()
try:
    cur.execute("create table employee(name varchar(50) not null,empid int not null, username varchar(50) not null,password varchar(50) not null)")
except:
    pass
while(True):
    b=input("Employee Id(xxxx-xxxxx) : ")
    a=input("Employee name : ")
    c=input("Username : ")
    d=input("Password : ")
    q1=""
    for i in a.split():
        q1=q1+i
    q2=b.split("-")
    try:
        if q2[0].isdigit()!=True or q2[1].isdigit()!=True:
            print("Enter Valid Employee Id")
    except:
        print("Enter Valid Formatted Employee Id")
    if q1.isalpha()!=True :
        print("Name must contain alphabat only")
    elif c[0].isupper()!=True or c.split()[0]!=c:
        print("First letter must be Uppercase and No space is Allowed")
    elif len(d)<6:
        print("Password must be of minimum 6 letter")
    else:
        cur.execute("insert into employee values(%r,%r,%r,%r)"%(a.capitalize(),b,c,d))
        if input("Press 1 to add more data \nOtherwise press any other key")!="1":
            break
db.commit()
