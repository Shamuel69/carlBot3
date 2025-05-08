import os
import tkinter as tk
from tkinter import filedialog
## functions for menus in attempt1.py

class App_func:
    def __init__(self):
        self.openfile = self.open()

    def open(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

        # filedialog.askopenfilename()
        print(f"file_path: {file_path}")