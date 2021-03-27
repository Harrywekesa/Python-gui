from tkinter import*
from tkinter import messagebox

app = Tk()
app.geometry('700x350')

def helloCallBack():
    messagebox.showinfo("Hello Python", helloCallBack())
    
B = Button(app, text = "Hello", bg = 'purple')
B.grid(row = 7)
app.mainloop()
    