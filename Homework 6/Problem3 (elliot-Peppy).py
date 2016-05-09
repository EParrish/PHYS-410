import csv
import matplotlib.pyplot as plt
import numpy as np
import glob
import math

def GrabData(file_path):
	Coordinates=[]

	with open(file_path, "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:

			latitude = float(row[0])
			longitude = float(row[1])

			Coordinates.append((latitude,longitude))

	return Coordinates

def SeparateLatandLong(list_of_coords):
	lats = []
	longs = []
	for i in list_of_coords:
		lats.append(i[0])
		longs.append(i[1])
	return lats, longs

def BuildWindows(window_size):

	# for i in xrange(1,rsize):
	# 	if i < window_size:
	# 		continue
	# 	if i > rsize - window_size:
	# 		continue
	# 	for j in xrange(1,csize):
	# 		if j < window_size:
	# 			continue
	# 		if j > csize - window_size:
	# 			continue
	# 		this_window = []
	# 		k = i - int(window_size/2)
	# 		x_neighbors = []
	# 		###### Grab x neighbors 
	# 		while k < i + int(window_size/2):
	# 			x_neighbors.append(k)
	# 			y_neighbors = []

	# 			l = j - int(window_size/2)
	# 			while l < j+ int(window_size/2):
	# 				y_neighbors.append(l)
	# 				l += 1

	# 				this_window.append([k,l])
				
	# 			windows["%s_%s" %(i,j)] = this_window
	# 			k += 1

	pass

def FindDistanceSquared(p0, p1):
	"""
	Calculate the great circle distance between two points 
	on the earth (specified in decimal degrees)
	"""
	lon1 = p0[0]; lat1 = p0[1];
	lon2 = p1[0]; lat2 = p1[1];
	# convert decimal degrees to radians 
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	# haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	km = 6367 * c
	return km

def ReturnBox(box_size, p0):
	"""
	Returns the points offset from p0 that make a box of size box_size
	!!!!!!!!!!!!!! box_size is in km !!!!!!!!!!!!!!
	Taken from here: http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
	"""
	R=6378137 # Earth's Radius in m
	dN = float(box_size * 1000); dE = float(box_size * 1000); # Set offsets in m
	lon = p0[0]; lat = p0[1]; # Grab coordinates of center point

	# Convert offsets to radians
	dLat = dN/R
	dLon = dE/(R*math.cos(math.pi * lat / 180))

	topLat = lat + dLat * 180/math.pi
	bottomLat = lat - dLat * 180/math.pi

	leftLon = lon - dLon * 180/math.pi
	rightLon = lon + dLon * 180/math.pi

	return topLat, bottomLat, leftLon, rightLon

def PartA():
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Slimmed_Data) # SeparateLatandLong(Full_Data) 

	box_size = 16;
	cnts16 = []

	for point in Slimmed_Data:
		topLat, bottomLat, leftLon, rightLon = ReturnBox(box_size, point)
		cnt = 0
		for otherpoints in Slimmed_Data:
			if otherpoints[0] >= leftLon and otherpoints[0] <= rightLon:
				if otherpoints[1] >= bottomLat and otherpoints[1] <= topLat:
					cnt += 1
		cnts16.append(cnt)
		print cnt

	# print cnts16
	# print len(lats)
	plt.figure()
	plt.scatter(longs, lats)
	plt.show()

if __name__ == "__main__":
	PartA()
	# ReturnBox(5, (0.0, 51.0))