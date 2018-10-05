from tkinter import *

# Create window
window=Tk()

def km_to_miles():
    # get the vallue of e1_value
    print(e1_value.get())
    miles=float(e1_value.get())/1.6
    # adding value of e1_value to text widget at the end of the text
    t1.insert(END, miles)
# Creating button to put in window
b1=Button(window,text='Execute',command=km_to_miles)
# putting button into the window panel
# b1.pack()

# putting button into the window panel using grid
b1.grid(row=0,column=0)

e1_value=StringVar()
# put input field in window
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

# put text widget
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

# end of the window
window.mainloop()
