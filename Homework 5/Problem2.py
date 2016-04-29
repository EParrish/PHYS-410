import csv
import random
import matplotlib.pyplot as plt
import itertools
import math
import time
from math import radians, cos, sin, asin, sqrt

def GrabData():
	CoordinateDictionary={}

	with open("posit.csv", "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:

			state = row[0]
			city = row[1]
			latitude = float(row[2])
			longitude = float(row[3])

			CoordinateDictionary["%s, %s" %(city, state)] = (latitude, longitude)

	return CoordinateDictionary

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

def FindRandomPath(CoordinateDictionary):
	"""
	Problem 2 Part A and B
	"""
	FiveCityDict = {"Olympia, Washington": CoordinateDictionary["Olympia, Washington"], 
					"Salem, Oregon": CoordinateDictionary["Salem, Oregon"],
					"Boise, Idaho": CoordinateDictionary["Boise, Idaho"],
					"Helana, Montana": CoordinateDictionary["Helana, Montana"],
					"Sacramento, California": CoordinateDictionary["Sacramento, California"]}

	keys = FiveCityDict.keys()
	lat_values=[]
	long_values=[]

	starting_city = random.choice(keys)
	print "Starting City: %s %s" %(starting_city, FiveCityDict[starting_city])
	lat_values.append(FiveCityDict[starting_city][0])
	long_values.append(FiveCityDict[starting_city][1])
	keys.remove(starting_city)

	# Shuffle order so path is random
	random.shuffle(keys)

	for i in keys:
		p0 = FiveCityDict[i]
		lat_values.append(p0[0])
		long_values.append(p0[1])
		print "\t %s %s" %(i, p0)

	keys.insert(0,starting_city)
	fig, ax = plt.subplots()
	plt.plot(lat_values, long_values, '-0')

	for i, txt in enumerate(keys):
		ax.annotate(txt, (lat_values[i], long_values[i]))

	plt.show()

def StartFromBoise(CoordinateDictionary):
	"""
	Problem 2 Part C
	"""
	FiveCityDict = {"Olympia, Washington": CoordinateDictionary["Olympia, Washington"], 
					"Salem, Oregon": CoordinateDictionary["Salem, Oregon"],
					"Boise, Idaho": CoordinateDictionary["Boise, Idaho"],
					"Helana, Montana": CoordinateDictionary["Helana, Montana"],
					"Sacramento, California": CoordinateDictionary["Sacramento, California"]}

	keys = FiveCityDict.keys()
	starting_city = "Boise, Idaho"
	# print "Starting City: %s" %(starting_city)
	keys.remove(starting_city)

	random.shuffle(keys)
	last_city = starting_city
	distances = []

	AllPossibleCombinations = list(itertools.permutations(keys, len(keys)))

	for i in AllPossibleCombinations:
		dist = 0
		for j in i:
			dist += FindDistanceSquared(FiveCityDict[last_city], FiveCityDict[j])
			last_city=j
		distances.append(dist)

	for k in xrange(len(distances)):
		x = list(AllPossibleCombinations[k])
		x.append(str(distances[k]))
		print "," .join(x)
		

	print "Minimum Path: %s" %(AllPossibleCombinations[distances.index(min(distances))],)
	print "Minimum Distance: %s" %(min(distances))

def PartD(CoordinateDictionary):
	"""
	Picks a set number of random cities and finds the minimum path distance.
	WARNING: Very Large Output. (560M when piped to text file, for 11 cities) Nevermind
	"""
	Number_of_Cities = 11

	AllKeys = CoordinateDictionary.keys()
	CityDict = {}
	for i in xrange(Number_of_Cities):
		this_choice = random.choice(AllKeys)
		CityDict[this_choice] = CoordinateDictionary[this_choice]

	keys = CityDict.keys()
	starting_city = random.choice(keys)
	print "Starting City: %s" %(starting_city)
	keys.remove(starting_city)

	random.shuffle(keys)
	last_city = starting_city
	distances = []

	AllPossibleCombinations = list(itertools.permutations(keys, len(keys)))

	for i in AllPossibleCombinations:
		dist = 0
		for j in i:
			dist += FindDistanceSquared(CityDict[last_city], CityDict[j])
			last_city=j
		distances.append(dist)

	# for k in xrange(len(distances)):
	# 	print "\t%s" %(AllPossibleCombinations[k],)
	# 	print "\t %s" %((distances[k]))
	for k in xrange(len(distances)):
		x = list(AllPossibleCombinations[k])
		x.append(str(distances[k]))
		print "," .join(x)

	print "Minimum Path: %s" %(AllPossibleCombinations[distances.index(min(distances))],)
	print "Minimum Distance: %s" %(min(distances))
	
if __name__ == "__main__":
	start_time = time.time()
	data = GrabData()
	# FindRandomPath(data)
	# StartFromBoise(data)
	PartD(data)
	print "Runtime: %s seconds" %(time.time() - start_time) 