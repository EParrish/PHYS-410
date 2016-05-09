import csv
import matplotlib.pyplot as plt
import numpy as np
import glob
from math import radians, cos, sin, asin, sqrt, pi
from ROOT import *

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
	dLon = dE/(R*cos(pi * lat / 180))

	topLat = lat + dLat * 180/pi
	bottomLat = lat - dLat * 180/pi

	leftLon = lon - dLon * 180/pi
	rightLon = lon + dLon * 180/pi

	return topLat, bottomLat, leftLon, rightLon

def PartA():
	"""
	Here we will simply start with a rectangular area which goes in latitude from 38.9 (south) to 41.8 (North) and -86.4 (West) to (-81.9) East. 
	Produce a file for all events within those boundaries. Submit a location plot of those events 
	"""
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Slimmed_Data) # SeparateLatandLong(Full_Data) 

	# box_size = 1;
	# cnts16 = []

	# for point in Slimmed_Data:
	# 	topLat, bottomLat, leftLon, rightLon = ReturnBox(box_size, point)
	# 	cnt = 0
	# 	for otherpoints in Slimmed_Data:
	# 		if otherpoints[0] >= leftLon and otherpoints[0] <= rightLon:
	# 			if otherpoints[1] >= bottomLat and otherpoints[1] <= topLat:
	# 				cnt += 1
	# 	cnts16.append(cnt)
	# 	# print cnt

	print cnts16
	print len(lats)
	plt.figure()
	plt.scatter(longs, lats)
	plt.show()

def CountOccurances(box_size, Slimmed_Data):
	cnts = []

	for point in Slimmed_Data:
		topLat, bottomLat, leftLon, rightLon = ReturnBox(box_size, point)
		cnt = 0
		for otherpoints in Slimmed_Data:
			if otherpoints[0] >= leftLon and otherpoints[0] <= rightLon:
				if otherpoints[1] >= bottomLat and otherpoints[1] <= topLat:
					cnt += 1
		cnts.append(cnt)
		# print cn

	return cnts

def PartC():
	"""
	Now measure event density (number of stores per square km) in box sizes of 1,2,4,8 and 16 square km. 
	for each box size, submit the histogram of densities that you measured and comment on any trends that you notice 
	"""
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Slimmed_Data) # SeparateLatandLong(Full_Data) 

	cnts16 = CountOccurances(16, Slimmed_Data)
	cnts8 = CountOccurances(8, Slimmed_Data)
	cnts4 = CountOccurances(4, Slimmed_Data)
	cnts2 = CountOccurances(2, Slimmed_Data)
	cnts1 = CountOccurances(1, Slimmed_Data)
 
	plt.figure()
	plt.hist(cnts16, 30)
	plt.xlabel("Box Density")
	plt.ylabel("Number of Occurances")
	plt.title("Box Size: 16")
	plt.axis([0,30,0,20])
	plt.text(15, 18,'Mean: %s'%(round(float(sum(cnts16)/float(len(cnts16))),2)),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

	plt.figure()
	plt.hist(cnts8, 20)
	plt.xlabel("Box Density")
	plt.ylabel("Number of Occurances")
	plt.title("Box Size: 8")
	plt.axis([0,20,0,30])
	plt.text(10, 28,'Mean: %s'%(round(float(sum(cnts8)/float(len(cnts8))),2)),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

	plt.figure()
	plt.hist(cnts4, 10)
	plt.xlabel("Box Density")
	plt.ylabel("Number of Occurances")
	plt.title("Box Size: 4")
	plt.axis([0,10,0,70])
	plt.text(5, 68,'Mean: %s'%(round(float(sum(cnts4)/float(len(cnts4))),2)),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

	plt.figure()
	plt.hist(cnts2, 7)
	plt.xlabel("Box Density")
	plt.ylabel("Number of Occurances")
	plt.title("Box Size: 2")
	plt.axis([0,7,0,115])
	plt.text(3.5, 100,'Mean: %s'%(round(float(sum(cnts2)/float(len(cnts2))),2)),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

	plt.figure()
	plt.hist(cnts1, 5)
	plt.xlabel("Box Density")
	plt.ylabel("Number of Occurances")
	plt.title("Box Size: 1")
	plt.axis([0,5,0,160])
	plt.text(2.5, 140,'Mean: %s'%(round(float(sum(cnts1)/float(len(cnts1))),2)),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

def PartD():
	"""
	For the 8 km box, submit a heat map representation that shows the amount of over and under density (compared to the background density) that exists on that scale
	"""
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Slimmed_Data) # SeparateLatandLong(Full_Data) 

	cnts8 = CountOccurances(8, Slimmed_Data)
	mean8 = round(float(sum(cnts8)/float(len(cnts8))),2)

	hist = TH2D("hist", ";Longitude;Latitude;Denstiy/<Density>", 290, -87, -81, 100, 38.5, 42)

	for i in xrange(len(lats)):
		hist.Fill(longs[i], lats[i], float(cnts8[i])/mean8)

	gStyle.SetOptStat(0)
	c1 = TCanvas("c1")
	c1.SetRightMargin(0.13)
	hist.Draw("COLZ")

	raw_input("Press Enter to Quit")
	return

def PartE():
	"""
	Repeat the above exercise but use a cricle of radius 25 km 
	"""
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Slimmed_Data) # SeparateLatandLong(Full_Data) 

	cnts = []
	for point in Slimmed_Data:
		cnt = 0
		for otherpoint in Slimmed_Data:
			if FindDistanceSquared(point, otherpoint) <= 25.0:
				cnt += 1
		cnts.append(cnt)

	mean = round(float(sum(cnts)/float(len(cnts))),2)

	plt.figure()
	plt.hist(cnts, 40)
	plt.xlabel("Circle Density")
	plt.ylabel("Number of Occurances")
	plt.title("Circle Radius: 25 km")
	plt.axis([0,40,0,20])
	plt.text(20, 18,'Mean: %s'%(mean),
     horizontalalignment='center',
     verticalalignment='center')
	plt.show()

	hist = TH2D("hist", ";Longitude;Latitude;Denstiy/<Density>", 290, -87, -81, 100, 38.5, 42)

	for i in xrange(len(lats)):
		hist.Fill(longs[i], lats[i], float(cnts[i])/mean)

	gStyle.SetOptStat(0)
	c1 = TCanvas("c1")
	c1.SetRightMargin(0.13)
	hist.Draw("COLZ")

	raw_input("Press Enter to Quit")
	return

if __name__ == "__main__":
	# PartA()
	# PartC()
	PartD()
	PartE()