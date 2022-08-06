import tkinter as tk

def add_1_0():
    value = int(e1.get())
    value += 1
    e1.delete(0, 'end')
    e1.insert(0, value)

def add_0_1():
    value = int(e1.get())
    value -= 1
    e1.delete(0, 'end')
    e1.insert(0, value)

root = tk.Tk()

#entry box
e1 = tk.Entry(root)
e1.insert(0, 0) 
e1.pack()

#buttons
bt1 = tk.Button(root, text="+", command=add_1_0)
bt1.pack() 
bt2 = tk.Button(root, text="-", command=add_0_1)
bt2.pack()

root.mainloop()
