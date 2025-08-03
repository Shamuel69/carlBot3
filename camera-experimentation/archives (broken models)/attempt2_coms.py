import tkinter as tk
from PIL import Image, ImageTk
import colorsys
import cv2
import numpy as np
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
        self.window_settings = False

        self.camera_settings = [] 
        self.camera_settings_list = ['GaussianBlur', 'MedianBlur', 'MorphologicalGradient',
                                    'Closing', 'Opening', 'Erosion', 'Dilation',
                                    'BilateralFilter', 'tophat', 'blackhat']
        
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

        self.root.bind("<Button-1>", self.get_settings)

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

        self.amountwindows = tk.Menu(self.root)
        self.amountwindows_var = tk.IntVar() 
        self.dropdownwindows = tk.OptionMenu(self.right_panel,  self.amountwindows_var, "0", "1", "2", "3", "4", "5", command=lambda x: self.toggle_window(self.window_settings))
        
        self.hsv = tk.BooleanVar()
        self.hsv_button = tk.Checkbutton(self.right_panel, text="HSV", variable=self.hsv, onvalue=True)
        self.hsv_button.grid(row=7, column=0, pady=5)


        self.hsv_label = tk.Label(self.right_panel, text="HSV: ", font=("Arial", 10), width=20, background="#3a2865", fg="white")
        self.hsv_label.grid(row=6, column=0, pady=5)

        self.dropdownwindows.grid(row=7, column=1, pady=2)
    
    def window_helper(self, iteration):
        stored_setting = {}
        for iter, setting in enumerate(self.camera_settings_list):
                    if iter == 0:
                        self.listed_settings = tk.Label(self.right_panel, text=f"window{iteration+1}", font=("Arial", 8), width=10, background="#3a2865", fg="white")
                        self.listed_settings.grid(row=11+iteration, column=0, pady=2)
                    var = tk.BooleanVar()
                    checkbox = tk.Checkbutton(self.right_panel, variable=var, onvalue=True)
                    checkbox.grid(row=11+iteration, column=iter+1, pady=2)
                    stored_setting[setting] = var

        return stored_setting
    
    def get_settings(self, event):
        "debugging tool, **NOT FOR USE**"
        for iter, setting in enumerate(self.camera_settings):
            camera = []
            for key, var in setting.items():
                camera.append((key, var.get()))
            print(f"camera {iter+1}",camera, "\n")
        print("=====================================================================")
        

    def toggle_window(self, window_settings_visible):
        window_settings_visible = not window_settings_visible

        if window_settings_visible >= 1:
            for iter, setting in enumerate(self.camera_settings_list):
                    self.listed_settings = tk.Label(self.right_panel, text=setting, font=("Arial", 8), width=10, background="#3a2865", fg="white")
                    self.listed_settings.grid(row=10, column=iter+1, pady=2)

            for iteration in range(self.amountwindows_var.get()):
                self.window_helper(iteration)
                self.camera_settings.append(self.window_helper(iteration))
        else:
            if len(self.camera_settings) > 0:
                for setting in self.camera_settings:
                    for key in setting.keys():
                        setting[key].destroy()
            else:
                pass

    def store_color(self):
        self.value_ticker += 1
        colors = self.color_values
        added_text = ""

        if self.hsv.get() == True:
            hsvcnvt = np.uint8([[colors]])
            colors = cv2.cvtColor(hsvcnvt, cv2.COLOR_RGB2HSV)
            colors = [int(colors[0][0][0]), int(colors[0][0][1]), int(colors[0][0][2])]
            added_text = " (HSV)"
        if self.value_ticker % 2 == 0:
            self.lower_color = colors
            self.lowercolor_label.config(text=f"Lower Color{added_text}: {colors}")
        else:
            self.higher_color = colors
            self.uppercolor_label.config(text=f"Upper Color{added_text}: {colors}")
        
    def insert_color(self):
        color = self.color_id
        if self.hsv.get() == True:
            color = colorsys.rgb_to_hsv(self.color_id)

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


