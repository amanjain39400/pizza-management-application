from tkinter import *
import time
def Login():
    scr=Tk()
    scr.title("Janta Restaurant")
    scr.geometry("1366x768")
    #scr.resizable(False, False)
    fr=Frame(scr,height=150,width=1366)
    logo=PhotoImage(file="../logo.PNG")
    ba=Label(fr,image=logo,height=150).place(x=0,y=0)
    home=Button(fr,text="Home",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
    home.place(x=800,y=100)
    adlog=Button(fr,text="Administrator Login",cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
    adlog.place(x=925,y=100)
    about=Button(fr,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
    about.place(x=1210,y=100)
    localtime=time.asctime(time.localtime(time.time()))
    tim=Label(fr,text=localtime,fg="white",font=("default",16),bg="#0b1335")
    tim.place(x=925,y=50)
    fr.pack(fill=BOTH,expand=1)
    fr1=Frame(scr,height=618,width=1366)
    c=Canvas(fr1,height=618,width=1366)
    c.pack()
    logo1=PhotoImage(file="../pizzamain.png")
    c.create_image(683,309,image=logo1)
    c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
    log=Label(fr1,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("cooper black",27))
    log.place(x=59,y=105)
    lab1=Label(fr1,text="UserName",bg="#d3ede6",font=("cooper black",22))
    lab1.place(x=100,y=180)
    user=Entry(fr1,bg="white",font=("cooper black",22),bd=6 ,justify='right')
    user.place(x=320,y=180)
    lab2=Label(fr1,text="Password",bg="#d3ede6",font=("cooper black",22))
    lab2.place(x=105,y=250)
    pasd=Entry(fr1,bg="white",font=("cooper black",22),bd=6 ,justify='right')
    pasd.place(x=320,y=250)
    lg=Button(fr1,text="Login",cursor="hand2",fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
    lg.place(x=180,y=320)
    cl=Button(fr1,text="Clear",cursor="hand2",fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
    cl.place(x=450,y=320)
    rg=Button(fr1,text="New to Cafe 96",fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",20),bd=6)
    rg.place(x=200,y=390)
    c.create_rectangle(850,120,1310,480,fill="#d3ede6",outline="white",width=4)
    ext=PhotoImage(file="../p4.png")
    url=Label(fr1,image=ext,cursor="hand2").place(x=855,y=125)
    fr1.pack(fill=BOTH,expand=1)
    scr.mainloop()

if __name__=="__main__":
    X=Login()
    
    #0b1335
