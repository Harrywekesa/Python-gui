from tkinter import *

app = Tk()
app.title('Label')
app.geometry('700x350')

var = StringVar()
label = Label(app, textvariable = var, relief = RIDGE)

var.set('Hey !? How are you doing?')
label.pack()
app.mainloop()