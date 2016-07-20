

from scipy import misc
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import cv2
import scipy.ndimage
#import numpy as np
#from matplotlib import *



def convertToGreyScale(image, method="weighted"):
    
    def getWeightedAvg(pixel):
        return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]        
        
    grey = np.zeros(image.shape[0:-1])
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
            if method == "average":
                grey[rownum][colnum] = np.average(image[rownum][colnum])
            elif method == "weighted":
                grey[rownum][colnum] = getWeightedAvg(image[rownum][colnum])
        
    return grey

if __name__ == "__main__":
    image = misc.imread('retina.jpg')
    
    grey = convertToGreyScale(image,method="average")
    
    wgrey = convertToGreyScale(image)
    
    
    plt.subplot(2,2,1)
    plt.xticks([]),plt.yticks([])
    plt.title("Original")
    plt.imshow(image)
    
    plt.subplot(2,2,2)
    plt.xticks([]),plt.yticks([])
    plt.title("Average")
    plt.imshow(grey, cmap = cm.Greys_r)
    
    #plt.subplot(2,2,3)
    #plt.xticks([]),plt.yticks([])
    #plt.title("Weighted Average")
    #plt.imshow(grey, cmap = cm.Greys_r)

    
    #plt.show()
    #plt.draw()
    plt.savefig('lalala.jpg')  

    x = np.array([[0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123],
                  [0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123, 0.0123]])



    
    img = cv2.imread('lalala.jpg',0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ)) #stacking images side-by-side
    cv2.imwrite('response.png',res)



    res2 = scipy.ndimage.filters.median_filter(equ, [9,9], footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    cv2.imwrite('response2.png',res2)  

