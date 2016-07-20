import time
import cv2
import scipy.ndimage
import numpy as np
from matplotlib import *
import pylab as plt
import matplotlib.image


def cumsum(h, m, n):
    # finds cumulative sum of a numpy array, list
    return [sum(h[:i+1]) for i in range(m,n)]

img = cv2.imread('yay01.jpg',0)
equ = cv2.equalizeHist(img)
#res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('response.png',equ)

x = np.array([[0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123]])


res2 = scipy.ndimage.filters.median_filter(equ, [12,12], footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
#res2 = scipy.ndimage.filters.convolve(equ, x, output=None, mode='reflect', cval=0.0, origin=0)

cv2.imwrite('response2.png',res2)

res3 = res2 - equ
cv2.imwrite('response3.png',res3)

#----------------Computation of ISODATA starts from here-----------------

# load image to numpy arrayb
# matplotlib 1.3.1 only supports png images
# use scipy or PIL for other formats
img = np.uint8(matplotlib.image.imread('response3.png')*255.0)
#cv2.imwrite('response5.png',img)

hist, bins = np.histogram(img, 256, [0,256])
m = 0
mu=cumsum(hist, 0, len(hist)-1)

f1 = int(sum(np.multiply(bins[0:len(bins)-1], hist)))
f2 = int(mu[len(mu)-1])

T = []
a=f1/f2


T.append(a)
mu2 = cumsum(hist, 0, T[0]-1)
MBT=sum(np.multiply(bins[0:T[0]-1],hist[0:T[0]-1]))
l1 = mu2[len(mu2)-1]
MBT = MBT/l1
mu3=cumsum(hist, T[0]-1, len(hist)-1)

MAT = sum(np.multiply(bins[T[0]:len(bins)-1] ,hist[T[0]-1:len(hist)-1]))
l2 = mu3[len(mu3)-1]
MAT = MAT/l2

m = m+1
b = ((MAT+MBT)/2)

T.append(b)

while abs(T[m]-T[m-1])>=1:
    mu2 = cumsum(hist, 0, T[0]-1)
    MBT=sum(np.multiply(bins[0:T[0]-1],hist[0:T[0]-1]))
    l1 = mu2[len(mu2)-1]
    MBT = MBT/l1
    mu3=cumsum(hist, T[0]-1, len(hist)-1)

    MAT = sum(np.multiply(bins[T[0]:len(bins)-1] ,hist[T[0]-1:len(hist)-1]))
    l2 = mu3[len(mu3)-1]
    MAT = MAT/l2

    m = m+1
    b = ((MAT+MBT)/2)

    T.append(b)
    Threshold=T[m]


level = (Threshold-1) / (bins[len(bins)-1] - 1)

#------------------------------End of ISODATA---------------------------------

thresh = level - 0.008
maxValue = 255


th, dst = cv2.threshold(res3, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imwrite('response6.png',dst)
contours, hierarchy = cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imwrite('response7.png',dst)
res4 = cv2.drawContours(dst,contours,-1,(0,0,0),100)
cv2.imwrite('response8.png',dst)
time.sleep(2)