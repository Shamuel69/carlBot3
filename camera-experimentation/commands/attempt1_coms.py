import os
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys
from PIL import Image, ImageTk

## functions for menus in attempt1.py

# class App_func:
#     def __init__(self):
#         self.Rnum = 



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
    def __init__(self, width=500, height=200):
        self.width = width
        self.height = height
        
        self.root = tk.Tk()

        self.left_panel = tk.Frame(self.root, width=width, height=height)
        self.left_panel.pack(side="left")

        self.right_panel = tk.Frame(self.root, width=width, height=height, background="#3a2865")
        self.right_panel.pack(side="right")

        self.img_data = self.generate_gradient_image(width, height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)


        self.canvas = tk.Canvas(self.left_panel, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.bind("<Button-1>", self.get_color)
        
        #side color panel
        self.label = tk.Label(self.right_panel, text="Click a color", font=("Arial", 14), width=20)
        self.label.grid(row= 0, column=0, pady=10)

        self.label2 = tk.Label(self.right_panel, text="Color Mode", font=("Arial", 12), width=20)
        self.label2.grid(row= 1, column=0)

        #sliders
        self.scale1 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="gog")
        self.scale2 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, )
        self.scale3 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, )
        self.scale1.grid(row= 0, column=1, pady=7)
        self.scale2.grid(row= 1, column=1, pady=7)
        self.scale3.grid(row= 2, column=1, pady=7)

        self.dropdown = tk.OptionMenu(self.right_panel, tk.StringVar(), "rgb", "hsv", "grayscale")
        self.dropdown.grid(row= 2, column=0)

        
    def generate_gradient_image(self, width, height):
        img = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                r = int((x / width) * 255)
                g = int((y / height) * 255)
                b = 225
                img.putpixel((x, y), (r, g, b))
        return img
    
    def get_color(self, event):
        x, y = event.x, event.y
        if 0 <= x < self.width and 0 <= y < self.height:
            rgb = self.img_data.getpixel((x, y))
            hex_color = '#%02x%02x%02x' % rgb
            print(f"selected color: {hex_color}")
            self.label.config(text=f"selected color: {hex_color}")
    
    def colorset(self):
        print(self.dropdown.get())
        if self.dropdown.get() == "rgb":
            self.label2.config(text="RGB")
        elif self.dropdown.get() == "hsv":
            self.label2.config(text="HSV")
        elif self.dropdown.get() == "grayscale":
            self.label2.config(text="Grayscale")
        #make an adjustable rgb slider that changes the color

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