from tkinter import*

#Creating a window object
app = Tk()

#Part
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

part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 0, column = 3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app,text = "Retailer", font = ('bold', 12))
retailer_label.grid(row = 1, column = 0, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 1, column = 1)

#Price
price_text = StringVar()
price_label = Label(app,text = "Price", font = ('bold', 12))
price_label.grid(row = 1, column = 2, sticky = W)
app.title('Tkinter Gui')
app.geometry('700x350')

part_entry = Entry(app, textvariable = part_text)
part_entry.grid(row = 1, column = 3)

#start program
app.mainloop()