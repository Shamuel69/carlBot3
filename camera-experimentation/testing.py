import cv2
import numpy as np
# import tkinter as tk

# tk._test()
cap = cv2.VideoCapture(0)

lower_range = np.array([100, 150, 0])
upper_range = np.array([140, 255, 255])

kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        raise Exception("Could not read frame. Please make sure there is a camera connected.")
    
    # mask = np.zeros(frame.shape[:2], dtype="uint8")    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    masked = cv2.inRange(hsv, lower_range, upper_range)
    # showing_mask = cv2.imshow(frame, masked)
    result = cv2.bitwise_and(frame, frame, mask=masked)

    # masked = cv2.morphologyEx(masked, cv2.MORPH_OPEN, kernel)
    masked = cv2.morphologyEx(masked, cv2.MORPH_CLOSE, kernel)
    masked = cv2.GaussianBlur(masked, (5, 5), 0)

    eroded = cv2.erode(masked, kernel, iterations=5)
    dilated = cv2.dilate(masked, kernel, iterations=5)
    
    # masked = cv2.erode(masked, kernel, iterations=5)
    # masked = cv2.dilate(masked, kernel, iterations=5)

    dialated_mask = cv2.bitwise_and(frame, frame, mask=masked)

    # result = cv2.bitwise_and(frame, frame, mask=masked)
    # combined = cv2.bitwise_or(frame, frame, mask=gay_mask)

    contours, _ = cv2.findContours(masked, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 7000:
            (x,y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            cv2.circle(frame, center, radius, (0, 255, 255), 2)
            cv2.putText(frame, "Gog", (center[0]-40, center[1]-radius-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    stacked = np.hstack((frame, 
                         result, 
                         dialated_mask))

    # cv2.imshow('masked frame', result)
    cv2.imshow('normal frame',stacked)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cv2.destroyAllWindows()