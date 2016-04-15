import csv
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import cm
import scipy.ndimage as ndimage

Image_Array = [] # [[0 for x in range(1025)] for x in range(10000)]

with open("galaxy.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')

	# cnt = 0
	last_y_pos = 1
	this_row = []

	for row in thisreader:

		x_pos = int(row[0])
		y_pos = int(row[1])
		z_value = float(row[2])
		print z_value

		if y_pos == last_y_pos:
			this_row.append(z_value)

		elif y_pos != last_y_pos:
			# if len(this_row) != 0:
			Image_Array.append(np.array(this_row))
			last_y_pos = y_pos
			this_row = [z_value]

		if x_pos == 1124 and y_pos == 1024:
			Image_Array.append(np.array(this_row))


		# print x_pos+1, y_pos+1, z_value

		# Image_Array[x_pos+1][y_pos+1] = z_value
		# print Image_Array[x_pos+1][y_pos+1], z_value

# gStyle.SetOptStat(0)
# canvas = TCanvas("canvas")

# histo = TH2D("histo", "GrayScale", 1024, 0, 1024, 1024, 0, 1030)

# for i in range(len(Image_Array)):
# 	for j in range(len(Image_Array[i])):
# 		histo.Fill(i,j,Image_Array[i][j])

# histo.Draw("COLZ")
# raw_input("Press Enter to Quit")


# Image_Array.pop(0)
Image_Array.reverse()
numpyarray = np.array(Image_Array)
# im = Image.fromarray(numpyarray)
# im.putpalette(getpalette(cm.jet))

plt.imshow(numpyarray, cmap=plt.cm.gray)
plt.show()
# img = Image.fromarray(Image_Array)
# toimage(Image_Array).show()
