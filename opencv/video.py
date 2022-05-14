import cv2

# Read video
cap=cv2.VideoCapture('C:/Users/mayij/Desktop/Loc 6 - 1pm-2pm.avi')

# Identify background for stable camera
det=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)


while True:
    # Get return value and frame
    ret,frame=cap.read()
    
    # Get height and width of frame
    height,width,_=frame.shape
    
    # Get region of interest
    roi=frame[:,:]

    # Add mask
    mask=det.apply(roi)
    _,mask=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    
    # Find contour
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # Get rid of small contours
        area=cv2.contourArea(cnt)
        
        # Draw contours and rectangles
        if area >100:
            # cv2.drawContours(roi,[cnt],-1,(0,255,0),2)
            x,y,w,h=cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x+w,y+h),(0,255,0),3)
    
    # Show frame
    cv2.imshow('Roi',roi)
    # cv2.imshow('Mask',mask)
    
    # Exit when press ESC
    key=cv2.waitKey(30)
    if key==27:
        break

# Realease video
cap.release()

# Destroy all windows
cv2.destroyAllWindows()