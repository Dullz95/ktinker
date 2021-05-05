from tkinter import *


def add_numbers():
    r = int(e1.get())+int(e2.get())
    e3.insert(0, r)


def clear():
    e1.delete(0)
    e2.delete(0)


root = Tk()

#Put onto screen

root.geometry("500x150")
root.title("Adding Numbers")

label_text = StringVar()
Label(root, text="Enter First Number:").grid(row=0, sticky=W)
Label(root, text="Enter Second Number:").grid(row=1, sticky=W)
Label(root, text="Result of Addition:").grid(row=3, sticky=W)
result = Label(root, text="", textvariable=label_text).grid(row=3, column=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=3, column=1)

b = Button(root, text="Add", command=add_numbers)
b1 = Button(root, text="Clear", command=clear)
b2 = Button(root, text="Exit", command=root.destroy)
b.grid(row=5, column=1, sticky=W+E+N+S, padx=5, pady=5)
b1.grid(row=5, column=2, sticky=W+E+N+S, padx=5, pady=5)
b2.grid(row=5, column=3, sticky=W+E+N+S, padx=5, pady=5)

# run program

mainloop()