import os
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys
from PIL import Image, ImageTk

## functions for menus in attempt1.py

class colorwheel:
    def __init__(self, width=500, height=200):
        self.width = width
        self.height = height
        
        self.root = tk.Tk()

        self.left_panel = tk.Frame(self.root, width=width, height=height)
        self.left_panel.pack(side="left")

        self.right_panel = tk.Frame(self.root, width=width, height=height, background="#3a2865")
        self.right_panel.pack(side="right")

        #sliders
        self.scale1 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="r")
        self.scale2 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="g")
        self.scale3 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="b")
        self.scale1.grid(row= 0, column=1, pady=7)
        self.scale2.grid(row= 1, column=1, pady=7)
        self.scale3.grid(row= 2, column=1, pady=7)
        self.scale_data = self.get_scale_values()
        
        self.img_data = self.generate_gradient_image(width, height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)

        self.canvas = tk.Canvas(self.left_panel, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.bind("<Button-1>", self.get_color)
        
        #reset button
        self.reset_button = tk.Button(self.left_panel, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

        #side color panel
        self.label = tk.Label(self.right_panel, text="Click a color", font=("Arial", 14), width=20)
        self.label.grid(row=3, column=0, pady=10)

        self.label2 = tk.Label(self.right_panel, text="Color Mode", font=("Arial", 12), width=20)
        self.label2.grid(row=1, column=0)

        self.dropdown = tk.OptionMenu(self.right_panel, tk.StringVar(), "rgb", "hsv", "grayscale")
        self.dropdown.grid(row=2, column=0)

        
    def generate_gradient_image(self, width, height):
        img = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                r = self.scale_data[0]
                g = self.scale_data[1]
                b = self.scale_data[2]
                img.putpixel((x, y), (r, g, b))
        return img
    
    def reset(self):
        self.img_data = self.generate_gradient_image(self.width, self.height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)

        self.canvas = tk.Canvas(self.left_panel, width=self.width, height=self.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        print(self.scale_data[1])
    
    # def generate_gradient_image(self, width, height):
    #     img = Image.new("RGB", (width, height))
    #     for x in range(width):
    #         for y in range(height):
    #             r = int((x / width) * 255)
    #             g = int((y / height) * 255)
    #             b = self.scale_data[2]
    #             img.putpixel((x, y), (r, g, b))
    #     return img
    
    def get_scale_values(self):
        r = self.scale1.get()
        g = self.scale2.get()
        g = self.scale2.set(200)
        g = self.scale2.get()
        b = self.scale3.get()
        return r, g, b

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
        print(self.scale_data[2])
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


if __name__ == '__main__':    
    picker = colorwheel()
    picker.run()
    
        

