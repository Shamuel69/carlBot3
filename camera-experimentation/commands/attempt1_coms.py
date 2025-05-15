import os
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys
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



class ColorPicker(tk.Canvas):
    def __init__(self, master, width=200, height=200):
        super().__init__(master, width=width, height=height)
        self.width = width
        self.height = height
        self.hsv = (0, 0, 0)
        self.draw_gradient()
        self.bind("<Button-1>", self.get_color)

    def draw_gradient(self):
        for y in range(self.height):
            for x in range(self.width):
                hue = x / self.width
                saturation = 1.0
                value = y / self.heights
                r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
                self.create_rectangle(x, y, x + 1, y + 1, fill="#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255)))

    def get_color(self, event=None):
        x = event.x
        y = event.y
        h = x / self.width
        s = y / self.height
        v = 1
        self.hsv = (h,s,v)
        return self.hsv
        # self.master.label.config(text=f"H:{h*360:.2f}, S: {s*100:.2f}%, V: {v*100:.2f}%")
    @staticmethod
    def update_hsv_values(root, stringvar):
        hsv_values = ColorPicker(root).get_color()
        stringvar.set(f"H: {hsv_values[0]*360:.2f}, S: {hsv_values[1]*100:.2f}, V: {hsv_values[2]*100:.2f}%")


def color(self):
    color_chosen = colorchooser.askcolor(title="Select color")