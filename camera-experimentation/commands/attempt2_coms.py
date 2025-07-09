import tkinter as tk
from PIL import Image, ImageTk

class colorwheel:
    def __init__(self, width=500, height=200):
        self.width = width
        self.height = height

        self.root = tk.Tk()

        self.left_panel = tk.Frame(self.root, width=width, height=height)
        self.left_panel.pack(side="left")

        self.right_panel = tk.Frame(self.root, width=width, height=height, background="#3a2865")
        self.right_panel.pack(side="right")

        self.color_canvas = tk.Label(self.right_panel, width=width*.75, height=75, background="#000000", command=self.get_color)
        self.color_canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


        #sliders
        self.scale1 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="r")
        self.scale2 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="g")
        self.scale3 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="b")
        self.scale1.grid(row= 2, column=1, pady=7)
        self.scale2.grid(row= 3, column=1, pady=7)
        self.scale3.grid(row= 4, column=1, pady=7)

        self.img_data = self.generate_gradient_image(width, height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)

        self.canvas = tk.Canvas(self.left_panel, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.bind("<Button-1>", self.get_color)

        self.label = tk.Label(self.right_panel, text="Click a color", font=("Arial", 14), width=20)
        self.label.grid(row=3, column=0, pady=10)

    def grab_color(self):
        
        r,g,b = self.scale1.get(), self.scale2.get(), self.scale3.get()      
        hex_color = '#%02x%02x%02x' % r % g % b
        self.label.config(text=f"R: {r}, G: {g}, B: {b}")
        self.color_canvas.config(background=hex_color, fontcolor=hex_color)

    def generate_gradient_image(self, width, height):
        img = Image.new("RGB", (width, height))
        for x in range(width):
            for y in range(height):
                fx = x / (width - 1)
                fy = y / (height - 1)

                r = (1 - fx)*(1 - fy)*255 + fx*(1 - fy)*0 + (1 - fx)*fy*0 + fx*fy*255
                g = (1 - fx)*(1 - fy)*0 + fx*(1 - fy)*255 + (1 - fx)*fy*0 + fx*fy*255
                b = (1 - fx)*(1 -fy)*0 + fx*(1 - fy)*0 + (1 - fx)*fy*255 + fx*fy*255
                img.putpixel((x, y), (int(r), int(g), int(b)))
        return img

    # def generate_gradient_image(self, width, height):
    #     img = Image.new("RGB", (width, height))
    #     for x in range(width):
    #         for y in range(height):
    #             r = int((1-x / (width*.8)) * 255)
    #             g = int((x / (width/.9)) * 255)
    #             b = int((y / height*1.2) * 255)
    #             img.putpixel((x, y), (r, g, b))
    #     return img
    
    def get_color(self, event):
        x, y = event.x, event.y
        if 0 <= x < self.width and 0 <= y < self.height:
            rgb = self.img_data.getpixel((x, y))
            hex_color = '#%02x%02x%02x' % rgb
            print(f"selected color: {hex_color}")
            self.label.config(text=f"selected color: {hex_color}")
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':    
    picker = colorwheel()
    picker.run()


