from tkinter import *

root = Tk()
xscrollbar = Scrollbar(root,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
yscrollbar = Scrollbar(root, orient=VERTICAL)
yscrollbar.pack( side = RIGHT, fill=Y )

w = Label(root, text="Label: Aman Jain")#some label

mylist = Listbox(root,yscrollcommand = yscrollbar.set,xscrollcommand = xscrollbar.set )
for line in range(100):
   mylist.insert(END, w.cget("text") + str(line))

mylist.pack( side = LEFT, fill = BOTH )
xscrollbar.config( command = mylist.xview )
yscrollbar.config( command = mylist.yview )

mainloop()


#self.xscrollbar = Scrollbar(self.root, orient=HORIZONTAL, command=self.canvas.xview)
##self.xscrollbar.pack(side=BOTTOM, fill=X)
##self.yscrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
##self.yscrollbar.pack(side=RIGHT, fill=Y)

# Attach canvas to scrollbars
##self.canvas.configure(xscrollcommand=self.xscrollbar.set)
##self.canvas.configure(yscrollcommand=self.yscrollbar.set)
