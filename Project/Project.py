import cv2 as cv
import numpy as np
import math

img = cv.imread('/Users/SamX/Desktop/NumMeth/Project/Full/Full5.png',0)
print(img)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
