import tkinter as ttk
from tkinter import *
import cv2

root = Tk()
root.title("GOGTEST")

content = ttk.Frame(root, background="#1c1139", height=300, width=400)
frame = ttk.Frame(content, relief=SUNKEN, borderwidth=2, background="grey", height=100, width=400)
namelbl = ttk.Label(content, text="MYNAMEGREG")
name = ttk.Entry(content)


onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(False)
twovar.set(False)
threevar.set(False)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# content.grid(column=0, row=0, sticky=(N,S,E,W))

box = ttk.Canvas(root, height=300, width=400, background="#1c1139")
button = ttk.Button(root, text="Hello", width=200, height=100, command=lambda: print("hello"))
button.place(x=100, y=50, anchor='center')
box.pack()

# frame.grid(column=0, row=0, columnspan=4, rowspan=4, padx=5, sticky=(N, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N,E,W), padx=5, pady=5)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)


# frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# label = ttk.Label(root, text="Hello World")
# ttk.Button(root, text="hello").grid(column=20)
# label.pack()s

root.mainloop()

    