import tkinter as ttk
from tkinter import filedialog

class App(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.file = None
        self.frame = ttk.Frame(self, background="#1c1139", height=300, width=400) 
        self.button = ttk.Button(self.frame, text="apeshit mf")
        self.button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()