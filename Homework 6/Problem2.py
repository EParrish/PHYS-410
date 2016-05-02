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
	full_data = GrabData("walmart.csv")
	length_of_data = len(full_data)
	print length_of_data
	return

def point_in_poly(x,y,poly):
	"""
	Stolen from here: http://geospatialpython.com/2011/08/point-in-polygon-2-on-line.html
	Checks if a coordinate point is in the given state. 
	inputs:
		x: longitude value
		y latitude value
		poly: points that make the state border
	returns:
		"IN" if point is in state
		"OUT" if point is not in state
	"""

	# check if point is a vertex
	if (x,y) in poly: return "IN"

	# check if point is on a boundary
	for i in range(len(poly)):
	  p1 = None
	  p2 = None
	  if i==0:
	     p1 = poly[0]
	     p2 = poly[1]
	  else:
	     p1 = poly[i-1]
	     p2 = poly[i]
	  if p1[1] == p2[1] and p1[1] == y and x > min(p1[0], p2[0]) and x < max(p1[0], p2[0]):
	     return "IN"
	  
	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
	  p2x,p2y = poly[i % n]
	  if y > min(p1y,p2y):
	     if y <= max(p1y,p2y):
	        if x <= max(p1x,p2x):
	           if p1y != p2y:
	              xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
	           if p1x == p2x or x <= xints:
	              inside = not inside
	  p1x,p1y = p2x,p2y

	if inside: return "IN"
	else: return "OUT"

def PartB():
	full_data = GrabData("walmart.csv")
	all_state_csvs = glob.glob("./State_Polygons/*.csv")

	# Only want continental US
	all_state_csvs.remove("./State_Polygons/Hawaii.csv")
	all_state_csvs.remove("./State_Polygons/Alaska.csv")

	# Using data from http://econym.org.uk/gmap/states.xml for all of the state borders
	State_Boundaries={}		# A dictionary of lists of tuples that contain coordinates that outline each states borders
	State_Sorted_Stores={} 	# A dictionary of lists of tuples that contain coordinates of all the stores in that state
	All_State_Boundaries=[] # A list with all of the points describing state boundaries

	# Prove that the coordinates look right by plotting all state borders
	for state in all_state_csvs:
		
		this_state = state.split('State_Polygons/',1)[1]
		this_state = this_state.split('.',1)[0]

		this_state_data = GrabData(state)
		State_Boundaries[this_state] = this_state_data
		for i in this_state_data:
			All_State_Boundaries.append(i)

		#Create Empty lists for each state to fill later
		State_Sorted_Stores[this_state] = []

	# Check if the point is in any state
	Continental_Stores = [] #	A little unneseccary. But a list of tuples with the coordinates for the store. Not sorted
	for store in full_data:
		for checking_state in State_Boundaries.keys():
			where_is_store = point_in_poly(store[0], store[1], State_Boundaries[checking_state])
			if where_is_store.lower() == "in":
				Continental_Stores.append((store[0], store[1]))
				State_Sorted_Stores[checking_state].append(store) # Only continental states
			elif where_is_store.lower() == "out":
				continue
			else:
				raise Exception("Checking if in State Failed")

	print "Number of Stores in Continental US: %s" %(len(Continental_Stores))
	# print Continental_Stores

	# # Plot state boundaries to see
	# lats, longs = SeparateLatandLong(All_State_Boundaries)
	# plt.figure()
	# plt.scatter(longs,lats)
	# plt.show()
	# # Dakotas look a little odd, but overall it looks okay.

	return State_Sorted_Stores

def PartC():
	State_Sorted_Stores = PartB()
	CA_Stores = State_Sorted_Stores["California"]
	GA_Stores = State_Sorted_Stores["Georgia"]

	CA_Area = 163696.0 #	Stolen from Google [mi^2]
	GA_Area = 59425.0 # 	Stolen from Google [mi^2]

	CA_Population = 38800000.0 #	Stolen from Google [in 2014]
	GA_Population = 10100000.0 #	Stoeln from Google [in 2014]

	CA_Area_Density = round(CA_Area / len(CA_Stores),2)
	GA_Area_Density = round(GA_Area / len(GA_Stores),2)

	CA_Pop_Density = int(round(CA_Population / len(CA_Stores)))
	GA_Pop_Density = int(round(GA_Population / len(GA_Stores)))

	print "CA Population Density: %s [Persons/Store]" %(CA_Pop_Density)
	print "GA Population Density: %s [Persons/Store]" %(GA_Pop_Density)
	print "CA Area Density: %s [mi^2/Store]" %(CA_Area_Density)
	print "GA Area Density: %s [mi^2/Store]" %(GA_Area_Density)

	return

if __name__ == "__main__":
	# PartA()
	PartB()
	# PartC()