import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('test_real3.jpg',0)

kernel = np.ones((25,25),np.uint8)
dialation = cv.dilate(img,kernel,iterations = 1)

edges = cv.Canny(img,0,200)



plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()