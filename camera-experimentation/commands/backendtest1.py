import cv2
import numpy as np

cap = cv2.VideoCapture(0)

display_data = {}
checkbox_settings = []

lower_range = None
upper_range = None

def process_data(monitor_settings, colors, HSV=True):
    global lower_range
    global upper_range 

    global checkbox_settings

    try:
        lower_range = np.uint8([[colors[0]]])
        upper_range= np.uint8([[colors[1]]])
    except TypeError as e:
        print(f"Error: {e} - please ensure that the correct data type was provided for colors.")

    if HSV != True:
        lower_range = cv2.cvtColor(lower_range, cv2.COLOR_RGB2HSV)
        upper_range = cv2.cvtColor(upper_range, cv2.COLOR_RGB2HSV)

    
    display_data["window_amount"] = len(monitor_settings)
    
    checkbox_settings = monitor_settings

    startmachine()

def add_filters(settings):
    for key, var in settings.items():
        print(key, var)

def startmachine():
    print("machine started: stage 0")

    while True:
        ret, frame = cap.read()
        if not ret:
            raise Exception("Could not read frame. Please make sure there is a camera connected.")

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        held_mask = []

        for setting in checkbox_settings:
            for key, var in setting.items():
                if var == True:
                    add_filters(setting)
            masked = cv2.inRange(hsv, lower_range, upper_range)
            result = cv2.bitwise_and(frame, frame, mask=masked)
            held_mask.append(result)
        
        stacked = np.hstack((frame, *held_mask))
        cv2.imshow('result', stacked)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def get_data(number:int, decrypted=False):
    temp_dict = {}
    if decrypted:
        for key in checkbox_settings[number]:
            temp_dict[key] = key.get()
        return temp_dict
    return checkbox_settings[number]


##continue to think about possible params then get started on sorting out an easy way to access the listed settings    


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         raise Exception("Could not read frame. Please make sure there is a camera connected.")
    
#     cv2.imshow('frame', frame)
    
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lower_range = np.array([100, 150, 0])
#     upper_range = np.array([140, 255, 255])
#     masked = cv2.inRange(hsv, lower_range, upper_range)
#     cv2.imshow('masked', masked)
#     result = cv2.bitwise_and(frame, frame, mask=masked)
#     cv2.imshow('result', result)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break