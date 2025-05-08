import tkinter as ttk
from tkinter import *
from commands.attempt1_coms import App_func

root = Tk()
root.title("embedded app")
# testing menu
# ++++++++++++++++++++++++++++++++++++++++
root.option_add("*Font", "Consolas")
root.option_add("*tearoff", FALSE)

# win = Toplevel(root)
menubar = Menu(root)

root["menu"] = menubar
root["background"] = "#1c1139"

menu_file = Menu(menubar)
menu_edit = Menu(menubar)

menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Edit", menu=menu_edit)

menu_file.add_command(label='New', command=lambda: print("new"))
menu_file.add_separator()
menu_file.add_command(label='Open', command=lambda: App_func().openfile)
menu_file.add_command(label='Save', command=lambda: print("save"))
menu_file.add_command(label='Exit', command=lambda: print("exit"))

# ++++++++++++++++++++++++++++++++++++++++

root.mainloop()