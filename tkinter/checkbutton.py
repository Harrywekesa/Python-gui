from tkinter import *

app = Tk()
app.title('Checkbutton')
app.geometry('700x350')

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(app, text = "Music", width = 20, onvalue = 1)
C2 = Checkbutton(app, text = "Video", width = 20, onvalue = 1)

C1.pack()
C2.pack()

l1 = Label(app, text = "User name")
l1.pack(side = LEFT)

E1 = Entry(app, bd = 5)
E1.pack(side = RIGHT)

app.mainloop()