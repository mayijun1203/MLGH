import cv2
import numpy as np
import plotly.io as pio
import plotly.express as px


pio.renderers.default = "browser"


# Read and show image
df=cv2.imread('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/test.jpg')
# cv2.imshow('original',df)


# Resize the image, frame and live video
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow('rescale',rescale(df,0.1))


# Create blank image
blank=np.zeros((500,500,3),dtype='uint8')
# cv2.imshow('Blank',blank)

# Add green square to blank image
blank[200:300,300:400]=0,255,0
# cv2.imshow('Square',blank)

# Add rectangle
# cv2.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=3) # width 3 px
# cv2.rectangle(blank,(0,0),(250,250),(0,255,0),cv2.FILLED) # fill rectangle
cv2.rectangle(blank,(0,0),(250,250),(0,255,0),-1) # fill rectangle
# cv2.imshow('Rectangle',blank)

# Add circle
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
# cv2.imshow('Circle',blank)

# Add line
cv2.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,255),thickness=3)
# cv2.imshow('Line',blank)

# Add text
cv2.putText(blank,'Hello World',(225,225),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,0),2)
# cv2.imshow('Text',blank)

# Convert to grayscale
gray=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)

# Blur
blur=cv2.GaussianBlur(df,ksize=(7,7),sigmaX=cv2.BORDER_DEFAULT) # Kernel size best be odd
# cv2.imshow('Blur',blur)

# Edge Cascade
canny=cv2.Canny(blur,threshold1=125,threshold2=175)
# cv2.imshow('Canny',canny)

# Dilation
dilated=cv2.dilate(canny,kernel=(7,7),iterations=3)
# cv2.imshow('Dilation',dilated)

# Eroding
eroded=cv2.erode(dilated,kernel=(7,7),iterations=3)
# cv2.imshow('Eroding',eroded)

# Resize
resized=cv2.resize(df,(1500,1500),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('INTER_CUBIC',resized)
resized=cv2.resize(df,(1500,1500),interpolation=cv2.INTER_LINEAR)
# cv2.imshow('INTER_LINEAR',resized)
resized=cv2.resize(df,(1500,1500),interpolation=cv2.INTER_AREA)
# cv2.imshow('INTER_AREA',resized)

# Crop
cropped=df[50:200,200:400]
# cv2.imshow('Crop',cropped)

# Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv2.warpAffine(img,transMat,dim)
# x<0: left; x>0:right; y<0:up; y>0:down
trans=translate(df,-100,100)
# cv2.imshow('Translated',trans)

# Rotation
def rotate(img,angle,roPoint=None):
    (height,width)=img.shape[:2]
    if roPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1)
    dim=(width,height)
    return cv2.warpAffine(img,rotMat,dim)
rot=rotate(df,30)
# cv2.imshow('Rotated',rot)
# Limited alternative
rot=cv2.rotate(df,cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow('Rotated',rot)

# Flipping
flip=cv2.flip(df,-1)
# 0:verticle; 1:horizontal; -1:both
# cv2.imshow('Flipped',flip)



# Contour Detection
blank=np.zeros(df.shape,dtype='uint8')
gray=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
# blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
# canny=cv2.Canny(blur,125,175)
ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY) # Binarizing the image
contours,hierarchies=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(blank,contours,-1,(0,255,0),1)
# cv2.imshow('Contours',blank)
print(len(contours))
fig=px.imshow(blank)
fig.show()







cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()