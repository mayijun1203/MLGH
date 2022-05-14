import numpy as np
import matplotlib.pyplot as plt

import skimage.restoration
import skimage.io


df=skimage.io.imread('C:/Users/mayij/Desktop/test.jpg')
skimage.io.imshow(df)


def getmask(image):
    mask = np.zeros(image.shape[:-1])
    mask[600:800,300:500] = 1
    return mask

mask=getmask(df)
skimage.io.imshow(mask)

# mask=skimage.io.imread('C:/Users/mayij/Desktop/mask.jpg')
# skimage.io.imshow(mask)


image_result=skimage.restoration.inpaint.inpaint_biharmonic(df,mask,channel_axis=-1)
skimage.io.imshow(image_result)
skimage.io.imsave('C:/Users/mayij/Desktop/result.jpg',image_result)
