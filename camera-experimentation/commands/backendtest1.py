import cv2
import numpy as np

cap = cv2.VideoCapture(0)

display_data = {}
checkbox_settings = []

lower_range = None
upper_range = None

def process_data(monitor_settings, colors, HSV=True, **kwargs):
    global lower_range
    global upper_range 

    global checkbox_settings

    lower_range = np.array(colors[0])
    upper_range= np.array(colors[1])
    
    if HSV != True:
        lower_range = cv2.cvtColor(lower_range, cv2.COLOR_RGB2HSV)
        upper_range = cv2.cvtColor(upper_range, cv2.COLOR_RGB2HSV)

    if kwargs["window_amount"] >= 1:
        display_data["window_amount"] = kwargs["window_amount"]

    else:
        display_data["window_amount"] = len(monitor_settings)
    
    checkbox_settings = monitor_settings

##continue to think about possible params then get started on sorting out an easy way to access the listed settings    


while True:
    ret, frame = cap.read()
    if not ret:
        raise Exception("Could not read frame. Please make sure there is a camera connected.")
    
    cv2.imshow('frame', frame)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([100, 150, 0])
    upper_range = np.array([140, 255, 255])
    masked = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('masked', masked)
    result = cv2.bitwise_and(frame, frame, mask=masked)
    cv2.imshow('result', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break