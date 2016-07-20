

import numpy as np
from scipy import misc
import grayscale as gs
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def threshold(image, threshold):
    assert len(image.shape) == 2, "Must be grayscale image"
    thresh = np.zeros(image.shape)
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):    
            if image[rownum][colnum] > threshold:
                thresh[rownum][colnum] = 0 
            else:
                thresh[rownum][colnum] = 255
    return thresh


def otsu(image):
    assert len(image.shape) == 2, "Must be grayscale image"
    th = _getOtsuThreshold(image)
    return threshold(image, th)
    
    
def _getOtsuThreshold(image):
    import measure as m
    s = 0;
    histogram = m.getHistGray(image)
    for i in range(len(histogram)):
        s += i * histogram[i]
    sumB = 0
    wB = 0
    wF = 0
    mB = None
    mF = None
    m = 0.0
    between = 0.0
    threshold1 = 0.0
    threshold2 = 0.0
    total = len(image.ravel())
    for i in range(len(histogram)):
        wB += histogram[i]
        if wB == 0:
            continue;
        wF = total - wB
        if (wF == 0):
            break
        sumB += i * histogram[i]
        mB = sumB / wB
        mF = (s - sumB) / wF
        between = wB * wF * ((mB - mF) ** 2)
        if between >= m :
            threshold1 = i
            if between > m :
                threshold2 = i
            m = between
    return ( threshold1 + threshold2 ) / 2.0;
    
if __name__ == "__main__":
    
    image = misc.imread('retina.jpg')
    grey = gs.convertToGreyScale(image)
    thresh = otsu(grey)
    plt.imshow(thresh, cmap = cm.Greys_r)
    plt.show()
    
    


