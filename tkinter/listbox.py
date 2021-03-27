from tkinter import *
import tkinter

app = Tk()
app.title('Listbox')
app.geometry('700x350')
app

Lb1 = Listbox(app, selectmode = EXTENDED, background = 'black', fg = 'green',cursor = 'circle', bg = "black", relief = RIDGE, selectbackground = 'red')
Lb1.insert(1, 'Python')
Lb1.insert(2, 'Perl')
Lb1.insert(3, 'C')
Lb1.insert(4, 'PHP')
Lb1.insert(5, 'JSP')
Lb1.insert(6, 'Ruby')


Lb1.grid()
app.mainloop()