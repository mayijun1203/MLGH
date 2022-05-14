import cv2

df=cv2.imread('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/opencv/test.jpg')
cv2.imshow('frame',df)

cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()