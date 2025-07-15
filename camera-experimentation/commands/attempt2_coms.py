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
        
        #states and values
        self.color_id = None
        self.color_values = None
        self.value_ticker = 0
        self.upper_color = None
        self.lower_color = None

        self.camera_settings = {"GaussianBlur": None, "MedianBlur": None,"MorphologicalGradient": None, 
                                 "Closing": None, "Opening": None, "Erosion": None, "Dilation": None,
                                 "BilateralFilter": None, "tophat": None, "blackhat": None } 
        
        #sliders
        self.scale1 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="r", command=lambda x: self.updateblock())
        self.scale2 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="g", command=lambda x: self.updateblock())
        self.scale3 = tk.Scale(self.right_panel, from_=0, to=255, orient="horizontal", length=150, label="b", command=lambda x: self.updateblock())
        self.scale1.grid(row= 2, column=1, pady=7)
        self.scale2.grid(row= 3, column=1, pady=7)
        self.scale3.grid(row= 4, column=1, pady=7)

        #color preview
        self.img_data = self.grab_color()
        self.photo_image = ImageTk.PhotoImage(self.img_data)

        self.color_canvas = tk.Canvas(self.right_panel, width=375, height=75)
        self.color_canvas.grid(row=1, column=1)
        self.color_canvas.image = self.photo_image

        #left image
        self.img_data = self.generate_gradient_image(width, height)
        self.photo_image = ImageTk.PhotoImage(self.img_data)

        self.canvas = tk.Canvas(self.left_panel, width=width, height=height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)
        self.canvas.image = self.photo_image
        self.canvas.bind("<Button-1>", self.get_color)

        #text labels
        self.label = tk.Label(self.right_panel, text="Click a color", font=("Arial", 10), width=20)
        self.label.grid(row=2, column=0, pady=5)

        self.rgb_label = tk.Label(self.right_panel, text="RGB: ", font=("Arial", 10), width=20)
        self.rgb_label.grid(row=3, column=0, pady=5)

        ##color labels
        self.uppercolor_label = tk.Label(self.right_panel, text="upper color: ", font=("Arial", 8), width=25, background="#3a2865", fg="white")
        self.uppercolor_label.grid(row=4, column=0, pady=2)

        self.lowercolor_label = tk.Label(self.right_panel, text="lower color: ", font=("Arial", 8), width=25, background="#3a2865", fg="white")
        self.lowercolor_label.grid(row=5, column=0, pady=2)

        #buttons
        self.store_button = tk.Button(self.right_panel, text="store color", font=("Arial", 10), width=10, command=self.store_color)
        self.store_button.grid(row=5, column=1, pady=5)

        self.start_button = tk.Button(self.right_panel, text="start machine", font=("Arial", 10), width=10, command=print("part 2"))
        self.start_button.grid(row=6, column=1, pady=5)

        self.onevar = tk.BooleanVar()
        self.twovar = tk.BooleanVar()
        self.threevar = tk.BooleanVar()
        self.fourvar = tk.BooleanVar()
        self.fivevar = tk.BooleanVar()
        self.sixvar = tk.BooleanVar()
        self.sevenvar = tk.BooleanVar()
        self.eightvar = tk.BooleanVar()
        
        self.dropdown = tk.Menu(self.root)
        self.dropdown_var = tk.StringVar() # <- make function that updates this accordingly 
        self.dropdown = tk.OptionMenu(self.right_panel, self.dropdown_var, "Erosion", "Dilation", "Opening (Erosion -> Dilation)", "Closing (Dilation -> Erosion)")
        
        self.one = tk.Checkbutton(self.right_panel, text="Blur", variable=self.onevar, onvalue=True)
        #make second dropdown that tells about which one to use: top hat or black hat, or render both (cpu intensive)

        self.dropdownHats = tk.Menu(self.root)
        self.dropdownHats_var = tk.StringVar() # <- make function that updates this accordingly 
        self.dropdownHats = tk.OptionMenu(self.right_panel, self.dropdownHats_var, "TopHat", "BlackHat", "Render Both (cpu intensive)")

        self.dropdownBlur = tk.Menu(self.root)
        self.dropdownBlur_var = tk.StringVar() # <- make function that updates this accordingly 
        self.dropdownBlur = tk.OptionMenu(self.right_panel, self.dropdownBlur_var, "Blur", "BilateralFilter", "MedianBlur", "GaussianBlur", "Render All (cpu intensive)")


        # self.dropdown.add_checkbutton(label="Blur", variable=self.onevar, onvalue=True)
        # self.dropdown.add_checkbutton(label="Erosion", variable=self.twovar, onvalue=True)
        # self.dropdown.add_checkbutton(label="Dilation", variable=self.threevar, onvalue=True)
        # self.dropdown.add_checkbutton(label="Closing", variable=self.fourvar, onvalue=True)
        # self.dropdown.add_checkbutton(label="Opening", variable=self.fivevar, onvalue=True)
        # self.dropdown.add_checkbutton(label="MorphologicalGradient", variable=self.sixvar, onvalue=True)
        # self.dropdown.add_checkbutton(label="TopHat", variable=self.sevenvar, onvalue=True)
        # self.dropdown.add_checkbutton(label="BlackHat", variable=self.eightvar, onvalue=True)

        # self.one = tk.Checkbutton(self.right_panel, text="Blur", variable=self.onevar, onvalue=True)
        # self.two = tk.Checkbutton(self.right_panel, text="Erosion", variable=self.twovar, onvalue=True)
        # self.three = tk.Checkbutton(self.right_panel, text="Dilation", variable=self.threevar, onvalue=True)
        # self.four = tk.Checkbutton(self.right_panel, text="Closing", variable=self.fourvar, onvalue=True)
        # self.five = tk.Checkbutton(self.right_panel, text="Opening", variable=self.fivevar, onvalue=True)
        # self.six = tk.Checkbutton(self.right_panel, text="MorphologicalGradient", variable=self.sixvar, onvalue=True)
        # self.seven = tk.Checkbutton(self.right_panel, text="TopHat", variable=self.sevenvar, onvalue=True)
        # self.eight = tk.Checkbutton(self.right_panel, text="BlackHat", variable=self.eightvar, onvalue=True)
        self.dropdown.grid(row=7, column=1, pady=5)
    

    def store_color(self):
        self.value_ticker += 1
        if self.value_ticker % 2 == 0:
            self.lower_color = self.color_values
            self.lowercolor_label.config(text=f"Lower Color: {self.lower_color}")
        else:
            self.upper_color = self.color_values
            self.uppercolor_label.config(text=f"Upper Color: {self.upper_color}")
        
        


    def insert_color(self):
        color = self.color_id
        
        self.rgb_label.config(text=f"selected color: {self.color_id}")
        self.color_canvas.config(bg=color)

    def updateblock(self):
        r = self.scale1.get()
        g = self.scale2.get()
        b = self.scale3.get()

        color = f'#{r:02x}{g:02x}{b:02x}'
        self.color_id = color
        self.color_values = [r, g, b]
        print(f"selected color: {self.color_id}, second value {self.color_values}")
        self.rgb_label.config(text=f"selected color: {self.color_id}")
        self.color_canvas.config(bg=color)

    def grab_color(self):
        img = Image.new("RGB", (375, 75))
        r, g, b = self.scale1.get(), self.scale2.get(), self.scale3.get()
        for x in range(375):
            for y in range(75):
                img.putpixel((x, y), (int(r), int(g), int(b)))

        return img

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

    
    def get_color(self, event):
        x, y = event.x, event.y
        if 0 <= x < self.width and 0 <= y < self.height:
            rgb = self.img_data.getpixel((x, y))
            hex_color = '#%02x%02x%02x' % rgb
            hex_color = self.color_id
            print(f"selected color: {hex_color}")
            self.label.config(text=f"selected color: {hex_color}")
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':    
    picker = colorwheel()
    picker.run()


