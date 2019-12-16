### demo file 1

import numpy as np
import cv2
from matplotlib import pyplot as plt # Load an color image in grayscale
img = cv2.imread('test_image/DSC_0345.JPG',0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()