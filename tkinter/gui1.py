from tkinter import*
from tkinter import messagebox
from db import Database
import tkinter

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row) 

def add_item():
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    populate_list()
    
def remove_item():
    print('Remove') 
    
def update_item():
    print('Update')
    
def clear_text():
    print('Clear text')

#Creating a window object
app = tkinter.Tk()

#Spare Part name
part_text = StringVar()
part_label = Label(app,text = "Part Name", font = ('bold', 12), pady = 20)
part_label.grid(row = 0, column = 0, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column = 1)

#Customer
customer_text = StringVar()
customer_label = Label(app,text = "Customer", font = ('bold', 12))
customer_label.grid(row = 0, column = 2, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = customer_text)
part_entry.grid(row = 0, column = 3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app,text = "Retailer", font = ('bold', 12))
retailer_label.grid(row = 1, column = 0, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = retailer_text)
part_entry.grid(row = 1, column = 1)

#Price
price_text = StringVar()
price_label = Label(app,text = "Price", font = ('bold', 12))
price_label.grid(row = 1, column = 2, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = price_text)
part_entry.grid(row = 1, column = 3)

#parts list
parts_list = Listbox(app, height = 8, width = 50, border = 0)
parts_list.grid(row = 3, column = 0, columnspan = 3, rowspan = 6, pady = 20, padx = 20)

#scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row = 3, column = 3)

#set scroll to listbox
parts_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = parts_list.yview)

#Buttons
add_btn = Button(app, text = 'Add Part', width = 12, command = add_item, bg = 'green', relief = RIDGE, bd = 4 )
add_btn.grid(row = 2, column = 0, pady = 20)

remove_btn = Button(app, text = 'Remove Part', width = 12, command = remove_item, activebackground = 'blue', relief = SUNKEN)
remove_btn.grid(row = 2, column = 1)

update_btn = Button(app, text = 'Update Part', width = 12, command = update_item, activeforeground = 'orange',relief = GROOVE)
update_btn.grid(row = 2, column = 2)

clear_btn = Button(app, text = 'Clear Input', width = 12, command = clear_text, fg = 'red', highlightcolor = 'brown', relief = RAISED)
clear_btn.grid(row = 2, column = 3)

#populate data
populate_list()

#start program
app.mainloop()