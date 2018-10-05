from tkinter import *

# Create window
window=Tk()

def from_kg():
    # get the vallue of e1_value
    # print(e1_value.get())
    grams=float(e2_value.get())*1000
    pounds=float(e2_value.get())*2.20462
    ounces=float(e2_value.get())*35.274
    # adding value of e1_value to text widget at the end of the text
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

e2_value = StringVar()
# put input field in window
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0,column=1)

# Creating button to put in window
b1=Button(window,text='Convert',command=from_kg)
# putting button into the window panel
# b1.pack()

# putting button into the window panel using grid
b1.grid(row=0,column=3)


# put text widget
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

# end of the window
window.mainloop()
