from tkinter import *
from time import sleep
def Register():
    scr=Tk()
    scr.title("Janta Restaurant")
    scr.geometry("1366x768")
    scr.resizable(False, False)
    fr=Frame(scr,height=150,width=1366)
    logo=PhotoImage(file="../logo.PNG")
    ba=Label(fr,image=logo,height=150).place(x=0,y=0)
    home=Button(fr,text="Home",bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
    home.place(x=800,y=100)
    adlog=Button(fr,text="Administrator Login",cursor="hand2",bg="#0b1335",fg="white",font=("default",16))
    adlog.place(x=950,y=100)
    about=Button(fr,text="About Us",bg="#0b1335",cursor="hand2",fg="white",font=("default",16))
    about.place(x=1210,y=100)
    fr.pack(fill=BOTH,expand=1)
    
    fr1=Frame(scr,height=618,width=1366)
    c=Canvas(fr1,height=618,width=1366)
    c.pack()
    logo1=PhotoImage(file="../pizzamain.png")
    c.create_image(683,309,image=logo1)
    c.create_rectangle(50,50,1316,550,fill="#d3ede6",outline="white",width=6)
    log=Label(fr1,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
    log.place(x=480,y=60)
    c.create_text(250,120,text="General Information",fill="#000000",font=("Cooper Black",24))
    lab1=Label(fr1,text="FirstName",bg="#d3ede6",font=("cooper black",22))
    lab1.place(x=90,y=150)
    first=Entry(fr1,bg="white",font=("cooper black",22),bd=5)
    first.place(x=290,y=150)
    lab2=Label(fr1,text="LastName",bg="#d3ede6",font=("cooper black",22))
    lab2.place(x=730,y=150)
    last=Entry(fr1,bg="white",font=("cooper black",22),bd=5)
    last.place(x=920,y=150)
    lab3=Label(fr1,text="Email",bg="#d3ede6",font=("cooper black",22))
    lab3.place(x=90,y=250)
    email=Entry(fr1,bg="white",font=("cooper black",22),bd=5)
    email.place(x=290,y=250)
    lab4=Label(fr1,text="Password",bg="#d3ede6",font=("cooper black",22))
    lab4.place(x=730,y=250)
    pasd=Entry(fr1,bg="white",font=("cooper black",22),bd=5)
    pasd.place(x=920,y=250)
    lab5=Label(fr1,text="Mobile No.",bg="#d3ede6",font=("cooper black",22))
    lab5.place(x=90,y=350)
    mob=Entry(fr1,bg="white",font=("cooper black",22),bd=5)
    mob.place(x=290,y=350)
    bc=Button(fr1,text="Back",cursor="hand2",fg="white",bg="#0b1335",font=("cooper black",26),bd=5)
    bc.place(x=360,y=450)
    rg=Button(fr1,text="Register",cursor="hand2",fg="white",bg="#0b1335",font=("cooper black",26),bd=5)
    rg.place(x=630,y=450)
    cl=Button(fr1,text="Clear",cursor="hand2",fg="white",bg="#0b1335",font=("cooper black",26),bd=5)
    cl.place(x=900,y=450)
    fr1.pack(fill=BOTH,expand=1)
    scr.mainloop()

if __name__=="__main__":
    X=Register()