from tkinter import *

app = Tk()
app.title('Checkbox items')
frame = Frame(app)
frame.pack()

bottomframe = Frame(app)
bottomframe.pack(side = BOTTOM)

redbutton = Button(frame, text = 'Red', fg ='black')
redbutton.pack(side = LEFT)

greenbutton = Button(frame, text = 'brown', fg = 'black')
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text = 'blue', fg = 'black')
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text = 'black', fg = 'white')
blackbutton.pack(side = BOTTOM)

app.mainloop()

