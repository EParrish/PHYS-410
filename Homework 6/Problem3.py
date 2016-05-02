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

def PartA():
	Full_Data = GrabData("walmart.csv")
	Slimmed_Data=[]

	for store in Full_Data:
		if store[0] >= 38.9 and store[0] <= 41.8:
			if store[1] >= -86.4 and store[1] <= -81.9:
				Slimmed_Data.append(store)
	
	lats, longs = SeparateLatandLong(Full_Data)# SeparateLatandLong(Slimmed_Data)

	plt.figure()
	plt.scatter(longs, lats)
	plt.show()

if __name__ == "__main__":
	PartA()