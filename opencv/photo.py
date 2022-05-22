import cv2
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import os


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
# print(len(contours))
# fig=px.imshow(blank)
# fig.show()


# Color space
# BGR to Grayscale
grey=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grey',grey)
# BGR to HSV
hsv=cv2.cvtColor(df,cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV',hsv)
# BGR to LAB
lab=cv2.cvtColor(df,cv2.COLOR_BGR2LAB)
# cv2.imshow('Lab',lab)
# BGT to RGB
rgb=cv2.cvtColor(df,cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB',rgb)
# HSV to BGR
bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
# cv2.imshow('BGR',bgr)

# Color channel
# Split
b,g,r=cv2.split(df)
# cv2.imshow('B',b) # grayscale
# cv2.imshow('G',g)
# cv2.imshow('R',r)
# Merge
merged=cv2.merge([b,g,r])
# cv2.imshow('Merged',merged)
# Actual blue
blank=np.zeros(df.shape[:2],dtype='uint8')
blue=cv2.merge([b,blank,blank])
# cv2.imshow('Blue',blue)


# Blurring & Smoothing
# Averaging
avg=cv2.blur(df,ksize=(7,7))
# cv2.imshow('Averaging',avg)
# Gaussian (more natural)
gaus=cv2.GaussianBlur(df,(7,7),0)
# cv2.imshow('Gaussian',gaus)
# Median
med=cv2.medianBlur(df,7)
# cv2.imshow('Median',med)
# Bilateral
bilat=cv2.bilateralFilter(df,7,35,25)
# cv2.imshow('Bilateral',bilat)


# Bitwise operators
blank=np.zeros((500,500),dtype='uint8')
rect=cv2.rectangle(blank.copy(),(100,100),(400,400),255,-1)
# cv2.imshow('Rectangle',rect)
circ=cv2.circle(blank.copy(),(250,250),200,255,-1)
# cv2.imshow('Circle',circ)
# AND (intersection)
btwand=cv2.bitwise_and(rect,circ)
# cv2.imshow('Bitwise AND',btwand)
# OR (Union)
btwor=cv2.bitwise_or(rect,circ)
# cv2.imshow('Bitwise OR',btwor)
# XOR (Complement)
btwxor=cv2.bitwise_xor(rect,circ)
# cv2.imshow('Bitwise XOR',btwxor)
# NOT (Reverse)
btwnot=cv2.bitwise_not(rect)
# cv2.imshow('Bitwise NOT',btwnot)


# Masking
blank=np.zeros(df.shape[:2],dtype='uint8')
circ=cv2.circle(blank.copy(),(df.shape[1]//2,df.shape[0]//2),100,255,-1)
rect=cv2.rectangle(blank.copy(),(100,100),(df.shape[1]//2,df.shape[0]//2),255,-1)
mask=cv2.bitwise_xor(rect,circ)
# cv2.imshow('Mask',mask)
masked=cv2.bitwise_and(df,df,mask=mask)
# cv2.imshow('Masked',masked)

# Histogram
# Grey
grey=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grey',grey)
blank=np.zeros(df.shape[:2],dtype='uint8')
mask=cv2.circle(blank.copy(),(df.shape[1]//2,df.shape[0]//2),100,255,-1)
masked=cv2.bitwise_and(grey,grey,mask=mask)
# cv2.imshow('Masked',masked)
greyhist=cv2.calcHist([df],channels=[0],mask=mask,histSize=[256],ranges=[0,256])
fig=px.line(greyhist)
# fig.show()

# Color
fig=go.Figure()
colors=('blue','green','red')
for i,col in enumerate(colors):
    hist=cv2.calcHist([df],channels=[i],mask=mask,histSize=[256],ranges=[0,256])
    fig=fig.add_trace(go.Scatter(x=list(range(0,256)),
                                 y=[x[0] for x in hist],
                                 mode='lines',
                                 line_color=col))
# fig.show()


# Thresholding
# Simple
grey=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
threshold,thresh=cv2.threshold(grey,thresh=150,maxval=255,type=cv2.THRESH_BINARY)
# cv2.imshow('Simple Threshold',thresh)

# Inverse
threshold,threshiv=cv2.threshold(grey,thresh=150,maxval=255,type=cv2.THRESH_BINARY_INV)
# cv2.imshow('Simple Threshold Inverse',threshiv)

# Adaptive
adaptthresh=cv2.adaptiveThreshold(grey,maxValue=255,adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,thresholdType=cv2.THRESH_BINARY,blockSize=11,C=3)
# cv2.imshow('Adaptive Threshold Mean',adaptthresh)

# Adaptive Inverse
adaptthreshinv=cv2.adaptiveThreshold(grey,maxValue=255,adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,thresholdType=cv2.THRESH_BINARY_INV,blockSize=11,C=3)
# cv2.imshow('Adaptive Threshold Gaussian Inverse',adaptthreshinv)


# Edge Detection
# Laplacian
grey=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
lap=cv2.Laplacian(grey,ddepth=cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
# cv2.imshow('Laplacian',lap)

# Sobel
sobelx=cv2.Sobel(grey,ddepth=cv2.CV_64F,dx=1,dy=0)
sobely=cv2.Sobel(grey,ddepth=cv2.CV_64F,dx=0,dy=1)
combinesobel=cv2.bitwise_or(sobelx,sobely)
# cv2.imshow('Sobel X',sobelx)
# cv2.imshow('Sobel Y',sobely)
# cv2.imshow('Combined Sobel',combinesobel)

# Canny
canny=cv2.Canny(df,threshold1=150,threshold2=175)
# cv2.imshow('Canny',canny)


# Face Detection
# Haar Cascade (Not advanced enough)
grey=cv2.cvtColor(df,cv2.COLOR_BGR2GRAY)
haar=cv2.CascadeClassifier('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/haarcascade_frontalface_default.xml')
faces=haar.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)
# print(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(df,(x,y),(x+w,y+h),(0,255,0),thickness=2)
resized=cv2.resize(df,(500,500),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Face',resized)


# Face Recognition
# Local Binary Patterns Histogram (Not advanced enough)
# Train
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/'
people=['BP','CH']
haar=cv2.CascadeClassifier('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/haarcascade_frontalface_default.xml')
features=[]
labels=[]
def createtrain():
    for person in people:
        label=people.index(person)
        for img in os.listdir(path+person):
            imgarray=cv2.imread(path+person+'/'+img)
            grey=cv2.cvtColor(imgarray,cv2.COLOR_BGR2GRAY)
            faces=haar.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces:
                facesroi=grey[y:y+h,x:x+w]
                features.append(facesroi)
                labels.append(label)
createtrain()
print(len(features))
print(len(labels))
features=np.array(features,dtype='object')
labels=np.array(labels)
facerecog=cv2.face.LBPHFaceRecognizer_create()
facerecog.train(features,labels)
facerecog.save('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/facetrained.yml')
np.save('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/features.npy',features)
np.save('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/labels.npy',labels)
# Read
features=np.load('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/features.npy',allow_pickle=True)
labels=np.load('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/labels.npy')
facerecog=cv2.face.LBPHFaceRecognizer_create()
facerecog.read('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/facetrained.yml')
img=cv2.imread('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/facerecog.jpg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Person',grey)
faces=haar.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h) in faces:
    facesroi=grey[y:y+h,x:x+w]
    label,conf=facerecog.predict(facesroi)
    cv2.putText(img,text=str(people[label])+' '+str(int(conf)),org=(200,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=10,color=(0,255,0))
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
resized=cv2.resize(img,(500,int(img.shape[0]/img.shape[1]*500)),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Recgonized',resized)








cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()