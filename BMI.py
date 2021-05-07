import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("BMI")

root.geometry("750x500")
answer1 = StringVar()
answer2 = StringVar()
celsius = StringVar()
fahrenheit = StringVar()

cel = Label(root, text= "temp in celsius: ").place(x=10, y=10)
entry1 = Entry(root, textvariable= celsius).place(x=200, y=10)
label_name=Label(root, text="Answer: ").place(x=10, y=50)
entry_name =Entry(root, textvariable= answer1, state="readonly").place(x=200, y=50)


far = Label(root, text = "temp in fahrenheit: ").place(x=10, y=150)
entry2 = Entry(root, textvariable= fahrenheit).place(x=200, y=150)
label_name2 = Label(root, text="Answer: ").place(x=10, y=200)
entry_name2= Entry(root, textvariable= answer2, state="readonly").place(x=200, y=200)

def conv_c():
    f=int(celsius.get()) * (9/5) + 32
    answer1.set(f)

def conv_f():
    c=(int(fahrenheit.get()) -32) * 5/9
    answer2.set(c)
def clear():


convert_c = Button(root, text="Convert", command=conv_c).place(x=150, y=80)
convert_f = Button(root, text="Convert", command=conv_f).place(x=150, y=250)
root.mainloop()