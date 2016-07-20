

import numpy as np

def getHistGray(image):
    assert len(image.shape) == 2, "Must be grayscale image"
    hist = np.zeros(255)
    for row in image:
        for col in row:
            hist[int(col)] += 1
    return hist
    
if __name__ == "__main__":
    import grayscale as gs
    from scipy import misc
    image = misc.imread('retina.jpg')
    grey = gs.convertToGreyScale(image)
    hist = getHistGray(grey)
    print hist