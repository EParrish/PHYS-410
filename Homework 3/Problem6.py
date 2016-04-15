from __future__ import division
# galaxy_pixel_values = []
# galaxy_center = []


# with open("galaxy.csv", "r") as csvfile:
# 	thisreader = csv.reader(csvfile, delimiter=',')

# 	for row in thisreader:
# 		x_pos = int(row[0])
# 		y_pos = int(row[1])
# 		z_value = float(row[2])

# 		if z_value == 1072.0:
# 			#print(x_pos, y_pos)
# 			continue

# 		if x_pos > 512:
# 			#print("a")
# 			if x_pos < 525:
# 				#print("b")
# 				if y_pos > 475:
# 					#print("c")
# 					if y_pos < 490:
# 						#print(z_value)
# 						galaxy_center.append(z_value)
# print(y_pos, x_pos)

# wi = 0
# wo = 5
# for i in range(y_pos):
	
# 	inner_edge = (x-519)^2 + (y-480)^2 = 20^2 + wi^2
# 	outer_edge = (x-519+)^2 + (y-480)^2 = 20^2 + wo^2

		# galaxy_pixel_values.append(z_value)
# print(galaxy_center)

# brightest_star_value = max(galaxy_center)
# print(brightest_star_value) 


# x_pos between 525 and 512
# y_pos between 475 and 490
# Center is (519, 480)


import csv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage
from math import sqrt

annular_ring1= [] 
annular_ring2 = []
annular_ring3 = []
annular_ring4 = []
annular_ring5 = []
annular_ring6 = []
annular_ring7 = []
annular_ring8 = []
annular_ring9 = []
annular_ring10 = []
annular_ring11= [] 
annular_ring12 = []
annular_ring13 = []
annular_ring14 = []
annular_ring15 = []
annular_ring16 = []
annular_ring17 = []
annular_ring18 = []
annular_ring19 = []
# annular_ring20 = []


def DeltaR(x_pos, y_pos):
	DR = sqrt((x_pos-519)**2+(y_pos-480)**2)
	return DR

Image_Array = []

with open("galaxy.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')

	last_y_pos = 1
	this_row = []

	for row in thisreader:

		x_pos = int(row[0])
		y_pos = int(row[1])
		z_value = float(row[2])
		# print x_pos, y_pos, z_value


		DR = DeltaR(x_pos, y_pos)

		if DR >= 20 and DR <=25:
			annular_ring1.append(z_value)
			z_value = 999999999

		if DR >= 45 and DR <= 50:
			annular_ring2.append(z_value)
			z_value = 999999999

		if DR >= 70 and DR <= 75:
			annular_ring3.append(z_value)
			z_value = 999999999

		if DR >= 95 and DR <= 100:
			annular_ring4.append(z_value)
			z_value = 999999999

		if DR >= 120 and DR <= 125:
			annular_ring5.append(z_value)
			z_value = 999999999

		if DR >= 145 and DR <= 150:
			annular_ring6.append(z_value)
			z_value = 999999999

		if DR >= 170 and DR <= 175:
			annular_ring7.append(z_value)
			z_value = 999999999

		if DR >= 195 and DR <= 200:
			annular_ring8.append(z_value)
			z_value = 999999999

		if DR >= 220 and DR <= 225:
			annular_ring9.append(z_value)
			z_value = 999999999

		if DR >= 245 and DR <= 250:
			annular_ring10.append(z_value)
			z_value = 999999999

		if DR >= 270 and DR <= 275:
			annular_ring11.append(z_value)
			z_value = 999999999

		if DR >= 295 and DR <= 300:
			annular_ring12.append(z_value)
			z_value = 999999999

		if DR >= 320 and DR <= 325:
			annular_ring13.append(z_value)
			z_value = 999999999

		if DR >= 345 and DR <= 350:
			annular_ring14.append(z_value)
			z_value = 999999999

		if DR >= 370 and DR <= 375:
			annular_ring15.append(z_value)
			z_value = 999999999

		if DR >= 395 and DR <= 400:
			annular_ring16.append(z_value)
			z_value = 999999999

		if DR >= 420 and DR <= 425:
			annular_ring17.append(z_value)
			z_value = 999999999

		if DR >= 445 and DR <= 450:
			annular_ring18.append(z_value)
			z_value = 999999999

		if DR >= 470 and DR <= 475:
			annular_ring19.append(z_value)
			z_value = 999999999

		# if DR >= 495 and DR <= 500:
		# 	annular_ring20.append(z_value)
		# 	z_value = 999999999


		if y_pos == last_y_pos:
			this_row.append(z_value)

		elif y_pos != last_y_pos:
			# if len(this_row) != 0:
			Image_Array.append(np.array(this_row))
			last_y_pos = y_pos
			this_row = [z_value]

		if x_pos == 1124 and y_pos == 1024:
			Image_Array.append(np.array(this_row))

# print annular_ring1
# print annular_ring2

mean1 = sum(annular_ring1) / len(annular_ring1)
mean2 = sum(annular_ring2) / len(annular_ring2)
mean3 = sum(annular_ring3) / len(annular_ring3)
mean4 = sum(annular_ring4) / len(annular_ring4)
mean5 = sum(annular_ring5) / len(annular_ring5)
mean6 = sum(annular_ring6) / len(annular_ring6)
mean7 = sum(annular_ring7) / len(annular_ring7)
mean8 = sum(annular_ring8) / len(annular_ring8)
mean9 = sum(annular_ring9) / len(annular_ring9)
mean10 = sum(annular_ring10) / len(annular_ring10)
mean11 = sum(annular_ring11) / len(annular_ring11)
mean12 = sum(annular_ring12) / len(annular_ring12)
mean13 = sum(annular_ring13) / len(annular_ring13)
mean14 = sum(annular_ring14) / len(annular_ring14)
mean15 = sum(annular_ring15) / len(annular_ring15)
mean16 = sum(annular_ring16) / len(annular_ring16)
mean17 = sum(annular_ring17) / len(annular_ring17)
mean18 = sum(annular_ring18) / len(annular_ring18)
mean19 = sum(annular_ring19) / len(annular_ring19)
# mean20 = sum(annular_ring20) / len(annular_ring20)


print mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8, mean9, mean10, mean11, mean12, mean13, mean14, mean15, mean16, mean17, mean18, mean19 # , mean20

fig = plt.figure()
Image_Array.reverse()
#print Image_Array[0]
#print Image_Array[1]
#print Image_Array[2]
numpyarray = np.array(Image_Array)

plt.imshow(numpyarray)#, cmap=plt.cm.gray)
plt.show()

# c1 = plt.Circle((519, 480), 20^2, color='r')
# # c2 = plt.Circle((300, 400), 50, color=(1, 0, 0))
# # c3 = plt.Circle((500, 200), 50, color=(0, 1, 0))

# # # Open new figure


# # # In figure, Image as background
# #plt.imshow(img)

# # # Add the circles to figure as subplots
# fig.add_subplot(111).add_artist(c1)
# # fig.add_subplot(111).add_artist(c2)
# # fig.add_subplot(111).add_artist(c3)

# plt.show()

