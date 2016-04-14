import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage

######################################
#################### Problem 4########
img = ndimage.imread('Problem3.png')
img = ndimage.gaussian_filter(img, sigma=(5,5,0), order=0)

plt.imshow(img, interpolation='nearest')
plt.show()