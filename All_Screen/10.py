from tkinter import *
import random
import time
def Address():
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
    log=Label(f1,text="SPECIALTY CHICKEN",bg="#9db1f2",font=("Cooper Black",22))
    log.place(x=540,y=4)
    c.create_rectangle(400, 40, 966, 420,fill="#d3ede6",outline="white",width=6)
    # pizza 1
    c.create_rectangle(405, 50, 960, 170,width=2)
    delu=PhotoImage(file="../roasted.png")
    c.create_image(470,110,image=delu)
    c.create_text(650,80,text="Roasted Chicken",fill="#000000",font=("Cooper Black",20))
    c.create_text(875,80,text="₹109",fill="#ff3838",font=("default",17,'bold'))
    c.create_text(590,120,text="Quantity : ",fill="#000000",font=("default",12))
    qty1=Entry(f1,bg="#aae2d7",font=("default",12),width=4,)
    qty1.place(x=650,y=110)
    add1=Button(f1,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
    add1.place(x=850,y=120)
    #pizza 2
    c.create_rectangle(405, 170, 960, 290,width=2)
    vag=PhotoImage(file="../chicken-meatballs.jpg")
    c.create_image(470,230,image=vag)
    c.create_text(650,200,text="Chicken Meatballs",fill="#000000",font=("Cooper Black",20))
    c.create_text(875,200,text="₹99",fill="#ff3838",font=("default",17,'bold'))
    c.create_text(590,240,text="Quantity : ",fill="#000000",font=("default",12))
    qty2=Entry(f1,bg="#aae2d7",font=("default",12),width=4,)
    qty2.place(x=650,y=230)
    add2=Button(f1,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
    add2.place(x=850,y=240)
    #pizza 3
    c.create_rectangle(405, 290, 960, 410,width=2)
    pep=PhotoImage(file="../Boneless-Chicken-wings-192x192.png")
    c.create_image(470,350,image=pep)
    c.create_text(650,320,text="Boneless Chicken",fill="#000000",font=("Cooper Black",20))
    c.create_text(875,320,text="₹139",fill="#ff3838",font=("default",17,'bold'))
    c.create_text(590,360,text="Quantity : ",fill="#000000",font=("default",12))
    qty3=Entry(f1,bg="#aae2d7",font=("default",12),width=4,)
    qty3.place(x=650,y=350)
    add3=Button(f1,text="ADD",bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
    add3.place(x=850,y=360)

    con=Button(f1,text="Confirm Order",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
    con.place(x=600,y=430)
    more=Button(f1,text="Add More..",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
    more.place(x=630,y=500)
    f1.pack(fill=BOTH,expand=1)
    scr.mainloop()

if __name__=="__main__":
    x=Address()
