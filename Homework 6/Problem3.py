import csv
import matplotlib.pyplot as plt
import numpy as np
import glob

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

def FindDistanceSquared(p0, p1):
	# """
	# Returns the distances squared (DR)^2
	# Google says math.sqrt call is slow

	# p0: tuple of first points coordinates
	# p1: tuple of second points coordinates
	# """
	# return (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2
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

def PartA():
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:	
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Full_Data) #SeparateLatandLong(Slimmed_Data)

	plt.figure()
	plt.scatter(longs, lats)
	plt.show()

if __name__ == "__main__":
	PartA()