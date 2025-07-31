import tkinter as tk
from PIL import Image, ImageTk
import colorsys
import cv2
import numpy as np

class colorwheel:
    def __init__(self, width=500, height=300):
        self.width = width
        self.height = height

        self.root = tk.Tk()

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