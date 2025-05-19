import os
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys
from PIL import Image, ImageTk

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



# class ColorPicker(tk.Canvas):
#     def __init__(self, master, width=300, height=200):
#         super().__init__(master, width=width, height=height)
#         self.width = width
#         self.height = height
#         self.hsv = (0, 0, 0)
#         self.draw_gradient()
#         self.bind("<Button-1>", self.get_color)

#     def draw_gradient(self):
#         for y in range(self.height):
#             for x in range(self.width):
#                 hue = x / self.width
#                 saturation = 0
#                 value = y / self.height
#                 r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
#                 self.create_rectangle(x, y, x + 1, y + 1, fill="#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255)))
class colorwheel:
    def __init__(self, width=300, height=200):
        self.width = width
        self.height = height
        
        self.root = tk.Tk()
        self.img_data = self.generate_gradient_image(width, height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)


        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.bind("<Button-1>", self.get_color)
        
        self.label = tk.Label(self.root, text="Click a color", font=("Arial", 14), width=20)
        self.label.pack(pady=10)
        
    def generate_gradient_image(self, width, height):
        img = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                r = int((x / width) * 255)
                g = int((y / height) * 255)
                b = 150
                img.putpixel((x, y), (r, g, b))
        return img
    
    def get_color(self, event):
        x, y = event.x, event.y
        if 0 <= x < self.width and 0 <= y < self.height:
            rgb = self.img.getpixel((x, y))
            hex_color = '#%02x%02x%02x' % rgb
            print(f"selected color: {hex_color}")
            self.label.config(text=f"selected color: {hex_color}")

    def run(self):
        self.root.mainloop()


    # def get_color(self, event=None):
    #     x = event.x
    #     y = event.y
    #     h = x / self.width
    #     s = y / self.height
    #     v = 1
    #     self.hsv = (h,s,v)
    #     print(self.hsv)
    #     return self.hsv
    #     # self.master.label.config(text=f"H:{h*360:.2f}, S: {s*100:.2f}%, V: {v*100:.2f}%")



picker = colorwheel()
picker.run()