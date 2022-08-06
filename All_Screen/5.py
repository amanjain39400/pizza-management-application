from tkinter import *
import random
import time
root = Tk()
#root.config(bg="#f2e8b8")
root.title("Janta Restaurant")
root.geometry("1366x768")

fr=Frame(root,bg="#f2e8b8",height=150,width=1366)
fr.pack(side=TOP,fill=BOTH)
c=Canvas(fr,height=150,bg="#f2e8b8",width=1366)
c.pack()
logo=PhotoImage(file="../logo2.png")
c.create_image(683,50,image=logo)
home=Button(fr,text="Home",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
home.place(x=1100,y=25)
localtime=time.asctime(time.localtime(time.time()))
c.create_text(900,50,text=localtime,fill="white",font=("default",16))
c.create_text(683,125,font=( 'Cooper Black' ,25, 'bold','underline' ),text="Management System")
out=Button(fr,text="Log Out",bg="#0b1335",cursor="hand2",fg="white",bd=5,font=("default",16,'bold'))
out.place(x=1200,y=25)

def Ref():
    x=random.randint(100, 500)
    randomRef = str(x)
    order.set(randomRef)

    v1=vp1.get()
    if v1=="Medium":
        p1=float(Deluxe_Veggie.get())*450
    elif v1=="Large":
        p1=float(Deluxe_Veggie.get())*650
    else:
        p1=float(Deluxe_Veggie.get())*250
    v2=vp2.get()
    if v2=="Medium":
        p2= float(Veg_Vaganza.get())*400
    elif v2=="Large":
        p2= float(Veg_Vaganza.get())*600
    else:
        p2= float(Veg_Vaganza.get())*250
    v3=vp3.get()
    if v3=="Medium":
        p3= float(Pepper.get())*385
    elif v3=="Large":
        p3= float(Pepper.get())*550
    else:
        p3= float(Pepper.get())*225
    v4=vp4.get()
    if v4=="Medium":
        p4= float(Margherita.get())*195
    elif v4=="Large":
        p4= float(Margherita.get())*385
    else:
        p4= float(Margherita.get())*99
    v5=vp5.get()
    if v5=="Medium":
        p5= float(Non_Veg_Supreme.get())*450
    elif v5=="Large":
        p5= float(Non_Veg_Supreme.get())*650
    else:
        p5= float(Non_Veg_Supreme.get())*250
    v6=vp6.get()
    if v6=="Medium":
        p6= float(Chicken_Tikka.get())*400
    elif v6=="Large":
        p6= float(Chicken_Tikka.get())*600
    else:
        p6= float(Chicken_Tikka.get())*225
    v7=vp7.get()
    if v7=="Medium":
        p7= float(Chicken_Sausage.get())*385
    elif v7=="Large":
        p7= float(Chicken_Sausage.get())*550
    else:
        p7= float(Chicken_Sausage.get())*225
    v8=vp8.get()
    if v8=="Medium":
        p8= float(Chicken_Peri.get())*195
    elif v8=="Large":
        p8= float(Chicken_Peri.get())*385
    else:
        p8= float(Chicken_Peri.get())*99
    p9= float(Roasted_Chicken.get())*109
    p10= float(Chicken_Meatballs.get())*99
    p11= float(Boneles_sChicken.get())*139
    p12= float(Coke_Mobile.get())*45
    p13= float(Burger_Pizza.get())*99
    p14= float(White_Pasta.get())*135
    
    costofmeal = "Rs.",str('%.2f'% (p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14))
    PayTax=((p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14)*.05)
    Totalcost=(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14)
    Ser_Charge=((p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( '%.2f'%(PayTax + Totalcost + Ser_Charge))
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    Deluxe_Veggie.set("0")
    Veg_Vaganza.set("0")
    Pepper.set("0")
    Margherita.set("0")
    Non_Veg_Supreme.set("0")
    Chicken_Tikka.set("0")
    Chicken_Sausage.set("0")
    Chicken_Peri.set("0")
    Coke_Mobile.set("0")
    Burger_Pizza.set("0")
    White_Pasta.set("0")
    Roasted_Chicken.set("0")
    Chicken_Meatballs.set("0")
    Boneles_sChicken.set("0")
    Total.set("0")
    Service_Charge.set("0")
    Tax.set("0")
    cost.set("0")
    order.set("0")
    vp1.set("Medium")
    vp2.set("Medium")
    vp3.set("Medium")
    vp4.set("Medium")
    vp5.set("Medium")
    vp6.set("Medium")
    vp7.set("Medium")
    vp8.set("Medium")

    

def price():
    roo = Tk()
    roo.geometry("600x768+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="Veg Pizza", fg="black", anchor=W)
    lblinfo.grid(row=1, column=1)
    lblinfo = Label(roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
    lblinfo.grid(row=1, column=2)
    lblinfo = Label(roo, font=('aria', 18, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Deluxe Veggie", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Veg Vaganza", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="5 Pepper", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Margherita", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Non-Veg Pizza", fg="black", anchor=W)
    lblinfo.grid(row=6, column=1)
    lblinfo = Label(roo, font=('aria', 15), text="(Medium/Large/Regular)", fg="black", anchor=W)
    lblinfo.grid(row=6, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Non-Veg Supreme", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹450/₹650/₹250", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Tikka", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹400/₹600/₹250", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Suasage", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹385/₹550/₹225", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Peri", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹195/₹385/₹99", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Specialty Chicken", fg="black", anchor=W)
    lblinfo.grid(row=11, column=1)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Roasted Chicken", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹109", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Meatballs", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Boneless Chicken", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹139", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Sides & Beverages", fg="black", anchor=W)
    lblinfo.grid(row=15, column=1)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coke Mobile", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹45", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Pizza", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹99", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="White Pasta", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="₹135", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=2)

    roo.mainloop()




f1 = Frame(root,width =1366,bg="#f2e8b8",height=618,relief=SUNKEN)
f1.pack(side=BOTTOM,fill=BOTH,expand=1)
Deluxe_Veggie= StringVar()
Veg_Vaganza = StringVar()
Pepper = StringVar()
Margherita= StringVar()
Non_Veg_Supreme = StringVar()
Chicken_Tikka = StringVar()
Chicken_Sausage= StringVar()
Chicken_Peri= StringVar()
Coke_Mobile = StringVar()
Burger_Pizza = StringVar()
White_Pasta = StringVar()
Roasted_Chicken= StringVar()
Chicken_Meatballs = StringVar()
Boneles_sChicken = StringVar()
Total = StringVar()
Service_Charge= StringVar()
Tax = StringVar()
cost = StringVar()
order=StringVar()
vp1=StringVar()
vp2=StringVar()
vp3=StringVar()
vp4=StringVar()
vp5=StringVar()
vp6=StringVar()
vp7=StringVar()
vp8=StringVar()
reset()
l=["Medium","Large","Regular"]

#veg pizza
non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=0,column=1)
lbl1 = Label(f1,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Veg Pizza",bd=10,anchor='w')
lbl1.place(x=180,y=0)
lbl11 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
lbl11.grid(row=1,column=0)
lbl12 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
lbl12.grid(row=1,column=1)
lbl13 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
lbl13.grid(row=1,column=2,padx=4)

lbldel= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Deluxe Veggie:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lbldel.grid(row=2,column=0)
opdel=OptionMenu(f1,vp1,*l)
opdel.config(width=6)
opdel.grid(row=2,column=1)
txtdel= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Deluxe_Veggie , bd=6,width=4,bg="powder blue" ,justify='right')
txtdel.grid(row=2,column=2)

lblvaga = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Veg Vaganza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblvaga.grid(row=3,column=0)
opvaga=OptionMenu(f1,vp2,*l)
opvaga.config(width=6)
opvaga.grid(row=3,column=1)
txtvaga = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Veg_Vaganza , bd=6,width=4,bg="powder blue" ,justify='right')
txtvaga.grid(row=3,column=2)

lblpep= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text=" 5 Pepper:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblpep.grid(row=4,column=0)
oppep=OptionMenu(f1,vp3,*l)
oppep.config(width=6)
oppep.grid(row=4,column=1)
txtpep= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pepper ,bd=6,width=4,bg="powder blue" ,justify='right')
txtpep.grid(row=4,column=2)

lblmag = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Margherita:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblmag.grid(row=5,column=0)
opmag=OptionMenu(f1,vp4,*l)
opmag.config(width=6)
opmag.grid(row=5,column=1)
txtmag = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Margherita,width=4,bg="powder blue",bd=6 ,justify='right')
txtmag.grid(row=5,column=2)


#non veg
non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=6,column=1)
lbl2 = Label(f1,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Non-Veg Pizza",bd=10,anchor='w')
lbl2.place(x=150,y=270)
lbl21 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
lbl21.grid(row=7,column=0)
lbl22 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=7,bg="#f2e8b8",text="Size",bd=6,anchor='w')
lbl22.grid(row=7,column=1)
lbl23 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
lbl23.grid(row=7,column=2)

lblsup= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Non-Veg Supreme:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblsup.grid(row=8,column=0)
opsup=OptionMenu(f1,vp5,*l)
opsup.config(width=6)
opsup.grid(row=8,column=1)
txtsup= Entry(f1,width=4,font=('ariel' ,16,'bold'), textvariable=Non_Veg_Supreme , bd=6,bg="powder blue" ,justify='right')
txtsup.grid(row=8,column=2)

lbltika = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Tikka:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lbltika.grid(row=9,column=0)
optika=OptionMenu(f1,vp6,*l)
optika.config(width=6)
optika.grid(row=9,column=1)
txttika = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Chicken_Tikka , bd=6,width=4,bg="powder blue" ,justify='right')
txttika.grid(row=9,column=2)

lblsaus= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Sausage:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblsaus.grid(row=10,column=0)
opsaus=OptionMenu(f1,vp7,*l)
opsaus.config(width=6)
opsaus.grid(row=10,column=1)
txtsaus= Entry(f1,width=4,font=('ariel' ,16,'bold'), textvariable=Chicken_Sausage , bd=6,bg="powder blue" ,justify='right')
txtsaus.grid(row=10,column=2)

lblperi = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken Peri:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblperi.grid(row=11,column=0)
opperi=OptionMenu(f1,vp8,*l)
opperi.config(width=6)
opperi.grid(row=11,column=1)
txtperi= Entry(f1,font=('ariel' ,16,'bold'),width=4, textvariable=Chicken_Peri , bd=6,bg="powder blue" ,justify='right')
txtperi.grid(row=11,column=2)

#Special
non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=0,column=5)
lbl3 = Label(f1,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Specialty",bd=10,anchor='w')
lbl3.place(x=550,y=0)
lbl31 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
lbl31.grid(row=1,column=4)
lbl33 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
lbl33.grid(row=1,column=5)

lblros= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Roasted Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblros.grid(row=2,column=4)
txtros= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Roasted_Chicken , bd=6,width=4,bg="powder blue" ,justify='right')
txtros.grid(row=2,column=5)

lblmeat = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Chicken_Meatballs:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblmeat.grid(row=3,column=4)
txtmeat = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Chicken_Meatballs , bd=6,width=4,bg="powder blue" ,justify='right')
txtmeat.grid(row=3,column=5)

lblbon= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Boneless Chicken:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblbon.grid(row=4,column=4)
txtbon= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Boneles_sChicken,bd=6,width=4,bg="powder blue" ,justify='right')
txtbon.grid(row=4,column=5)

#Sides
non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=6,column=4)
lbl4 = Label(f1,pady=2, font=( 'Cooper Black' ,20, 'bold','underline' ),bg="#f2e8b8",text="Sides & Beverages",bd=10,anchor='w')
lbl4.place(x=500,y=270)
lbl41 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=6,bg="#f2e8b8",text="Items",bd=6,anchor='w')
lbl41.grid(row=7,column=4)
lbl43 = Label(f1,pady=2, font=( 'Cooper Black' ,16,'underline' ),width=8,bg="#f2e8b8",text="Quantity",bd=6,anchor='w')
lbl43.grid(row=7,column=5)

lblcok= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Coke Mobile:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblcok.grid(row=8,column=4)
txtcok= Entry(f1,width=4,font=('ariel' ,16,'bold'), textvariable=Coke_Mobile , bd=6,bg="powder blue" ,justify='right')
txtcok.grid(row=8,column=5)

lblbur = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Burger Pizza:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblbur.grid(row=9,column=4)
txtbur = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger_Pizza , bd=6,width=4,bg="powder blue" ,justify='right')
txtbur.grid(row=9,column=5)

lblpas= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="White Pasta:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblpas.grid(row=10,column=4)
txtpas= Entry(f1,width=4,font=('ariel' ,16,'bold'), textvariable=White_Pasta , bd=6,bg="powder blue" ,justify='right')
txtpas.grid(row=10,column=5)

#bill
non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=3,column=8)
lbl5 = Label(f1,pady=2, font=( 'Cooper Black' ,22, 'bold','underline' ),bg="#f2e8b8",text="Bill Payment",bd=10,anchor='w')
lbl5.place(x=1050,y=140)

non=Label(f1,pady=2,text=(" "),font=( 'Cooper Black' ,20),width=5,bg="#f2e8b8",bd=10,anchor='w')
non.grid(row=4,column=6)
lblord= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),width=10,text="Order No:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblord.grid(row=4,column=7)
txtord= Entry(f1,font=('ariel' ,16,'bold'), textvariable=order , bd=6,width=14,bg="powder blue" ,justify='right')
txtord.grid(row=4,column=8)

lblco = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Subtotal:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblco.grid(row=5,column=7)
txtco = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost,width=14,bd=6,bg="powder blue" ,justify='right')
txtco.grid(row=5,column=8)

lblser= Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Service Charge:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lblser.grid(row=6,column=7)
txtser= Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge ,width=14,bd=6,bg="powder blue" ,justify='right')
txtser.grid(row=6,column=8)

lbltax = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Tax:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lbltax.grid(row=7,column=7)
txttax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax, bd=6,width=14,bg="powder blue" ,justify='right')
txttax.grid(row=7,column=8)

lbltot = Label(f1,pady=2, font=( 'aria' ,16, 'bold' ),text="Total:",bg="#f2e8b8",fg="#7769ad",bd=6,anchor='w')
lbltot.grid(row=8,column=7)
txttot = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total, bd=6,width=14,bg="powder blue" ,justify='right')
txttot.grid(row=8,column=8)

btnprice=Button(f1,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="PRICE", bg="powder blue",command=price)
btnprice.place(x=970,y=440)

btnTotal=Button(f1,pady=2,bd=6,fg="black",font=('ariel' ,16,'bold'),width=6, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.place(x=1160,y=440)

btnreset=Button(f1,pady=2,bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=reset)
btnreset.place(x=970,y=500)

btnexit=Button(f1,pady=2, bd=6 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=qexit)
btnexit.place(x=1160,y=500)

root.mainloop()


