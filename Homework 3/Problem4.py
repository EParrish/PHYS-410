import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
import csv
import cv2

# Image_Array = [] # [[0 for x in range(1025)] for x in range(10000)]

# with open("stars.csv", "r") as csvfile:
# 	thisreader = csv.reader(csvfile, delimiter=',')

# 	# cnt = 0
# 	last_y_pos = 1
# 	this_row = []

# 	for row in thisreader:

# 		x_pos = int(row[0])
# 		y_pos = int(row[1])
# 		z_value = float(row[2])


# 		if y_pos == last_y_pos:
# 			this_row.append(z_value)

# 		elif y_pos != last_y_pos:
# 			# if len(this_row) != 0:
# 			Image_Array.append(np.array(this_row))
# 			last_y_pos = y_pos
# 			this_row = [z_value]

# 		if x_pos == 1124 and y_pos == 1024:
# 			Image_Array.append(np.array(this_row))

# # Image_Array.pop(0)
# Image_Array.reverse()
# numpyarray = np.array(Image_Array)
# plt.imshow(numpyarray, cmap=plt.cm.gray)
# # plt.show()

###########################################
############### Denoising #################
###########################################
# Filtered_Image_Array=numpyarray]
plt.figure()
Filtered_Image_Array = ndimage.imread("Problem5_Galaxy_Edit1.png", flatten=True)
med_denoised = ndimage.median_filter(Filtered_Image_Array,3)
# plt.show()

###########################################
############### Sharpening ################
###########################################
# Filtered_Image_Array=numpyarray
Filtered_Image_Array = ndimage.gaussian_filter(med_denoised, 3) # Filtered_Image_Array, 3)
filter_blurred = ndimage.gaussian_filter(Filtered_Image_Array, 1)
alpha=30
sharpened_image = Filtered_Image_Array + alpha * (Filtered_Image_Array - filter_blurred)
plt.imshow(sharpened_image, cmap=plt.cm.gray)
plt.show()

# print img
# num_largest=25
# indeces = (-img).argpartition(num_largest, axis=None)[:num_largest]

# x,y=np.unravel_index(indeces, img.shape)
# for i in xrange(num_largest):
# 	print x[i], y[i]# , img[x,y]
# print "x =", x
# print "y =", y
# print "Largest Values: %s" %(img[x,y])
# print "Compare to %s" %(np.)


############## Sorbel Processing #################
# sx = ndimage.sobel(img, axis=0, mode='constat')
# sy = ndimage.soble(img, axis=1, mode='constant')
# sob = np.hypot(sx,sy)

# ############## Hough Transform ####################
# circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, dp=1.5, minDist=50, minRadius=5, maxRadius=100)
# img_circles = np.copy(img)

# if circles is not None and len(circles) > 0:
# 	circles = circles[0]
# 	for (x,y,r) in circles:
# 		x,y,r=int(x),int(y),int(r)
# 		cv2.circle(img_circles, (x,y), r, (255, 255, 0), 4)
# 	plt.imshow(cv2.cvtColor(img_circles, cv2.COLOR_BGR2RGB))

# print "Number of Circle Detected: %s" %(len(circles[0]))
# plt.show()

######################################
#################### Problem 4########
# img = ndimage.imread('Problem3.png')
# # img = ndimage.gaussian_filter(img, sigma=(5,5,0), order=0)

# plt.imshow(img, interpolation='nearest')
# plt.show()