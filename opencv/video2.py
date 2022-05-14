import cv2
import cvlib as cv
import matplotlib.pyplot as plt

# Read video
cap=cv2.VideoCapture('C:/Users/mayij/Desktop/Loc 6 - 1pm-2pm.avi')

while True:
    # Get return value and frame
    ret,frame=cap.read()
    
    bbox,label,conf=cv.detect_common_objects(frame)
    output_image=cv.object_detection.draw_bbox(frame,bbox,label,conf)
    plt.imshow(output_image)
    
    for i in range(0,len(label)):
        if label[i]=='car':
            x,y,w,h=bbox[i]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    # Show frame
    cv2.imshow('Frame',frame)
    # cv2.imshow('Mask',mask)
    
    # Exit when press ESC
    key=cv2.waitKey(30)
    if key==27:
        break

# Realease video
cap.release()

# Destroy all windows
cv2.destroyAllWindows()