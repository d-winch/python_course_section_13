# from tkinter import *
#
# window = Tk()
#
# def km_to_miles():
#     miles = float(e1_value.get()) * 1.6
#     t1.insert(END, miles)
#
# b1 = Button(window, text="Execute", command=km_to_miles)
# b1.grid(row=0,column=0,columnspan=1)
#
# e1_value = StringVar()
#
# e1 = Entry(window, textvariable=e1_value)
# e1.grid(row=0,column=1)
#
# t1 = Text(window,height=1,width=20)
# t1.grid(row=0,column=2)
#
# window.mainloop()

from tkinter import *

window = Tk()

def kg_convert():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value,width=20)
e1.grid(row=0,column=0)

e1=Label(window,text="Kg")
e1.grid(row=0,column=1)

b1 = Button(window, text="Convert", command=kg_convert)
b1.grid(row=0,column=2,columnspan=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
