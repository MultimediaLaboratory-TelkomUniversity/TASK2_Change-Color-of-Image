"""
@author : Ida Bagus Dwi Satria Kusuma - @dskusuma
Notes   :
There are two kind of solutions. The first is solution using the Open-CV's
library. The second is without the library.
"""

import numpy as np 
import cv2

# Read color image 
img = cv2.imread('gambar1.jpg', cv2.COLOR_BGR2GRAY)

# Filter
filt = np.array([[1, 1, 1], 
                 [1, 1, 1], 
                 [1, 1, 1]])

# Get the image's height and width
height, width = img.shape

# Calculate Convolution
