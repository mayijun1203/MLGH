import requests
import datetime
import time

path='C:/Users/mayij/Desktop/DOC/DCP2020/IMGREC/'
url='http://207.251.86.238/cctv1119'

for i in range(0,1000):
    ts=datetime.datetime.now().strftime('%m%d%H%M%S')
    r=requests.get(url).content
    with open(path+ts+'.jpg', 'wb') as handler:
        handler.write(r)
    time.sleep(2)











import cv2
import matplotlib.pyplot as plt
import cvlib as cv

im=cv2.imread(path+'0720095841.jpg')
plt.imshow(im)

bbox,label,conf=cv.detect_common_objects(im)
output_image=cv.object_detection.draw_bbox(im,bbox,label,conf)
plt.imshow(output_image)










import os
import numpy as np
import cv2
import cvlib as cv
import matplotlib.pyplot as plt

def get_vector(a, b):
    dx = float(b[0] - a[0])
    dy = float(b[1] - a[1])
    distance = np.math.sqrt(dx**2 + dy**2)
    if dy > 0:
        angle = np.math.degrees(np.math.atan(-dx/dy))
    elif dy == 0:
        if dx < 0:
            angle = 90.0
        elif dx > 0:
            angle = -90.0
        else:
            angle = 0.0
    else:
        if dx < 0:
            angle = 180 - np.math.degrees(np.math.atan(dx/dy))
        elif dx > 0:
            angle = -180 - np.math.degrees(np.math.atan(dx/dy))
        else:
            angle = 180.0        
    return distance, angle

def is_valid_vector(a):
    distance, angle = a
    threshold_distance = max(50.0, -0.008 * angle**2 + 0.4 * angle + 25.0)
    return (distance <= threshold_distance)



m=[]
for i in os.listdir(path)[0:6]:
    im=cv2.imread(path+i)
    plt.imshow(im)
    bbox,label,conf=cv.detect_common_objects(im)
    output_image=cv.object_detection.draw_bbox(im,bbox,label,conf)
    plt.imshow(output_image)
    m+=[(x[0]+int((x[2]-x[0])/2),x[1]+int((x[3]-x[1])/2)) for x in bbox]


f=m[3]
l=[]
for i in m:
    if is_valid_vector(get_vector(f,i))==True:
        l+=[i]
        f=i


for i in l:
    cv2.circle(output_image,i,5,(255, 0, 0),-1)
plt.imshow(output_image)


cv2.polylines(output_image,[np.int32(l).reshape((-1, 1, 2))],False,(255, 0, 0),1)
plt.imshow(output_image)





