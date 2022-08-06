from tkinter import *
import time
from time import*
from sqlite3 import *
from tkinter import messagebox
import re
import itertools
import os
import shutil
import threading
from PIL import Image, ImageTk
class Pizza:
    cartlist=[]
    orderlist=[]
    amount=0
    money=0
    s=0
    tt=0
    sc=Tk()
    sc.geometry("1366x768")
    sc.title("Janta Restaurant")
    sc.iconbitmap('p.ico')
    scr=Frame(sc)
    scr.pack()
##    sc.resizable(False, False)
   
#--  page 1------
    def main(sf):
##        try:
##            sf.scr.destroy()
##            sf.scr=Tk()
##        except:
##            try:
##                sf.scr=Tk()
##            except:
##                pass
##
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="./logo1.png")
        sf.l=Label(sf.f1,image=sf.logo)
        sf.l.place(x=0,y=0)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.back=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,284,image=sf.back)
        sf.lab=Button(sf.f2,text= "Click Here to enter the World of Pizzas",command=lambda:sf.Login(),cursor="hand2", bd=10 ,font=("cooper black",30, 'bold'),fg="white",bg="#0b1335")
        sf.lab.place(x=250,y=250)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#------ page 2------
    def Login(sf):
        sf.cartlist=[]
        sf.amount=0
        sf.s=""
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="logo.PNG")
        sf.ba=Label(sf.f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.f1,text="Home",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=750,y=90)
        sf.adlog=Button(sf.f1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=880,y=90)
        sf.abt=Button(sf.f1,text="About Us",bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.abt.config(command=lambda:sf.about())
        sf.abt.place(x=1155,y=90)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.tim=Label(sf.f1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        #sf.tim.place(x=925,y=50)
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=870,y=25)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)
        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50,100,700,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.f2,text="LOGIN",fg="white",bg="#0b1335",width=26,font=("cooper black",27))
        sf.log.place(x=59,y=105)
        sf.lab1=Label(sf.f2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=100,y=180)
        sf.user=Entry(sf.f2,bg="white",font=("cooper black",22),bd=6 ,justify='left')
        sf.user.place(x=320,y=180)
        sf.lab2=Label(sf.f2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=105,y=250)
        sf.pasd=Entry(sf.f2,bg="white",show="*",font=("cooper black",22),bd=6 ,justify='left')
        sf.pasd.place(x=320,y=250)
        sf.lg=Button(sf.f2,text="Login",cursor="hand2",command=lambda:sf.logindatabase(),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.lg.place(x=180,y=320)
        def clear(sf):
            sf.user.delete(0,END)
            sf.pasd.delete(0,END)
        sf.cl=Button(sf.f2,text="Clear",cursor="hand2",command=lambda:clear(sf),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        sf.cl.place(x=450,y=320)
        sf.rg=Button(sf.f2,text="New to Janta Restaurant",command=lambda:sf.Register(),fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",18),bd=6)
        sf.rg.place(x=200,y=390)
        sf.c.create_rectangle(840,90,1310,460,fill="#d3ede6",outline="white",width=4)
        frame=Frame(sf.c)
        frame.place(x=850,y=100)
        sf.ext=PhotoImage(file="p0.png")
        sf.c.create_image(1075,275,image=sf.ext)
        def update_image_file(dst):
            TEST_IMAGES = 'p0.png','p1.png', 'p2.png', 'p3.png', 'p4.png','p5.png', 'p6.png', 'p7.png', 'p8.png','p9.png'
            for src in itertools.cycle(TEST_IMAGES):
                shutil.copy(src, dst)
                time.sleep(1)
        def refresh_image(canvas, img, image_path, image_id):
            try:
                pil_img = Image.open(image_path).resize((450,350), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(pil_img)
                canvas.itemconfigure(image_id, image=img)
            except IOError: 
                img = "p1.png"
            finally:
                canvas.after(1500, refresh_image, canvas, img, image_path, image_id)
        try:
            #sf.ext=PhotoImage(file="p9.png")
            image_path = 'test.png'
            th = threading.Thread(target=update_image_file, args=(image_path,))
            th.daemon = True
            th.start()
            while not os.path.exists(image_path):
                time.sleep(0)
            canvas =Canvas(frame, height=350, width=450)
            img=None
            image_id = canvas.create_image(225, 175, image=img)
            canvas.pack()
            refresh_image(canvas, img, image_path, image_id)
        except:
            #sf.ext=PhotoImage(file="p0.png")
            sf.c.create_image(1075,275,image=sf.ext)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultlog(sf):
        sf.loguser=sf.user.get()
        sf.logpass=sf.pasd.get()
        return sf.loguser,sf.logpass
    

    def about(sf):
        sf.scr1=Toplevel()
        sf.scr1.title("Janta Restaurant")
        sf.scr1.geometry("1066x568")
        sf.scr1.configure(background='black')
        sf.L=Label(sf.scr1,text="Janta Restaurant ",font=("cooper black",22),bg = "#a854a1")
        sf.L2=Label(sf.scr1,text="Newly Opened Pizza Shop",font=("ariel",20),bg = "#a854a1")
        sf.L.pack()
        sf.L2.pack()
        sf.lo=PhotoImage(file="de.png")
        sf.ff1=Frame(sf.scr1,height=200,width=1066,bg="black")
        sf.ff1.pack()
        sf.lap=Label(sf.ff1,image=sf.lo)
        sf.lap.place(x=325,y=25)
        sf.explanation = """Aman Jain"""
        sf.w2 = Label(sf.ff1, 
              justify=CENTER,
              padx = 10, 
              text=sf.explanation,font="Helvetica 20 bold italic",fg = "red",).place(x=500,y=40)
        sf.L4=Label(sf.scr1,text="\nGUI based Project\n Pizza Management system which work same as you\nfind in the webpages to order some food online.\n",font=("ariel",20),bg = "#d3ede6")
        sf.L4.pack()
        sf.L3=Label(sf.scr1,text="Created By :- AMAN JAIN",font="Helvetica 20 bold italic",fg = "light green",
		 bg = "dark green")
        sf.L3.pack()
        sf.scr1.mainloop()
#--  page 3------
    def Adminlogin(sf):
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.home=Button(sf.f1,text="Home",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",20,'bold'))
        sf.home.place(x=1110,y=50)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(1000,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=780,y=60)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)
        sf.f2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(350,100,1016,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.f2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("cooper black",27))
        sf.log.place(x=357,y=110)
        sf.lab1=Label(sf.f2,text="UserName",bg="#d3ede6",font=("cooper black",22))
        sf.lab1.place(x=400,y=200)
        sf.usera=Entry(sf.f2,bg="white",font=("cooper black",22),bd=5)
        sf.usera.place(x=650,y=200)
        sf.lab2=Label(sf.f2,text="Password",bg="#d3ede6",font=("cooper black",22))
        sf.lab2.place(x=405,y=270)
        sf.pasda=Entry(sf.f2,bg="white",show="*",font=("cooper black",22),bd=5)
        sf.pasda.place(x=650,y=270)
        sf.lg=Button(sf.f2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.admindatabase(),font=("copper black",20,'bold'),bd=5)
        sf.lg.place(x=650,y=350)
        sf.cl=Button(sf.f2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Login(),font=("copper black",20,'bold'),bd=5)
        sf.cl.place(x=400,y=350)
        def clear(sf):
            sf.usera.delete(0,END)
            sf.pasda.delete(0,END)
        sf.rg=Button(sf.f2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(sf),bd=5,font=("copper black",20,'bold'))
        sf.rg.place(x=900,y=350)
        
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def resultadmin(sf):
        sf.loguser=sf.usera.get()
        sf.logpass=sf.pasda.get()
        return sf.loguser,sf.logpass

#--  page 4------
    def Register(sf):
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.logo=PhotoImage(file="logo.PNG")
        sf.ba=Label(sf.f1,image=sf.logo,height=150).place(x=0,y=0)
        sf.home=Button(sf.f1,text="Home",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",bd=4,fg="white",font=("cooper black",16))
        sf.home.place(x=750,y=90)
        sf.adlog=Button(sf.f1,text="Administrator Login",command=lambda:sf.Adminlogin(),cursor="hand2",bd=4,bg="#0b1335",fg="white",font=("cooper black",16))
        sf.adlog.place(x=880,y=90)
        sf.abt=Button(sf.f1,text="About Us",command=lambda:sf.about(),bg="#0b1335",cursor="hand2",fg="white",font=("cooper black",16))
        sf.abt.place(x=1155,y=90)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.tim=Label(sf.f1,text=sf.localtime,fg="white",font=("default",16),bg="#0b1335")
        #sf.tim.place(x=925,y=50)
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=870,y=25)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)
        
        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.log=Label(sf.f2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
        sf.log.place(x=480,y=120)
        sf.lab1=Label(sf.f2,text="FirstName",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)
        sf.first=Entry(sf.f2,bg="white",width=15,font=("cooper black",18,'bold'),bd=5)
        sf.first.place(x=430,y=200)
        sf.lab2=Label(sf.f2,text="LastName",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200)
        sf.last=Entry(sf.f2,bg="white",width=15,font=("cooper black",18,'bold'),bd=5)
        sf.last.place(x=920,y=200)
        sf.lab3=Label(sf.f2,text="Username",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250)
        sf.usern=Entry(sf.f2,bg="white",width=15,font=("cooper black",18,'bold'),bd=5)
        sf.usern.place(x=430,y=250)
        sf.lab4=Label(sf.f2,text="Password",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250)
        sf.passd=Entry(sf.f2,bg="white",show="*",width=15,font=("cooper black",18,'bold'),bd=5)
        sf.passd.place(x=920,y=250)
        sf.lab5=Label(sf.f2,text="Email",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300)
        sf.email=Entry(sf.f2,bg="white",width=15,font=("cooper black",18,'bold'),bd=5)
        sf.email.place(x=430,y=300)
        sf.lab6=Label(sf.f2,text="Mobile No.",bg="#d3ede6",font=("cooper black",18))
        sf.lab6.place(x=730,y=300)
        sf.mob=Entry(sf.f2,bg="white",width=15,font=("cooper black",18),bd=5)
        sf.mob.place(x=920,y=300)
        sf.bc=Button(sf.f2,text="Back",cursor="hand2",command=lambda:sf.Login(),fg="white",bg="#0b1335",font=("cooper black",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.f2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=lambda:sf.Regdatabase(),font=("cooper black",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.usern.delete(0,END)
            sf.passd.delete(0,END)
            sf.first.delete(0,END)
            sf.last.delete(0,END)
            sf.email.delete(0,END)
            sf.mob.delete(0,END)
        sf.cl=Button(sf.f2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(sf),font=("cooper black",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
    def resultreg(sf):
        sf.reguser=sf.usern.get()
        sf.regpasd=sf.passd.get()
        sf.firstname=sf.first.get()
        sf.lastname=sf.last.get()
        sf.Email=sf.email.get()
        sf.Mob=sf.mob.get()
        return sf.reguser,sf.regpasd,sf.firstname,sf.lastname,sf.Email,sf.Mob

#--  page 5------
    def adminmain(sf,username):
##        sf.scr.destroy()
##        sf.scr = Tk()
##        #sf.scr.configure(background='#f2e8b8')
##        #sf.scr.config(bg="#f2e8b8")
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()

        sf.f1=Frame(sf.scr,bg="#f2e8b8",height=200,width=1366)
        sf.f1.pack(side=TOP,fill=BOTH)
        sf.c=Canvas(sf.f1,height=150,bg="#f2e8b8",width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo2.png")
        sf.c.create_image(683,50,image=sf.logo)
        sf.c.create_text(850,80,text="WELCOME : ",fill="white",font=("default",18))
        sf.name=username
        sf.c.create_text(1000,80,text=sf.name,fill="white",font=("default",18))
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(930,40,text=sf.localtime,fill="white",font=("default",20))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=780,y=20)
        sf.tick()
        
        
        sf.c.create_text(683,125,font=( 'Cooper Black' ,25, 'bold','underline' ),text="Management System")
        sf.out=Button(sf.f1,text="Log Out",bg="#0b1335",cursor="hand2",command=lambda:sf.Adminlogin(),fg="white",bd=5,font=("default",16,'bold'))
        sf.out.place(x=1150,y=40)
        a1,a2,a3,a4,a5,a6,a7,a8=0,0,0,0,0,0,0,0
        
        def Ref(sf):
            sf.con=connect("pizza.db")
##            sf.x=random.randint(100, 500)
##            sf.randomRef = str(sf.x)
            sf.cur=sf.con.cursor()
            try:
                 sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                 sf.con.commit()
            except:
                pass
            x=sf.cur.execute("select count(*) from orderdetail")
            ordno=list(x)[0][0]+1
            sf.order.set(ordno)

            sf.v1=sf.vp1.get()
            if sf.v1=="Medium":
                sf.a1=sf.Deluxe_Veggie.get()
                if not sf.a1.isdigit():
                    if sf.a1=="":
                        sf.a1=0
                        sf.p1=float(sf.a1)*450
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Deluxe_Veggie.set("0")
                else:
                    sf.p1=float(sf.a1)*450
            elif sf.v1=="Large":
                sf.a1=sf.Deluxe_Veggie.get()
                if not sf.a1.isdigit():
                    #sf.Deluxe_Veggie.set("0")
                    if sf.a1=="":
                        #sf.Deluxe_Veggie.set("0")
                        sf.a1=0
                        sf.p1=float(sf.a1)*650
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Deluxe_Veggie.set("0")
                else:
                    sf.p1=float(sf.a1)*650
            else:
                sf.a1=sf.Deluxe_Veggie.get()
                if not sf.a1.isdigit():
                    #sf.Deluxe_Veggie.set("0")
                    if sf.a1=="":
                        #sf.Deluxe_Veggie.set("0")
                        sf.a1=0
                        sf.p1=float(sf.a1)*250
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Deluxe_Veggie.set("0")
                else:
                    sf.p1=float(sf.a1)*250
            sf.v2=sf.vp2.get()
            if sf.v2=="Medium":
                sf.a2=sf.Veg_Vaganza.get()
                if not sf.a2.isdigit():
                    if sf.a2=="":
                        sf.a2=0
                        sf.p2=float(sf.a2)*400
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Veg_Vaganza.set("0")
                        
                else:
                    sf.p2= float(sf.a2)*400
            elif sf.v2=="Large":
                sf.a2=sf.Veg_Vaganza.get()
                if not sf.a2.isdigit():
                    #sf.Veg_Vaganza.set("0")
                    if sf.a2=="":
                        #sf.Veg_Vaganza.set("0")
                        sf.a2=0
                        sf.p2=float(sf.a2)*600
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Veg_Vaganza.set("0")
                else:
                    sf.p2= float(sf.a2)*600
            else:
                sf.a2=sf.Veg_Vaganza.get()
                if not sf.a2.isdigit():
                    #sf.Veg_Vaganza.set("0")
                    if sf.a2=="":
                        #sf.Veg_Vaganza.set("0")
                        sf.a2=0
                        sf.p2=float(sf.a2)*250
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Veg_Vaganza.set("0")
                else:
                    sf.p2= float(sf.a2)*250
            sf.v3=sf.vp3.get()
            if sf.v3=="Medium":
                sf.a3=sf.Pepper.get()
                if not sf.a3.isdigit():
                    
                    if sf.a3=="":
                        sf.a3=0
                        sf.p3=float(sf.a3)*385
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Pepper.set("0")
                else:
                    sf.p3= float(sf.a3)*385
            elif sf.v3=="Large":
                sf.a3=sf.Pepper.get()
                if not sf.a3.isdigit():
                    #sf.Pepper.set("0")
                    if sf.a3=="":
                        #sf.Pepper.set("0")
                        sf.a3=0
                        sf.p3=float(sf.a3)*550
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Pepper.set("0")
                else:
                    sf.p3= float(sf.a3)*550
            else:
                sf.a3=sf.Pepper.get()
                if not sf.a3.isdigit():
                    #sf.Pepper.set("0")
                    if sf.a3=="":
                        #sf.Pepper.set("0")
                        sf.a3=0
                        sf.p3=float(sf.a3)*225
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Pepper.set("0")
                else:
                    sf.p3= float(sf.a3)*225
            sf.v4=sf.vp4.get()
            if sf.v4=="Medium":
                sf.a4=sf.Margherita.get()
                if not sf.a4.isdigit():
                    if sf.a4=="":
                        sf.a4=0
                        sf.p4=float(sf.a4)*195
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Margherita.set("0")
                else:
                    sf.p4= float(sf.a4)*195
            elif sf.v4=="Large":
                sf.a4=sf.Margherita.get()
                if not sf.a4.isdigit():
                    if sf.a4=="":
                        sf.a4=0
                        sf.p4=float(sf.a4)*385
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Margherita.set("0")
                else:
                    sf.p4= float(sf.a4)*385
            else:
                sf.a4=sf.Margherita.get()
                #sf.a4=sf.Margherita.get()
                if not sf.a4.isdigit():
                    if sf.a4=="":
                        sf.a4=0
                        sf.p4=float(sf.a4)*99
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Margherita.set("0")
                else:
                    sf.p4= float(sf.a4)*99
            sf.v5=sf.vp5.get()
            if sf.v5=="Medium":
                sf.a5=sf.Non_Veg_Supreme.get()
                if not sf.a5.isdigit():
                    if sf.a5=="":
                        sf.a5=0
                        sf.p5=float(sf.a5)*450
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Non_Veg_Supreme.set("0")
                else:
                    sf.p5= float(sf.a5)*450
            elif sf.v5=="Large":
                sf.a5=sf.Non_Veg_Supreme.get()
                if not sf.a5.isdigit():
                    #sf.Non_Veg_Supreme.set("0")
                    if sf.a5=="":
                        sf.a5=0
                        sf.p5=float(sf.a5)*650
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Non_Veg_Supreme.set("0")
                else:
                    sf.p5= float(sf.a5)*650
            else:
                sf.a5=sf.Non_Veg_Supreme.get()
                if not sf.a5.isdigit():
                    #sf.Non_Veg_Supreme.set("0")
                    if sf.a5=="":
                        sf.a5=0
                        sf.p5=float(sf.a5)*250
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Non_Veg_Supreme.set("0")
                else:
                    sf.p5= float(sf.a5)*250
            sf.v6=sf.vp6.get()
            if sf.v6=="Medium":
                sf.a6=sf.Chicken_Tikka.get()
                if not sf.a6.isdigit():                    
                    if sf.a6=="":
                        sf.a6=0
                        sf.p6=float(sf.a6)*400
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Tikka.set("0")
                else:
                    sf.p6= float(sf.a6)*400
            elif sf.v6=="Large":
                sf.a6=sf.Chicken_Tikka.get()
                if not sf.a6.isdigit():
                    if sf.a6=="":
                        sf.a6=0
                        sf.p6=float(sf.a6)*600
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Tikka.set("0")
                else:
                    sf.p6= float(sf.a6)*600
            else:
                sf.a6=sf.Chicken_Tikka.get()
                if not sf.a6.isdigit():
                    if sf.a6=="":
                        sf.a6=0
                        sf.p6=float(sf.a6)*250
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Tikka.set("0")
                else:
                    sf.p6= float(sf.a6)*250
            sf.v7=sf.vp7.get()
            if sf.v7=="Medium":
                sf.a7=sf.Chicken_Sausage.get()
                if not sf.a7.isdigit():                    
                    if sf.a7=="":
                        sf.a7=0
                        sf.p7=float(sf.a7)*385
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Sausage.set("0")
                else:
                    sf.p7= float(sf.a7)*385
            elif sf.v7=="Large":
                sf.a7=sf.Chicken_Sausage.get()
                if not sf.a7.isdigit():
                    if sf.a7=="":
                        sf.a7=0
                        sf.p7=float(sf.a7)*550
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Sausage.set("0")
                else:
                    sf.p7= float(sf.a7)*550
            else:
                sf.a7=sf.Chicken_Sausage.get()
                if not sf.a7.isdigit():
                    if sf.a7=="":
                        sf.a7=0
                        sf.p7=float(sf.a7)*225
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Sausage.set("0")
                else:
                    sf.p7= float(sf.a7)*225
            sf.v8=sf.vp8.get()
            if sf.v8=="Medium":
                sf.a8=sf.Chicken_Peri.get()
                if not sf.a8.isdigit():                    
                    if sf.a8=="":
                        sf.a8=0
                        sf.p8=float(sf.a8)*195
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Peri.set("0")
                else:
                    sf.p8= float(sf.a8)*195
            elif sf.v8=="Large":
                sf.a8=sf.Chicken_Peri.get()
                if not sf.a8.isdigit():
                    if sf.a8=="":
                        sf.a8=0
                        sf.p8=float(sf.a8)*385
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Peri.set("0")
                else:
                    sf.p8= float(sf.a8)*385
            else:
                sf.a8=sf.Chicken_Peri.get()
                if not sf.a8.isdigit():
                    if sf.a8=="":
                        sf.a8=0
                        sf.p8=float(sf.a8)*99
                    else:
                        messagebox.showinfo("Alert","Enter Valid Quantity")
                        sf.Chicken_Peri.set("0")
                else:
                    sf.p8= float(sf.a8)*99
                    
            sf.a9=sf.Roasted_Chicken.get()
            if not sf.a9.isdigit():
                
                if sf.a9=="":
                    sf.a9=0
                    sf.p9=float(sf.a9)*109
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.Roasted_Chicken.set("0")
            else:
                sf.p9= float(sf.a9)*109

            sf.a10=sf.Chicken_Meatballs.get()
            if not sf.a10.isdigit():
                
                if sf.a10=="":
                    sf.a10=0
                    sf.p10=float(sf.a10)*99
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.Chicken_Meatballs.set("0")
            else:
                sf.p10= float(sf.a10)*99

            sf.a11=sf.Boneles_sChicken.get()
            if not sf.a11.isdigit():
                
                if sf.a11=="":
                    sf.a11=0
                    sf.p11=float(sf.a11)*139
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.Boneles_sChicken.set("0")
            else:
                sf.p11= float(sf.a11)*139

            sf.a12=sf.Coke_Mobile.get()
            if not sf.a12.isdigit():
                
                if sf.a12=="":
                    sf.a12=0
                    sf.p12=float(sf.a12)*45
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.Coke_Mobile.set("0")
            else:
                sf.p12= float(sf.a12)*45

            sf.a13=sf.Burger_Pizza.get()
            if not sf.a13.isdigit():
                
                if sf.a13=="":
                    sf.a13=0
                    sf.p13=float(sf.a13)*99
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.Burger_Pizza.set("0")
            else:
                sf.p13= float(sf.a13)*99

            sf.a14=sf.White_Pasta.get()
            if not sf.a14.isdigit():
                
                if sf.a14=="":
                    sf.a14=0
                    sf.p14=float(sf.a14)*135
                else:
                    messagebox.showinfo("Alert","Enter Valid Quantity")
                    sf.White_Pasta.set("0")
            else:
                sf.p14= float(sf.a14)*135

            sf.costofmeal = "₹",str('%.2f'% (sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14))
            sf.PayTax=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)*.05)
            sf.Totalcost=(sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)
            sf.Ser_Charge=((sf.p1+sf.p2+sf.p3+sf.p4+sf.p5+sf.p6+sf.p7+sf.p8+sf.p9+sf.p10+sf.p11+sf.p12+sf.p13+sf.p14)/99)
            sf.Service="₹ "+str('%.2f'% sf.Ser_Charge)
            sf.OverAllCost="₹ "+str(int(sf.PayTax + sf.Totalcost + sf.Ser_Charge))
            sf.PaidTax="₹ "+str('%.2f'% sf.PayTax)
            sf.money=int(sf.PayTax + sf.Totalcost + sf.Ser_Charge)
            sf.Service_Charge.set(sf.Service)
            sf.cost.set(sf.costofmeal)
            sf.Tax.set(sf.PaidTax)
            sf.Total.set(sf.OverAllCost)

        def updater():
            Ref(sf)
            sf.txttot.after(1000,updater)

        def reset(sf):
            sf.money=0
            sf.Deluxe_Veggie.set("0")
            sf.Veg_Vaganza.set("0")
            sf.Pepper.set("0")
            sf.Margherita.set("0")
            sf.Non_Veg_Supreme.set("0")
            sf.Chicken_Tikka.set("0")
            sf.Chicken_Sausage.set("0")
            sf.Chicken_Peri.set("0")
            sf.Coke_Mobile.set("0")
            sf.Burger_Pizza.set("0")
            sf.White_Pasta.set("0")
            sf.Roasted_Chicken.set("0")
            sf.Chicken_Meatballs.set("0")
            sf.Boneles_sChicken.set("0")
            sf.Total.set("0")
            sf.Service_Charge.set("0")
            sf.Tax.set("0")
            sf.cost.set("0")
            sf.order.set("0")
            sf.Cutomer_name.set("")
            sf.cusmob.set("")
            sf.vp1.set("Medium")
            sf.vp2.set("Medium")
            sf.vp3.set("Medium")
            sf.vp4.set("Medium")
            sf.vp5.set("Medium")
            sf.vp6.set("Medium")
            sf.vp7.set("Medium")
            sf.vp8.set("Medium")
            

        def price(sf):
            sf.roo = Tk()
            sf.roo.geometry("600x768+0+0")
            sf.roo.title("Price List")
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
            sf.lblinfo.grid(row=0, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15,'bold'), text="Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=1, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
            sf.lblinfo.grid(row=0, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Deluxe Veggie", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=2, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Veg Vaganza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=3, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="5 sf.Pepper", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=4, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="sf.Margherita", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=5, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Pizza", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
            sf.lblinfo.grid(row=6, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Non-Veg Supreme", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=7, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Tikka", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=8, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Suasage", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=9, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Peri", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=10, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Specialty Chicken", fg="black", anchor=W)
            sf.lblinfo.grid(row=11, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Roasted Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹109", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=12, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Chicken Meatballs", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=13, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Boneless Chicken", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹139", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=14, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Sides & Beverages", fg="black", anchor=W)
            sf.lblinfo.grid(row=15, column=1)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Coke Mobile", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹45", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=16, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="Burger Pizza", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=17, column=2)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="White Pasta", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=0)
            sf.lblinfo = Label(sf.roo, font=('aria', 15, 'bold'), text="₹135", fg="steel blue", anchor=W)
            sf.lblinfo.grid(row=18, column=2)

            sf.roo.mainloop()




        sf.f2 = Frame(sf.scr,width =1366,bg="#f2e8b8",height=618)
        sf.f2.pack(side=BOTTOM,fill=BOTH)
        sf.Deluxe_Veggie= StringVar()
        sf.Veg_Vaganza = StringVar()
        sf.Pepper = StringVar()
        sf.Margherita= StringVar()
        sf.Non_Veg_Supreme = StringVar()
        sf.Chicken_Tikka = StringVar()
        sf.Chicken_Sausage= StringVar()
        sf.Chicken_Peri= StringVar()
        sf.Coke_Mobile = StringVar()
        sf.Burger_Pizza = StringVar()
        sf.White_Pasta = StringVar()
        sf.Roasted_Chicken= StringVar()
        sf.Chicken_Meatballs = StringVar()
        sf.Boneles_sChicken = StringVar()
        sf.Total = StringVar()
        sf.Service_Charge= StringVar()
        sf.Tax = StringVar()
        sf.cost = StringVar()
        sf.order=StringVar()
        sf.Cutomer_name =StringVar()
        sf.cusmob = StringVar()
        sf.vp1=StringVar()
        sf.vp2=StringVar()
        sf.vp3=StringVar()
        sf.vp4=StringVar()
        sf.vp5=StringVar()
        sf.vp6=StringVar()
        sf.vp7=StringVar()
        sf.vp8=StringVar()
        reset(sf)
        sf.l=["Medium","Large","Regular"]

        #veg pizza
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=1)
        sf.lbl1 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Veg Pizza",bd=10,anchor='w')
        sf.lbl1.place(x=180,y=0)
        sf.lbl11 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl11.grid(row=1,column=0)
        sf.lbl12 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl12.grid(row=1,column=1)
        sf.lbl13 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl13.grid(row=1,column=2,padx=4)

        sf.lbldel= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Deluxe Veggie:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbldel.grid(row=2,column=0)
        sf.opdel=OptionMenu(sf.f2,sf.vp1,*sf.l)
        sf.opdel.config(width=6)
        sf.opdel.grid(row=2,column=1)
        sf.txtdel= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Deluxe_Veggie , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtdel.grid(row=2,column=2)

        sf.lblvaga = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Veg Vaganza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblvaga.grid(row=3,column=0)
        sf.opvaga=OptionMenu(sf.f2,sf.vp2,*sf.l)
        sf.opvaga.config(width=6)
        sf.opvaga.grid(row=3,column=1)
        sf.txtvaga = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Veg_Vaganza , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtvaga.grid(row=3,column=2)

        sf.lblpep= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text=" 5 Pepper:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpep.grid(row=4,column=0)
        sf.oppep=OptionMenu(sf.f2,sf.vp3,*sf.l)
        sf.oppep.config(width=6)
        sf.oppep.grid(row=4,column=1)
        sf.txtpep= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Pepper ,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtpep.grid(row=4,column=2)

        sf.lblmag = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Margherita:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmag.grid(row=5,column=0)
        sf.opmag=OptionMenu(sf.f2,sf.vp4,*sf.l)
        sf.opmag.config(width=6)
        sf.opmag.grid(row=5,column=1)
        sf.txtmag = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Margherita,width=4,bg="powder blue",bd=6 ,justify='right')
        sf.txtmag.grid(row=5,column=2)


        #sf.non veg
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=6,column=1)
        sf.lbl2 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Non-Veg Pizza",bd=10,anchor='w')
        sf.lbl2.place(x=150,y=290)
        sf.lbl21 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl21.grid(row=7,column=0)
        sf.lbl22 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
        sf.lbl22.grid(row=7,column=1)
        sf.lbl23 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl23.grid(row=7,column=2)

        sf.lblsup= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Non-Veg Supreme:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsup.grid(row=8,column=0)
        sf.opsup=OptionMenu(sf.f2,sf.vp5,*sf.l)
        sf.opsup.config(width=6)
        sf.opsup.grid(row=8,column=1)
        sf.txtsup= Entry(sf.f2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Non_Veg_Supreme , bd=6,bg="powder blue" ,justify='right')
        sf.txtsup.grid(row=8,column=2)

        sf.lbltika = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Tikka:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltika.grid(row=9,column=0)
        sf.optika=OptionMenu(sf.f2,sf.vp6,*sf.l)
        sf.optika.config(width=6)
        sf.optika.grid(row=9,column=1)
        sf.txttika = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Tikka , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txttika.grid(row=9,column=2)

        sf.lblsaus= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Sausage:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblsaus.grid(row=10,column=0)
        sf.opsaus=OptionMenu(sf.f2,sf.vp7,*sf.l)
        sf.opsaus.config(width=6)
        sf.opsaus.grid(row=10,column=1)
        sf.txtsaus= Entry(sf.f2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Sausage , bd=6,bg="powder blue" ,justify='right')
        sf.txtsaus.grid(row=10,column=2)

        sf.lblperi = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Peri:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblperi.grid(row=11,column=0)
        sf.opperi=OptionMenu(sf.f2,sf.vp8,*sf.l)
        sf.opperi.config(width=6)
        sf.opperi.grid(row=11,column=1)
        sf.txtperi= Entry(sf.f2,font=('ariel' ,16,'bold'),width=4, textvariable=sf.Chicken_Peri , bd=6,bg="powder blue" ,justify='right')
        sf.txtperi.grid(row=11,column=2)

        #Special
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=5)
        sf.lbl3 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Specialty",bd=10,anchor='w')
        sf.lbl3.place(x=550,y=0)
        sf.lbl31 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl31.grid(row=1,column=4)
        sf.lbl33 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl33.grid(row=1,column=5)

        sf.lblros= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Roasted Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblros.grid(row=2,column=4)
        sf.txtros= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Roasted_Chicken , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtros.grid(row=2,column=5)

        sf.lblmeat = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Meatballs:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmeat.grid(row=3,column=4)
        sf.txtmeat = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Chicken_Meatballs , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtmeat.grid(row=3,column=5)

        sf.lblbon= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Boneless Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblbon.grid(row=4,column=4)
        sf.txtbon= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Boneles_sChicken,bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtbon.grid(row=4,column=5)

        #Sides
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=6,column=4)
        sf.lbl4 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Sides & Beverages",bd=10,anchor='w')
        sf.lbl4.place(x=500,y=290)
        sf.lbl41 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
        sf.lbl41.grid(row=7,column=4)
        sf.lbl43 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
        sf.lbl43.grid(row=7,column=5)

        sf.lblcok= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Coke Mobile:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblcok.grid(row=8,column=4)
        sf.txtcok= Entry(sf.f2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.Coke_Mobile , bd=6,bg="powder blue" ,justify='right')
        sf.txtcok.grid(row=8,column=5)

        sf.lblbur = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Burger Pizza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblbur.grid(row=9,column=4)
        sf.txtbur = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Burger_Pizza , bd=6,width=4,bg="powder blue" ,justify='right')
        sf.txtbur.grid(row=9,column=5)

        sf.lblpas= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="White Pasta:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblpas.grid(row=10,column=4)
        sf.txtpas= Entry(sf.f2,width=4,font=('ariel' ,16,'bold'), textvariable=sf.White_Pasta , bd=6,bg="powder blue" ,justify='right')
        sf.txtpas.grid(row=10,column=5)

        # customer
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=0,column=8)
        sf.lbl6 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,22, 'bold','underline' ),bg="#f2e8b8",text="Customer Detail",bd=10,anchor='w')
        sf.lbl6.place(x=970,y=0)
        
        sf.lblnam= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Name:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblnam.grid(row=1,column=7)
        sf.txtnam= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Cutomer_name , bd=6,width=14,bg="powder blue" ,justify='left')
        sf.txtnam.grid(row=1,column=8)


        sf.lblmob = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Mobile No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblmob.grid(row=2,column=7)
        sf.txtmob = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.cusmob,width=14,bd=6,bg="powder blue" ,justify='left')
        sf.txtmob.grid(row=2,column=8)

        #bill
        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=3,column=8)
        sf.lbl5 = Label(sf.f2,pady=2, font=( 'Cooper Black' ,22, 'bold','underline' ),bg="#f2e8b8",text="Bill Payment",bd=10,anchor='w')
        sf.lbl5.place(x=1000,y=140)

        sf.non=Label(sf.f2,pady=2,text=(" "),font=( 'Cooper Black' ,20),width=5,bg="#f2e8b8",bd=10,anchor='w')
        sf.non.grid(row=4,column=6)
        sf.lblord= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="    Order No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblord.grid(row=4,column=7)
        sf.txtord= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.order , bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txtord.grid(row=4,column=8)

        sf.lblco = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Subtotal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblco.grid(row=5,column=7)
        sf.txtco = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.cost,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtco.grid(row=5,column=8)

        sf.lblser= Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Service Charge:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lblser.grid(row=6,column=7)
        sf.txtser= Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Service_Charge ,width=14,bd=6,bg="powder blue" ,justify='right')
        sf.txtser.grid(row=6,column=8)

        sf.lbltax = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Tax:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltax.grid(row=7,column=7)
        sf.txttax = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Tax, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttax.grid(row=7,column=8)

        sf.lbltot = Label(sf.f2,pady=2, font=( 'aria' ,16, 'bold' ),text="Total:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
        sf.lbltot.grid(row=8,column=7)
        sf.txttot = Entry(sf.f2,font=('ariel' ,16,'bold'), textvariable=sf.Total, bd=6,width=14,bg="powder blue" ,justify='right')
        sf.txttot.grid(row=8,column=8)

        sf.btnprice=Button(sf.f2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PRICE", bg="powder blue",command=lambda:price(sf))
        sf.btnprice.place(x=970,y=440)

        sf.btnTotal=Button(sf.f2,pady=2,bd=6,fg="black",font=('ariel' ,16,'bold'),width=6, text="TOTAL", bg="powder blue",command=lambda:updater())
        sf.btnTotal.place(x=1160,y=440)

        sf.btnreset=Button(sf.f2,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=lambda:reset(sf))
        sf.btnreset.place(x=970,y=500)

        sf.btnpay=Button(sf.f2,pady=2, bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PAY", bg="powder blue",command=lambda:sf.adminorderdetail())
        sf.btnpay.place(x=1160,y=500)
        sf.scr.mainloop()
    def resultadminorder(sf):
        r1="Deluxe Veggie"
        r2="Veg Vaganza"
        r3="Pepper"
        r4="Margherita"
        r5="Non Veg Supreme"
        r6="Chicken Tikka"
        r7="Chicken Sausage"
        r8="Chicken Peri"
        r9="Coke Mobile"
        r10="Burger Pizza"
        r11="White Pasta"
        r12="Roasted Chicken"
        r13="Chicken Meatballs"
        r14="Boneles_sChicken"
        r20=sf.Cutomer_name.get()
        r21=sf.cusmob.get()
        r22=sf.vp1.get()
        r23=sf.vp2.get()
        r24=sf.vp3.get()
        r25=sf.vp4.get()
        r26=sf.vp5.get()
        r27=sf.vp6.get()
        r28=sf.vp7.get()
        r29=sf.vp8.get()
        r30=sf.txtdel.get()
        r31=sf.txtvaga.get()
        r32=sf.txtpep.get()
        r33=sf.txtmag.get()
        r34=sf.txtsup.get()
        r35=sf.txttika.get()
        r36=sf.txtsaus.get()
        r37=sf.txtperi.get()
        r38=sf.txtros.get()
        r39=sf.txtmeat.get()
        r40=sf.txtbon.get()
        r41=sf.txtcok.get()
        r42=sf.txtbur.get()
        r43=sf.txtpas.get()

        l1=[r1,r22,r30]
        l2=[r2,r23,r31]
        l3=[r3,r24,r32]
        l4=[r4,r25,r33]
        l5=[r5,r26,r34]
        l6=[r6,r27,r35]
        l7=[r7,r28,r36]
        l8=[r8,r29,r37]
        l9=[r12,r38]
        l10=[r13,r39]
        l11=[r14,r40]
        l12=[r9,r41]
        l13=[r10,r42]
        l14=[r11,r43]
        
        return r20,r21,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14


#--  page 6------        
    def menulist(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        #sf.scr.resizable(False, False)

        sf.frmdes()
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(950,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)

        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(50, 140, 1316, 420,fill="#d3ede6",outline="white",width=6)
        sf.veg=PhotoImage(file="veg.png")
        sf.c.create_image(230,250,image=sf.veg)
        sf.vegbut=Button(sf.f2,text="Veg Pizza",cursor="hand2",fg="white",command=lambda:sf.vegpizza(sf.x,username),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.vegbut.place(x=170,y=350)
        sf.nonveg=PhotoImage(file="Non.png")
        sf.c.create_image(530,250,image=sf.nonveg)
        sf.nonvegbut=Button(sf.f2,text="Non-Veg Pizza",cursor="hand2",fg="white",command=lambda:sf.nonvegpiz(sf.x,username),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.nonvegbut.place(x=440,y=350)
        sf.chi=PhotoImage(file="chiken.png")
        sf.c.create_image(830,250,image=sf.chi)
        sf.chibut=Button(sf.f2,text="Special Chicken",cursor="hand2",fg="white",command=lambda:sf.SpecialChi(sf.x,username),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.chibut.place(x=730,y=350)
        sf.side=PhotoImage(file="extra.png")
        sf.c.create_image(1130,250,image=sf.side)
        sf.sidebut=Button(sf.f2,text="Sides and Beverages",cursor="hand2",fg="white",command=lambda:sf.sidebev(sf.x,username),bg="#0b1335",bd=5,font=("default",18,'bold'))
        sf.sidebut.place(x=1000,y=350)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 7------
    def pizmain(sf,username):
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        
        #sf.scr.resizable(False, False)
        sf.frmdes()
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.c.create_text(850,110,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1000,110,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1200,y=60)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(950,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=790,y=40)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)

        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.c.create_rectangle(400,120,966,470,fill="#d3ede6",outline="white",width=2)
        sf.deli=PhotoImage(file="delivery.png")
        sf.c.create_image(540,260,image=sf.deli)
        sf.pic=PhotoImage(file="pick.png")
        sf.c.create_image(825,260,image=sf.pic)
        sf.de=Button(sf.f2,text="Delivery",cursor="hand2",fg="white",command=lambda:sf.Address("Delivery",username),bg="#0b1335",font=("default",20),bd=5)
        sf.de.place(x=480,y=400)
        sf.pu=Button(sf.f2,text="Pick Up",cursor="hand2",fg="white",command=lambda:sf.menulist("Pick Up",username),bg="#0b1335",font=("default",20),bd=5)
        sf.pu.place(x=770,y=400)
        sf.c.create_rectangle(405,125,678,465,outline="black",width=2)
        sf.c.create_rectangle(688,125,960,465,outline="black",width=2)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 8------
    def vegpizza(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        
        #sf.scr.resizable(False, False)
        sf.frmdes()
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)        
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(950,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        sf.f1.pack(fill=BOTH,expand=1)

        sf.f2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="VEG PIZZA",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=600,y=4)
        sf.c.create_rectangle(400, 40, 966, 540,fill="#d3ede6",outline="white",width=6)
        #sf.q1=StringVar()
        #sf.q2=StringVar()
        #sf.q3=StringVar()
        #sf.q4=StringVar()
        #sf.q1.set("0")
        #sf.q2.set("0")
        #sf.q3.set("0")
        #sf.q4.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170,width=2)
        sf.delu=PhotoImage(file="deluxe.png")
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Deluxe Veggie    ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,80,text="₹450/₹650/₹250",fill="#ff3838",font=("default",17,'bold'))
        #ch1=sf.check(sf.f2,100)
        sf.v1=IntVar()
        sf.C11=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v1)
        sf.C11.place(x=550,y=100)
        sf.C12 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v1)
        sf.C12.place(x=650,y=100)
        sf.C13 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v1)
        sf.C13.place(x=750,y=100)
        sf.C11.select()
        sf.C11.deselect()    
        sf.C11.invoke()

        sf.pri1=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri1.place(x=850,y=70)
        def updat1():
            if sf.v1.get()==10:
                pric1="₹ 450"
            elif sf.v1.get()==20:
                pric1='₹ 650'
            else:
                pric1='₹ 250'
            sf.pri1.config(text=pric1)
            sf.pri1.after(100,updat1)
        updat1()

        def add1():
            value = int(sf.q1.get())
            value += 1
            if value>100:
                value=100
            sf.q1.delete(0, 'end')
            sf.q1.insert(0, value)

        def sub1():
            value = int(sf.q1.get())
            value -= 1
            if value<0:
                value=0
            sf.q1.delete(0, 'end')
            sf.q1.insert(0, value)
    
        sf.c.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q1=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q1.insert(0,0)
        sf.q1.place(x=670,y=140)
        sf.bt11 =Button(sf.f2, text="+", command=add1)
        sf.bt11.place(x=720,y=140) 
        sf.bt12 =Button(sf.f2, text="-", command=sub1)
        sf.bt12.place(x=652,y=140)
        
        
        sf.add1=Button(sf.f2,text="ADD",command=lambda:addch1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add1.place(x=850,y=120)
        def addch1():
            if sf.v1.get()==10:
                ch1="Medium"
                pric1=450
            elif sf.v1.get()==20:
                ch1="Large"
                pric1=650
            else:
                ch1="Regular"
                pric1=250
            try:
                sf.addlist(sf.x,username,["Deluxe Veggie",ch1,sf.q1.get(),pric1*int(sf.q1.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
            
        #pizza 2
        sf.c.create_rectangle(405, 170, 960, 290,width=2)
        sf.vag=PhotoImage(file="extravaganza.png")
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Veg Vaganza      ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,200,text="₹400/₹600/₹250",fill="#ff3838",font=("default",17,'bold'))
##        ch2=sf.check(sf.f2,220)
        sf.v2=IntVar()
        sf.C21=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v2)
        sf.C21.place(x=550,y=220)
        sf.C22 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v2)
        sf.C22.place(x=650,y=220)
        sf.C23 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v2)
        sf.C23.place(x=750,y=220)
        sf.C21.select()
        sf.C21.deselect()    
        sf.C21.invoke()

        sf.pri2=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri2.place(x=850,y=190)
        def updat2():
            if sf.v2.get()==10:
                pric2="₹ 400"
            elif sf.v2.get()==20:
                pric2='₹ 600'
            else:
                pric2='₹ 250'
            sf.pri2.config(text=pric2)
            sf.pri2.after(100,updat2)
        updat2()

        def add2():
            value = int(sf.q2.get())
            value += 1
            if value>100:
                value=100
            sf.q2.delete(0, 'end')
            sf.q2.insert(0, value)

        def sub2():
            value = int(sf.q2.get())
            value -= 1
            if value<0:
                value=0
            sf.q2.delete(0, 'end')
            sf.q2.insert(0, value)
    
        sf.c.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q2=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q2.insert(0,0)
        sf.q2.place(x=670,y=260)
        sf.bt21 =Button(sf.f2, text="+", command=add2)
        sf.bt21.place(x=720,y=260) 
        sf.bt22 =Button(sf.f2, text="-", command=sub2)
        sf.bt22.place(x=652,y=260)
        
        sf.add2=Button(sf.f2,text="ADD",command=lambda:addch2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add2.place(x=850,y=240)
        def addch2():
            if sf.v2.get()==10:
                ch2="Medium"
                pric2=400
            elif sf.v2.get()==20:
                ch2="Large"
                pric2=600
            else:
                ch2="Regular"
                pric2=250

            try:
                sf.addlist(sf.x,username,["Veg Vaganza",ch2,sf.q2.get(),pric2*int(sf.q2.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 3
        sf.c.create_rectangle(405, 290, 960, 410,width=2)
        sf.pep=PhotoImage(file="5-pepper-veg-pizza.png")
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="5 Pepper",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,320,text="₹385/₹550/₹225",fill="#ff3838",font=("default",17,'bold'))
        #ch3=sf.check(sf.f2,340)
        sf.v3=IntVar()
        sf.C31=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v3)
        sf.C31.place(x=550,y=340)
        sf.C32 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v3)
        sf.C32.place(x=650,y=340)
        sf.C33 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v3)
        sf.C33.place(x=750,y=340)
        sf.C31.select()
        sf.C31.deselect()    
        sf.C31.invoke()

        sf.pri3=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri3.place(x=850,y=310)
        def updat3():
            if sf.v3.get()==10:
                pric3="₹ 385"
            elif sf.v3.get()==20:
                pric3='₹ 550'
            else:
                pric3='₹ 225'
            sf.pri3.config(text=pric3)
            sf.pri3.after(100,updat3)
        updat3()

        def add3():
            value = int(sf.q3.get())
            value += 1
            if value>100:
                value=100
            sf.q3.delete(0, 'end')
            sf.q3.insert(0, value)

        def sub3():
            value = int(sf.q3.get())
            value -= 1
            if value<0:
                value=0
            sf.q3.delete(0, 'end')
            sf.q3.insert(0, value)
    
        sf.c.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q3=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q3.insert(0,0)
        sf.q3.place(x=670,y=380)
        sf.bt31 =Button(sf.f2, text="+", command=add3)
        sf.bt31.place(x=720,y=380) 
        sf.bt32 =Button(sf.f2, text="-", command=sub3)
        sf.bt32.place(x=652,y=380)

        sf.add3=Button(sf.f2,text="ADD",command=lambda:addch3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add3.place(x=850,y=360)
        def addch3():
            if sf.v3.get()==10:
                ch3="Medium"
                pric3=385
            elif sf.v3.get()==20:
                ch3="Large"
                pric3=550
            else:
                ch3="Regular"
                pric3=225
            try:
                sf.addlist(sf.x,username,["5 Pepper",ch3,sf.q3.get(),pric3*int(sf.q3.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
            
        #pizza 4
        sf.c.create_rectangle(405, 410, 960, 530,width=2)
        sf.mag=PhotoImage(file="Margherit.png")
        sf.c.create_image(470,470,image=sf.mag)
        sf.c.create_text(650,440,text="Margherita       ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,440,text="₹195/₹385/₹99",fill="#ff3838",font=("default",17,'bold'))
        #ch4=sf.check(sf.f2,460)
        sf.v4=IntVar()
        sf.C41=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v4)
        sf.C41.place(x=550,y=460)
        sf.C42 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v4)
        sf.C42.place(x=650,y=460)
        sf.C43 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v4)
        sf.C43.place(x=750,y=460)
        sf.C41.select()
        sf.C41.deselect()    
        sf.C41.invoke()

        sf.pri4=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri4.place(x=850,y=430)
        def updat4():
            if sf.v4.get()==10:
                pric4="₹ 195"
            elif sf.v4.get()==20:
                pric4='₹ 385'
            else:
                pric4='₹ 99'
            sf.pri4.config(text=pric4)
            sf.pri4.after(100,updat4)
        updat4()

        def add4():
            value = int(sf.q4.get())
            value += 1
            if value>100:
                value=100
            sf.q4.delete(0, 'end')
            sf.q4.insert(0, value)

        def sub4():
            value = int(sf.q4.get())
            value -= 1
            if value<0:
                value=0
            sf.q4.delete(0, 'end')
            sf.q4.insert(0, value)
    
        sf.c.create_text(590,500,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q4=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q4.insert(0,0)
        sf.q4.place(x=670,y=500)
        sf.bt41 =Button(sf.f2, text="+", command=add4)
        sf.bt41.place(x=720,y=500) 
        sf.bt42 =Button(sf.f2, text="-", command=sub4)
        sf.bt42.place(x=652,y=500)
        
        sf.add4=Button(sf.f2,text="ADD",command=lambda:addch4(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add4.place(x=850,y=480)
        def addch4():
            if sf.v4.get()==10:
                ch4="Medium"
                pric4=195
            elif sf.v4.get()==20:
                ch4="Large"
                pric4=385
            else:
                ch4="Regular"
                pric4=99
            try:
                sf.addlist(sf.x,username,["Margherita",ch4,sf.q4.get(),pric4*int(sf.q4.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")

        sf.con=Button(sf.f2,text="Confirm Order",command=lambda:sf.ordercheck(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.f2,text="Add More..",command=lambda:sf.menulist(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()
        
##----page 9 ------
    def addlist(sf,x,username,q):
        sf.x=x
        if (int(q[-2])>0 and int(q[-2])<101) and q[-2].isdigit():
            f=0
            i=0
            if len(q)==4:
                for i in range(len(sf.cartlist)):
                    if q[0] in sf.cartlist[i] and q[1] in sf.cartlist[i] and int(sf.cartlist[i][2])<101:
                        sf.cartlist[i][2]=str(int(sf.cartlist[i][2])+int(q[2]))
                        sf.cartlist[i][3]+=q[3]
                        sf.amount=sf.amount+q[-1]
                        f=1
            else:
                for i in range(len(sf.cartlist)):
                    if q[0] in sf.cartlist[i] and int(sf.cartlist[i][-2])<101:
                        sf.cartlist[i][-2]=str(int(sf.cartlist[i][-2])+int(q[-2]))
                        sf.cartlist[i][-1]+=q[-1]
                        sf.amount=sf.amount+q[-1]
                        f=1
                
            if f==0:
                sf.cartlist.append(q)
                sf.amount=sf.amount+q[-1]
            if  int(sf.cartlist[i][-2])==100:
                messagebox.showinfo("Cart","Add upto 100 of each")
            else:
                messagebox.showinfo("Cart","Item Successfully added")
        else:
            messagebox.showinfo("Cart","Enter Valid Quantity to add\n Only 1-100 at a time")
        sf.cart(sf.x,username)
        
#--  page 10------
    def nonvegpiz(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        #sf.scr.resizable(False, False)
        sf.frmdes()
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(950,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        

        sf.f2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="NON-VEG PIZZA",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=580,y=4)
        sf.c.create_rectangle(400, 40, 966, 540,fill="#d3ede6",outline="white",width=6)
##        sf.q5=StringVar()
##        sf.q6=StringVar()
##        sf.q7=StringVar()
##        sf.q8=StringVar()
##        sf.q5.set("0")
##        sf.q6.set("0")
##        sf.q7.set("0")
##        sf.q8.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170,width=2)
        sf.delu=PhotoImage(file="Non-Veg_Supreme.png")
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Non-Veg Supreme  ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,80,text="₹450/₹650/₹250",fill="#ff3838",font=("default",17,'bold'))
        #ch5=sf.check(sf.f2,100)
        sf.v5=IntVar()
        sf.C51=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v5)
        sf.C51.place(x=550,y=100)
        sf.C52 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v5)
        sf.C52.place(x=650,y=100)
        sf.C53 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v5)
        sf.C53.place(x=750,y=100)
        sf.C51.select()
        sf.C51.deselect()    
        sf.C51.invoke()

        sf.pri5=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri5.place(x=850,y=70)
        def updat5():
            if sf.v5.get()==10:
                pric5="₹ 450"
            elif sf.v5.get()==20:
                pric5='₹ 650'
            else:
                pric5='₹ 250'
            sf.pri5.config(text=pric5)
            sf.pri5.after(100,updat5)
        updat5()

        def add5():
            value = int(sf.q5.get())
            value += 1
            if value>100:
                value=100
            sf.q5.delete(0, 'end')
            sf.q5.insert(0, value)

        def sub5():
            value = int(sf.q5.get())
            value -= 1
            if value<0:
                value=0
            sf.q5.delete(0, 'end')
            sf.q5.insert(0, value)
    
        sf.c.create_text(590,150,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q5=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q5.insert(0,0)
        sf.q5.place(x=670,y=140)
        sf.bt51 =Button(sf.f2, text="+", command=add5)
        sf.bt51.place(x=720,y=140) 
        sf.bt52 =Button(sf.f2, text="-", command=sub5)
        sf.bt52.place(x=652,y=140)
                
        sf.add5=Button(sf.f2,text="ADD",command=lambda:addch5(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add5.place(x=850,y=120)
        def addch5():
            if sf.v5.get()==10:
                ch5="Medium"
                pric5=450
            elif sf.v5.get()==20:
                ch5="Large"
                pric5=650
            else:
                ch5="Regular"
                pric5=250
            try:
                sf.addlist(sf.x,username,["Non-Veg Supreme",ch5,sf.q5.get(),pric5*int(sf.q5.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 2
        sf.c.create_rectangle(405, 170, 960, 290,width=2)
        sf.vag=PhotoImage(file="nonChicken_Tikka.png")
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Chicken Tikka    ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,200,text="₹400/₹600/₹250",fill="#ff3838",font=("default",17,'bold'))
        #ch6=sf.check(sf.f2,220)
        sf.v6=IntVar()
        sf.C61=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v6)
        sf.C61.place(x=550,y=220)
        sf.C62 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v6)
        sf.C62.place(x=650,y=220)
        sf.C63 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v6)
        sf.C63.place(x=750,y=220)
        sf.C61.select()
        sf.C61.deselect()    
        sf.C61.invoke()

        sf.pri6=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri6.place(x=850,y=190)
        def updat6():
            if sf.v6.get()==10:
                pric6="₹ 400"
            elif sf.v6.get()==20:
                pric6='₹ 600'
            else:
                pric6='₹ 250'
            sf.pri6.config(text=pric6)
            sf.pri6.after(100,updat6)
        updat6()

        def add6():
            value = int(sf.q6.get())
            value += 1
            if value>100:
                value=100
            sf.q6.delete(0, 'end')
            sf.q6.insert(0, value)

        def sub6():
            value = int(sf.q6.get())
            value -= 1
            if value<0:
                value=0
            sf.q6.delete(0, 'end')
            sf.q6.insert(0, value)
    
        sf.c.create_text(590,270,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q6=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q6.insert(0,0)
        sf.q6.place(x=670,y=260)
        sf.bt61 =Button(sf.f2, text="+", command=add6)
        sf.bt61.place(x=720,y=260) 
        sf.bt62 =Button(sf.f2, text="-", command=sub6)
        sf.bt62.place(x=652,y=260)
        
        sf.add6=Button(sf.f2,text="ADD",command=lambda:addch6(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add6.place(x=850,y=240)
        def addch6():
            if sf.v6.get()==10:
                ch6="Medium"
                pric6=400
            elif sf.v6.get()==20:
                ch6="Large"
                pric6=600
            else:
                ch6="Regular"
                pric6=250
            try:
                sf.addlist(sf.x,username,["Chicken Tikka",ch6,sf.q6.get(),pric6*int(sf.q6.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 3
        sf.c.create_rectangle(405, 290, 960, 410,width=2)
        sf.pep=PhotoImage(file="non-Chicken_Sausage.png")
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Chicken Sausage  ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,320,text="₹385/₹550/₹225",fill="#ff3838",font=("default",17,'bold'))
        #ch7=sf.check(sf.f2,340)
        sf.v7=IntVar()
        sf.C71=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v7)
        sf.C71.place(x=550,y=340)
        sf.C72 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v7)
        sf.C72.place(x=650,y=340)
        sf.C73 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v7)
        sf.C73.place(x=750,y=340)
        sf.C71.select()
        sf.C71.deselect()    
        sf.C71.invoke()

        sf.pri7=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri7.place(x=850,y=310)
        def updat7():
            if sf.v7.get()==10:
                pric7="₹ 385"
            elif sf.v7.get()==20:
                pric7='₹ 550'
            else:
                pric7='₹ 225'
            sf.pri7.config(text=pric7)
            sf.pri7.after(100,updat7)
        updat7()

        def add7():
            value = int(sf.q7.get())
            value += 1
            if value>100:
                value=100
            sf.q7.delete(0, 'end')
            sf.q7.insert(0, value)

        def sub7():
            value = int(sf.q7.get())
            value -= 1
            if value<0:
                value=0
            sf.q7.delete(0, 'end')
            sf.q7.insert(0, value)
    
        sf.c.create_text(590,390,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q7=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q7.insert(0,0)
        sf.q7.place(x=670,y=380)
        sf.bt71 =Button(sf.f2, text="+", command=add7)
        sf.bt71.place(x=720,y=380) 
        sf.bt72 =Button(sf.f2, text="-", command=sub7)
        sf.bt72.place(x=652,y=380)
        
        sf.add7=Button(sf.f2,text="ADD",command=lambda:addch7(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add7.place(x=850,y=360)
        def addch7():
            if sf.v7.get()==10:
                ch7="Medium"
                pric7=385
            elif sf.v7.get()==20:
                ch7="Large"
                pric7=550
            else:
                ch7="Regular"
                pric7=225
            try:
                sf.addlist(sf.x,username,["Chicken Sausage",ch7,sf.q7.get(),pric7*int(sf.q7.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 4
        sf.c.create_rectangle(405, 410, 960, 530,width=2)
        sf.mag=PhotoImage(file="no-LoadedL.png")
        sf.c.create_image(470,470,image=sf.mag)
        sf.c.create_text(650,440,text="Chicken Peri     ",fill="#000000",font=("Cooper Black",20))
        #sf.c.create_text(860,440,text="₹195/₹385/₹99",fill="#ff3838",font=("default",17,'bold'))
        #ch8=sf.check(sf.f2,460)
        sf.v8=IntVar()
        sf.C81=Radiobutton(sf.f2,text = "Medium",value=10,variable=sf.v8)
        sf.C81.place(x=550,y=460)
        sf.C82 = Radiobutton(sf.f2, text = "Large",value = 20, variable =sf.v8)
        sf.C82.place(x=650,y=460)
        sf.C83 = Radiobutton(sf.f2, text = "Regular",value = 30, variable =sf.v8)
        sf.C83.place(x=750,y=460)
        sf.C81.select()
        sf.C81.deselect()    
        sf.C81.invoke()

        sf.pri8=Label(sf.f2,fg="#ff3838",bg="#d3ede6",font=("default",17,'bold'))
        sf.pri8.place(x=850,y=430)
        def updat8():
            if sf.v8.get()==10:
                pric8="₹ 195"
            elif sf.v8.get()==20:
                pric8='₹ 385'
            else:
                pric8='₹ 99'
            sf.pri8.config(text=pric8)
            sf.pri8.after(100,updat8)
        updat8()

        def add8():
            value = int(sf.q8.get())
            value += 1
            if value>100:
                value=100
            sf.q8.delete(0, 'end')
            sf.q8.insert(0, value)

        def sub8():
            value = int(sf.q8.get())
            value -= 1
            if value<0:
                value=0
            sf.q8.delete(0, 'end')
            sf.q8.insert(0, value)
    
        sf.c.create_text(590,500,text="Quantity : ",fill="#000000",font=("default",12))
        sf.q8=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q8.insert(0,0)
        sf.q8.place(x=670,y=500)
        sf.bt81 =Button(sf.f2, text="+", command=add8)
        sf.bt81.place(x=720,y=500) 
        sf.bt82 =Button(sf.f2, text="-", command=sub8)
        sf.bt82.place(x=652,y=500)

        sf.add8=Button(sf.f2,text="ADD",command=lambda:addch8(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add8.place(x=850,y=480)
        def addch8():
            if sf.v8.get()==10:
                ch8="Medium"
                pric8=195
            elif sf.v8.get()==20:
                ch8="Large"
                pric8=385
            else:
                ch8="Regular"
                pric8=99
            try:
                sf.addlist(sf.x,username,["Chicken Peri",ch8,sf.q8.get(),pric8*int(sf.q8.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        sf.con=Button(sf.f2,text="Confirm Order",command=lambda:sf.ordercheck(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=1050,y=250)
        sf.more=Button(sf.f2,text="Add More..",command=lambda:sf.menulist(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.more.place(x=1050,y=350)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 11------
    def SpecialChi(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        #sf.localtime=time.asctime(time.localtime(time.time()))
        #sf.c.create_text(950,50,text=sf.localtime,fill="white",font=("default",16))
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        
        sf.f2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="SPECIALTY CHICKEN",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=540,y=4)
        sf.c.create_rectangle(400, 40, 966, 420,fill="#d3ede6",outline="white",width=6)
##        sf.q9=StringVar()
##        sf.q10=StringVar()
##        sf.q11=StringVar()
##        sf.q9.set("0")
##        sf.q10.set("0")
##        sf.q11.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170,width=2)
        sf.delu=PhotoImage(file="roasted.png")
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Roasted Chicken  ",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,80,text="₹109",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,120,text="Quantity : ",fill="#000000",font=("default",12))

        def add9():
            value = int(sf.q9.get())
            value += 1
            if value>100:
                value=100
            sf.q9.delete(0, 'end')
            sf.q9.insert(0, value)

        def sub9():
            value = int(sf.q9.get())
            value -= 1
            if value<0:
                value=0
            sf.q9.delete(0, 'end')
            sf.q9.insert(0, value)
        sf.q9=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q9.insert(0,0)
        sf.q9.place(x=670,y=110)
        sf.bt91 =Button(sf.f2, text="+", command=add9)
        sf.bt91.place(x=720,y=110) 
        sf.bt92 =Button(sf.f2, text="-", command=sub9)
        sf.bt92.place(x=652,y=110)

        sf.add9=Button(sf.f2,text="ADD",command=lambda:addspe1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add9.place(x=850,y=120)
        def addspe1():
            try:
                sf.addlist(sf.x,username,["Roasted Chicken",sf.q9.get(),109*int(sf.q9.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
            
        #pizza 2
        sf.c.create_rectangle(405, 170, 960, 290,width=2)
        sf.vag=PhotoImage(file="chicken-meatballs.jpg")
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Chicken Meatballs",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,200,text="₹99",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,240,text="Quantity : ",fill="#000000",font=("default",12))

        def add10():
            value = int(sf.q10.get())
            value += 1
            if value>100:
                value=100
            sf.q10.delete(0, 'end')
            sf.q10.insert(0, value)

        def sub10():
            value = int(sf.q10.get())
            value -= 1
            if value<0:
                value=0
            sf.q10.delete(0, 'end')
            sf.q10.insert(0, value)
        sf.q10=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q10.insert(0,0)
        sf.q10.place(x=670,y=230)
        sf.bt101 =Button(sf.f2, text="+", command=add10)
        sf.bt101.place(x=720,y=230) 
        sf.bt102 =Button(sf.f2, text="-", command=sub10)
        sf.bt102.place(x=652,y=230)

        sf.add10=Button(sf.f2,text="ADD",command=lambda:addspe2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add10.place(x=850,y=240)
        def addspe2():
            try:
                sf.addlist(sf.x,username,["Chicken Meatballs",sf.q10.get(),99*int(sf.q10.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 3
        sf.c.create_rectangle(405, 290, 960, 410,width=2)
        sf.pep=PhotoImage(file="Boneless-Chicken-wings-192x192.png")
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="Boneless Chicken ",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,320,text="₹139",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,360,text="Quantity : ",fill="#000000",font=("default",12))

        def add11():
            value = int(sf.q11.get())
            value += 1
            if value>100:
                value=100
            sf.q11.delete(0, 'end')
            sf.q11.insert(0, value)

        def sub11():
            value = int(sf.q11.get())
            value -= 1
            if value<0:
                value=0
            sf.q11.delete(0, 'end')
            sf.q11.insert(0, value)
        sf.q11=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q11.insert(0,0)
        sf.q11.place(x=670,y=350)
        sf.bt111 =Button(sf.f2, text="+", command=add11)
        sf.bt111.place(x=720,y=350) 
        sf.bt112 =Button(sf.f2, text="-", command=sub11)
        sf.bt112.place(x=652,y=350)
        
        sf.add11=Button(sf.f2,text="ADD",command=lambda:addspe3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add11.place(x=850,y=360)
        def addspe3():
            try:
                sf.addlist(sf.x,username,["Boneless Chiken",sf.q11.get(),139*int(sf.q11.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        sf.con=Button(sf.f2,text="Confirm Order",command=lambda:sf.ordercheck(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=600,y=430)
        sf.more=Button(sf.f2,text="Add More..",command=lambda:sf.menulist(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.more.place(x=630,y=500)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

#--  page 12------
    def sidebev(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()

        sf.f2=Frame(sf.scr,height=618,width=1366)
        
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="SIDES & BEVERAGES",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=520,y=4)
        sf.c.create_rectangle(400, 40, 966, 420,fill="#d3ede6",outline="white",width=6)
##        sf.q12=StringVar()
##        sf.q13=StringVar()
##        sf.q14=StringVar()
##        sf.q12.set("0")
##        sf.q13.set("0")
##        sf.q14.set("0")
        # pizza 1
        sf.c.create_rectangle(405, 50, 960, 170,width=2)
        sf.delu=PhotoImage(file="coke.png")
        sf.c.create_image(470,110,image=sf.delu)
        sf.c.create_text(650,80,text="Coke Mobile      ",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,80,text="₹45",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,120,text="Quantity : ",fill="#000000",font=("default",12))

        def add12():
            value = int(sf.q12.get())
            value += 1
            if value>100:
                value=100
            sf.q12.delete(0, 'end')
            sf.q12.insert(0, value)

        def sub12():
            value = int(sf.q12.get())
            value -= 1
            if value<0:
                value=0
            sf.q12.delete(0, 'end')
            sf.q12.insert(0, value)
        sf.q12=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q12.insert(0,0)
        sf.q12.place(x=670,y=110)
        sf.bt121 =Button(sf.f2, text="+", command=add12)
        sf.bt121.place(x=720,y=110) 
        sf.bt122 =Button(sf.f2, text="-", command=sub12)
        sf.bt122.place(x=652,y=110)
        
        sf.add12=Button(sf.f2,text="ADD",command=lambda:addsid1(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add12.place(x=850,y=120)
        def addsid1():
            try:
                sf.addlist(sf.x,username,["Coke Mobile",sf.q12.get(),45*int(sf.q12.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 2
        sf.c.create_rectangle(405, 170, 960, 290,width=2)
        sf.vag=PhotoImage(file="burger.png")
        sf.c.create_image(470,230,image=sf.vag)
        sf.c.create_text(650,200,text="Burger Pizza     ",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,200,text="₹99",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,240,text="Quantity : ",fill="#000000",font=("default",12))

        def add13():
            value = int(sf.q13.get())
            value += 1
            if value>100:
                value=100
            sf.q13.delete(0, 'end')
            sf.q13.insert(0, value)

        def sub13():
            value = int(sf.q13.get())
            value -= 1
            if value<0:
                value=0
            sf.q13.delete(0, 'end')
            sf.q13.insert(0, value)
        sf.q13=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q13.insert(0,0)
        sf.q13.place(x=670,y=230)
        sf.bt131 =Button(sf.f2, text="+", command=add13)
        sf.bt131.place(x=720,y=230) 
        sf.bt132 =Button(sf.f2, text="-", command=sub13)
        sf.bt132.place(x=652,y=230)

        sf.add13=Button(sf.f2,text="ADD",command=lambda:addsid2(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add13.place(x=850,y=240)
        def addsid2():
            try:
                sf.addlist(sf.x,username,["Burger Pizza",sf.q13.get(),99*int(sf.q13.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        #pizza 3
        sf.c.create_rectangle(405, 290, 960, 410,width=2)
        sf.pep=PhotoImage(file="white.png")
        sf.c.create_image(470,350,image=sf.pep)
        sf.c.create_text(650,320,text="White Pasta      ",fill="#000000",font=("Cooper Black",20))
        sf.c.create_text(875,320,text="₹135",fill="#ff3838",font=("default",17,'bold'))
        sf.c.create_text(590,360,text="Quantity : ",fill="#000000",font=("default",12))

        def add14():
            value = int(sf.q14.get())
            value += 1
            if value>100:
                value=100
            sf.q14.delete(0, 'end')
            sf.q14.insert(0, value)

        def sub14():
            value = int(sf.q14.get())
            value -= 1
            if value<0:
                value=0
            sf.q14.delete(0, 'end')
            sf.q14.insert(0, value)
        sf.q14=Entry(sf.f2,bg="#aae2d7",font=("default",14),width=4)
        sf.q14.insert(0,0)
        sf.q14.place(x=670,y=350)
        sf.bt141 =Button(sf.f2, text="+", command=add14)
        sf.bt141.place(x=720,y=350) 
        sf.bt142 =Button(sf.f2, text="-", command=sub14)
        sf.bt142.place(x=652,y=350)
        
        sf.add14=Button(sf.f2,text="ADD",command=lambda:addsid3(),bg="#0b1335",cursor="hand2",fg="white",bd=4,font=("default",12,'bold'))
        sf.add14.place(x=850,y=360)
        def addsid3():
            try:
                sf.addlist(sf.x,username,["White Pasta",sf.q14.get(),135*int(sf.q14.get())])
            except:
                messagebox.showinfo("Attention","Enter valid Quantity")
        sf.con=Button(sf.f2,text="Confirm Order",command=lambda:sf.ordercheck(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
        sf.con.place(x=600,y=430)
        sf.more=Button(sf.f2,text="Add More..",command=lambda:sf.menulist(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.more.place(x=630,y=500)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def ordercheck(sf,x,username):
        if sf.amount==0:
            messagebox.showinfo("Pay","Place Some Order")
        else:
            sf.Orderde(sf.x,username)

#--  page 13------
    def Address(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="Address",fg="white",bg="#0b1335",width=20,font=("default",27))
        sf.log.place(x=480,y=110)
        sf.c.create_rectangle(150,100,1216,450,fill="#d3ede6",outline="white",width=6)
        sf.lab1=Label(sf.f2,text="City",bg="#d3ede6",font=("cooper black",18))
        sf.lab1.place(x=190,y=200)
        sf.city=Entry(sf.f2,bg="white",width=15,font=("default",18),bd=5)
        sf.city.place(x=430,y=200)
        sf.lab2=Label(sf.f2,text="Locality",bg="#d3ede6",font=("cooper black",18))
        sf.lab2.place(x=730,y=200)
        sf.loc=Entry(sf.f2,bg="white",width=15,font=("default",18),bd=5)
        sf.loc.place(x=918,y=200)
        sf.lab3=Label(sf.f2,text="Building Name",bg="#d3ede6",font=("cooper black",18))
        sf.lab3.place(x=190,y=250)
        sf.buil=Entry(sf.f2,bg="white",width=15,font=("default",18),bd=5)
        sf.buil.place(x=430,y=250)
        sf.lab4=Label(sf.f2,text="House No.",bg="#d3ede6",font=("cooper black",18))
        sf.lab4.place(x=730,y=250)
        sf.hou=Entry(sf.f2,bg="white",width=15,font=("default",18),bd=5)
        sf.hou.place(x=918,y=250)
        sf.lab5=Label(sf.f2,text="Landmark",bg="#d3ede6",font=("cooper black",18))
        sf.lab5.place(x=190,y=300)
        sf.lan=Entry(sf.f2,bg="white",width=15,font=("default",18),bd=5)
        sf.lan.place(x=430,y=300)
        sf.bc=Button(sf.f2,text="Back",command=lambda:sf.pizmain(username),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.bc.place(x=370,y=370)
        sf.rg=Button(sf.f2,text="Order Now",command=lambda:sf.ordernow(username),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.rg.place(x=610,y=370)
        def clear(sf):
            sf.city.delete(0,END)
            sf.loc.delete(0,END)
            sf.buil.delete(0,END)
            sf.hou.delete(0,END)
            sf.lan.delete(0,END)
        sf.cl=Button(sf.f2,text="Clear",command=lambda:clear(sf),cursor="hand2",fg="white",bg="#0b1335",font=("default",18),bd=5)
        sf.cl.place(x=910,y=370)
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

    def addressdetail(sf):
        return sf.city.get(),sf.loc.get(),sf.buil.get(),sf.hou.get(),sf.lan.get()

        
#--  page 14------
    def Orderde(sf,x,username):
        sf.x=x
##        sf.scr.destroy()
##        sf.scr=Tk()
##        sf.scr.geometry("1366x768")
##        sf.scr.title("Janta Restaurant")
##        sf.scr.iconbitmap('p.ico')
        sf.frmdes()
        #sf.scr.resizable(False, False)
        sf.f1=Frame(sf.scr,height=150,width=1366)
        sf.c=Canvas(sf.f1,height=150,width=1366)
        sf.c.pack()
        sf.logo=PhotoImage(file="logo.PNG")
        sf.c.create_image(683,75,image=sf.logo)
        sf.f1.pack(fill=BOTH,expand=1)
        sf.c.create_text(1000,70,text="WELCOME : ",fill="white",font=("default",20))
        sf.name=username
        sf.c.create_text(1150,70,text=sf.name,fill="white",font=("default",20))
        sf.home=Button(sf.f1,text="Log Out",command=lambda:sf.Login(),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.home.place(x=1150,y=100)
        sf.pd=Button(sf.f1,text=sf.x,command=lambda:sf.pickdev(sf.x),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.pd.place(x=1000,y=100)
        sf.cart(sf.x,username)
        sf.clock=Label(sf.f1,fg="white",font=("default",20),bg="#0b1335")
        sf.clock.place(x=920,y=10)
        sf.tick()
        sf.cart(sf.x,username)
        sf.f2=Frame(sf.scr,height=618,width=1366)
        sf.c=Canvas(sf.f2,height=618,width=1366)
        sf.c.pack()
        sf.logo1=PhotoImage(file="pizzamain.png")
        sf.c.create_image(683,309,image=sf.logo1)
        sf.log=Label(sf.f2,text="YOUR ORDER",bg="#9db1f2",font=("Cooper Black",22))
        sf.log.place(x=450,y=4)
        sf.c.create_rectangle(200, 50, 875, 550,fill="#d3ede6",outline="white",width=6)
        def listup():
            sf.con=connect("pizza.db")
            sf.cur=sf.con.cursor()
            try:
                sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
            except:
                pass
            x=sf.cur.execute("select count(*) from orderdetail")
            ordno="Order No. : "+str(list(x)[0][0]+1)
            sf.orde=Label(sf.f2,text=ordno,bg="#f2da9d",width=20,font=("Cooper Black",20))
            sf.orde.place(x=900,y=100)
            sf.amt=0
            for i in sf.cartlist:
                sf.amt+=i[-1]
            sf.ordtax="Tax : ₹ "+str("%.2f"%(sf.amt*0.05))
            sf.ordser="Serv. Char. : ₹ "+str("%.2f"%(sf.amt/99))
            sf.ordtot=sf.amt+sf.amt*0.05+sf.amt/99
            sf.ordt=Label(sf.f2,text=sf.ordtax,bg="#f2da9d",width=20,font=("Cooper Black",20))
            sf.ordt.place(x=900,y=150)
            sf.ords=Label(sf.f2,text=sf.ordser,bg="#f2da9d",width=20,font=("Cooper Black",20))
            sf.ords.place(x=900,y=200)
            sf.text="Total : ₹ "+str(int(sf.ordtot))
            sf.tot=Label(sf.f2,text=sf.text,bg="#f2da9d",width=20,font=("Cooper Black",20))
            sf.tot.place(x=900,y=250)
            sf.pay=Button(sf.f2,text="Pay",command=lambda:nozero(sf.amt),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
            sf.pay.place(x=1170,y=300)
            
            def nozero(x):
                if sf.amt==0:
                    messagebox.showinfo("Pay","Order Something")
                messagebox.showinfo("Pay","Payment Method is not available now")
            
            sf.exi=Button(sf.f2,text="Add more",command=lambda:sf.menulist(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
            sf.exi.place(x=930,y=300)
            def neword(x,username):
                sf.cartlist=[]
                sf.amount=0
                sf.menulist(sf.x,username)
            sf.newo=Button(sf.f2,text="Place New Order",command=lambda:neword(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",18,'bold'))
            sf.newo.place(x=980,y=400)
            sf.c.create_text(525,80,text="     Items\t      Size    Price    Qty",font=("Consolas",18,"bold","italic"))
            sf.c.create_text(525,85,text="_"*50,font=("cooper black",18))
            #sf.yaxis=110
        def listshow():
            listup()
            listbox=Frame(sf.f2,height=450,width=675)
            listbox.place(x=210,y=100)
            listNodes = Listbox(listbox,bg="#d3ede6",width=49,height=15,font=("Consolas", 18))
            listNodes.pack(side="left", fill="y")

            scrollbar = Scrollbar(listbox,orient="vertical")
            scrollbar.config(command=listNodes.yview)
            scrollbar.pack(side="right", fill="y")

            listNodes.config(yscrollcommand=scrollbar.set)
            c=0
            for j in sf.cartlist:
                c=c+1
                if len(j)==4:
                    sf.s="{:<3}{:<21}{:<9}{:<10}{}".format(str(c)+".",j[0],j[1],j[3],j[2])
                else:
                    sf.s="{:<3}{:<21}{:<9}{:<10}{}".format(str(c)+".",j[0],"  --  ",j[-1],j[-2])
                listNodes.insert(END,str(sf.s))
            def add(i):
                if int(sf.cartlist[i][-2])<100:
                    sf.cartlist[i][-1]+=sf.cartlist[i][-1]//int(sf.cartlist[i][-2])
                    sf.cartlist[i][-2]=str(int(sf.cartlist[i][-2])+1)
                    
                listshow()
            def sub(i):
                if int(sf.cartlist[i][-2])>1 :
                    sf.cartlist[i][-1]-=sf.cartlist[i][-1]//int(sf.cartlist[i][-2])
                    sf.cartlist[i][-2]=str(int(sf.cartlist[i][-2])-1)
                    #sf.cartlist[i][-1]-=sf.cartlist[i][-1]//len(sf.cartlist)
                listshow()
            def dell(i):
                sf.cartlist.pop(i)
                sf.cart(sf.x,username)
                listshow()
            def plmn(i,y1):
                b[i][0] =Button(sf.f2, text="+",font=("default",8),command=lambda:add(i))
                b[i][0].place(x=815,y=y1)
                if int(sf.cartlist[i][-2])==1:
                    b[i][1]=Button(sf.f2, text="⌦",font=("default",8),command=lambda:dell(i))
                    b[i][1].place(x=750,y=y1)
                else:
                    b[i][1]=Button(sf.f2, text="-",font=("default",8),command=lambda:sub(i))
                    b[i][1].place(x=755,y=y1)
            b=[[0]*2]*len(sf.cartlist)
            y1=106
            for i in range(len(sf.cartlist)):
                plmn(i,y1)
                y1+=29
        listshow()           
        sf.f2.pack(fill=BOTH,expand=1)
        sf.scr.mainloop()

 #-----  database-------               
    def logindatabase(sf):
        sf.credlog=sf.resultlog()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        try:
            sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
        except:
            pass
        x=sf.cur.execute("select count(*) from customer where username=%r"%(sf.credlog[0]))
        x=list(x)
        if x[0][0]==0:
            if sf.credlog[0]=="" or sf.credlog[1]=="":
                messagebox.showinfo("Login","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Login","You are Not Registered Yet")
            
        else:
            z=sf.cur.execute("select count(*) from customer where username=%r and password=%r"%(sf.credlog[0],sf.credlog[1]))
            z=list(z)
            if z[0][0]==0:
                messagebox.showinfo("Login","Enter the Correct Password")
            else:
                #y=sf.cur.execute("select first,last from customer where username=%r"%(sf.credlog[0]))
                #messagebox.showinfo("Login","You have Successfully Log In\nWelcome to the Janta Restaurant")            
                sf.pizmain(sf.credlog[0])

    def Regdatabase(sf):
        sf.credreg=sf.resultreg()
        if sf.credreg[0].isspace()==True or sf.credreg[1].isspace()==True or sf.credreg[2].isspace()==True or sf.credreg[3].isspace()==True or sf.credreg[4].isspace()==True or sf.credreg[5].isspace()==True or sf.credreg[0]=="" or sf.credreg[1]=="" or sf.credreg[2]=="" or sf.credreg[3]=="" or sf.credreg[4]=="" or sf.credreg[5]=="":
            messagebox.showinfo("Register","Empty Entry is not Allowed")
        else:
            if sf.credreg[2].isalpha()!=True or sf.credreg[3].isalpha()!=True:
                messagebox.showinfo("Name","Name must contain alphabat only") 
            elif sf.credreg[0]!=sf.credreg[0].split()[0]:
                messagebox.showinfo("Username","No space is Allowed")
            elif len(sf.credreg[1])<6:
                messagebox.showinfo("Password","Password must be of minimum 6 letter")
            elif not re.match(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',sf.credreg[4]):
                messagebox.showinfo("Email","Enter valid email address")
            elif sf.credreg[5].isdigit()!=True or len(sf.credreg[5])!=10:
                messagebox.showinfo("Mobile No.","Enter valid 10-digit Mobile No.")                
            else:
                sf.con=connect("pizza.db")
                sf.cur=sf.con.cursor()
                try:
                    sf.cur.execute("create table customer(username varchar(50) not null,password varchar(50) not null,first varchar(50) not null,last varchar(50) not null,email varchar(50),mob varchar(50) not null)")
                except:
                    pass
                x=sf.cur.execute("select count(*) from customer where username=%r or mob=%r or email=%r"%(sf.credreg[0],sf.credreg[5],sf.credreg[4]))
                if list(x)[0][0]==0:
                    sf.cur.execute("insert into customer values(%r,%r,%r,%r,%r,%r)"%(sf.credreg[0],sf.credreg[1],sf.credreg[2].capitalize(),sf.credreg[3].capitalize(),sf.credreg[4],sf.credreg[5]))
                    sf.con.commit()
                    messagebox.showinfo("Register","You are Successfully Registered")
                    sf.Login()
                else:
                    messagebox.showinfo("Register","You are Already Registered.. \nEnter New Username,Email and Mobile No.")
            
    def admindatabase(sf):
        sf.credadm=sf.resultadmin()
        sf.con=connect("pizza.db")
        sf.cur=sf.con.cursor()
        x=sf.cur.execute("select count(*) from employee where username=%r"%(sf.credadm[0]))
        x=list(x)
        if x[0][0]==0:
            if sf.credadm[0]=="" or sf.credadm[1]=="":
                messagebox.showinfo("Admin","Empty Entry is not allowed")
            else:
                messagebox.showinfo("Admin","You are Not Registered Yet")
            
        else:
            z=sf.cur.execute("select count(*) from employee where username=%r and password=%r"%(sf.credadm[0],sf.credadm[1]))
            z=list(z)
            if z[0][0]==0:
                messagebox.showinfo("Admin","Enter the Correct Password")
            else:
                y=sf.cur.execute("select empid from employee where username=%r"%(sf.credadm[0]))
                #messagebox.showinfo("Admin","You have Successfully Log In")            
                sf.adminmain(list(y)[0])

        

    def adminorderdetail(sf):
        sf.credadmord=sf.resultadminorder()
        q1=""
        for i in sf.credadmord[0].split():
            q1=q1+i
        if sf.credadmord[0]=="" or sf.credadmord[1]=="" or sf.credadmord[0].isspace()==True or sf.credadmord[1].isspace()==True:
            messagebox.showinfo("Attention","Enter Customer's Name and Mobile No")
        elif q1.isalpha()!=True:
                messagebox.showinfo("Attention","Name must contain alphabat only")
        elif sf.credadmord[1].isdigit()!=True or len(sf.credadmord[1])!=10:
                messagebox.showinfo("Mobile No.","Enter valid 10-digit Mobile No.")
        elif sf.money==0:
            messagebox.showinfo("Attention","Order Something and then press Total Button")
        else:
            if messagebox.askyesno("Pay","Want to make payment"):
                sf.con=connect("pizza.db")
                sf.cur=sf.con.cursor()
                od=[]
                try:
                    sf.cur.execute("create table orderdetail(id integer primary key,username varchar(50),name varchar(50),mobile varchar(50),money varchar(10) not null,address varchar ,orderdet varchar not null)")
                except:
                    pass
                for i in sf.credadmord[2:]:
                    if i[-1]=='0':
                        pass
                    else:
                        od.append(i)
                a=sf.credadmord[0]
                b=sf.credadmord[1]
                s="insert into orderdetail(name,mobile,money,orderdet) values(%r,%r,%r,%r)"%(a.capitalize(),b,str(sf.money),str(od))
                sf.cur.execute(s)
                sf.con.commit()
                messagebox.showinfo("Pay","Successfully Paid")
                sleep(2)
                messagebox.showinfo("New Order","Enter the Reset button to place New Order")


            
    def ordernow(sf,username):
        sf.credadd=sf.addressdetail()
        if sf.credadd[0].isspace()==True or sf.credadd[1].isspace()==True or sf.credadd[2].isspace()==True or sf.credadd[3].isspace()==True or sf.credadd[4].isspace()==True or sf.credadd[0]=="" or sf.credadd[1]=="" or sf.credadd[2]=="" or sf.credadd[3]=="" or sf.credadd[4]=="":
            messagebox.showinfo("Address","Empty Entry is not Allowed")
        else:
            sf.menulist(sf.x,username)


    def tick(sf):
        sf.time1=0
        sf.time2 = time.strftime('%b %d %Y %H:%M:%S')
        if sf.time2 != sf.time1:
            sf.time1 = sf.time2
            sf.clock.config(text=sf.time2)
        sf.clock.after(1000,sf.tick)

    def frmdes(sf):
        sf.f1.pack_forget()
        sf.f1.destroy()
        sf.f2.pack_forget()
        sf.f2.destroy()
    def pickdev(sf,x):
        sf.scr1=Toplevel()
        sf.scr1.title("Janta Restaurant")
        sf.scr1.geometry("750x300")
        sf.scr1.configure(background='black')
        sf.L1=Label(sf.scr1,bg = "black")
        sf.L1.pack()
        sf.L=Label(sf.scr1,font=("cooper black",22),bg = "#a854a1")
        sf.L.pack()
        sf.ff2=Frame(sf.scr1,height=150,width=1066,bg="black")
        sf.ff2.pack()
        sf.L2=Label(sf.ff2,bg = "black")
        sf.L2.pack()
        if x=="Delivery":
            sf.L.config(text="Delivery Address")
            ll=sf.credadd
            sf.ex=ll[2]+" "+ll[3]+"\n"+ll[4]+" "+ll[1]+"\n"+ll[0]
            sf.w2 = Label(sf.ff2,justify=CENTER,padx = 10,text=sf.ex,font="Helvetica 20 bold italic",fg = "light green",bg = "dark green").pack()
        else:
            sf.L.config(text="Pick Up Address")
            sf.ex="""MEDICAL SQUARE JHANSI U.P.

Right Side Part of Ground Floor Plot No 1317
Building No 14/A Ward No-29 Mouza Pichore
Kanpur Road Jhansi Uttar Pradesh 284002"""
            sf.w2 = Label(sf.ff2,justify=CENTER,padx = 10,text=sf.ex,font="Helvetica 20 bold italic",fg = "light green",bg = "dark green").pack()

    def cart(sf,x,username):
        sf.x=x
        sf.crt=Button(sf.f1,text="Cart"+"("+str(len(sf.cartlist))+")",command=lambda:sf.ordercheck(sf.x,username),bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
        sf.crt.place(x=850,y=100)
            
if __name__=="__main__":
    x=Pizza()
    x.main()
