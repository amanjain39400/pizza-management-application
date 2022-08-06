from tkinter import *
import random
import time
def Orderde():
    scr=Tk()
    scr.title("Janta Restaurant")
    scr.geometry("1366x768")
    #scr.resizable(False, False)
    fr=Frame(scr,height=150,width=1366)
    c=Canvas(fr,height=150,width=1366)
    c.pack()
    logo=PhotoImage(file="../logo.PNG")
    c.create_image(683,75,image=logo)
    home=Button(fr,text="Home",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
    home.place(x=1000,y=90)
    localtime=time.asctime(time.localtime(time.time()))
    c.create_text(1000,50,text=localtime,fill="white",font=("default",16))
    fr.pack(fill=BOTH,expand=1)
    f1=Frame(scr,height=618,width=1366)
    
    c=Canvas(f1,height=618,width=1366)
    c.pack()
    logo1=PhotoImage(file="../pizzamain.png")
    c.create_image(683,309,image=logo1)
    log=Label(f1,text="YOUR ORDER",bg="#9db1f2",font=("Cooper Black",22))
    log.place(x=450,y=4)
    c.create_rectangle(230, 50, 800, 500,fill="#d3ede6",outline="white",width=6)
    amt=1000
    l=Frame(c,height=450,width=570)
    l.place(x=285,y=250)

    vsbar = Scrollbar(f1, orient=VERTICAL, command=c.yview)
    vsbar.place(x=780,y=55)
    c.configure(yscrollcommand=vsbar.set)

    hsbar = Scrollbar(f1, orient=HORIZONTAL, command=c.xview)
    hsbar.place(x=235,y=480)
    c.configure(xscrollcommand=hsbar.set)

    c.configure(scrollregion=l, width=570, height=450)
    
    text="Total : "+str(amt)
    tot=Label(f1,text=text,bg="#f2da9d",width=12,font=("Cooper Black",22))
    tot.place(x=900,y=250)
    pay=Button(f1,text="Pay",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
    pay.place(x=900,y=300)
    exi=Button(f1,text="Exit",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
    exi.place(x=1070,y=300)

    f1.pack(fill=BOTH,expand=1)
    scr.mainloop()


if __name__=="__main__":
    x=Orderde()
