import requests
import datetime
import time

path='C:/Users/mayij/Desktop/IMGREC/'
url='http://207.251.86.238/cctv1119'

for i in range(0,1000):
    ts=datetime.datetime.now().strftime('%m%d%H%M')
    r=requests.get(url).content
    with open(path+ts+'.jpg', 'wb') as handler:
        handler.write(r)
    time.sleep(60)











import cv2
import matplotlib.pyplot as plt
import cvlib as cv

im=cv2.imread(path+'07200045.jpg')
plt.imshow(im)

bbox,label,conf=cv.detect_common_objects(im)
output_image=cv.object_detection.draw_bbox(im,bbox,label,conf)
plt.imshow(output_image)
print('Number of cars in the image is ' + str(label.count('car')))

