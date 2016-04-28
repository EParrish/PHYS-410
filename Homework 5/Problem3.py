import csv
import random
import matplotlib.pyplot as plt
import itertools
import math
import time

"""
If time allows. Convert distances from lat/long to miles using great arcs.
"""
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
	"""
	Returns the distances squared (DR)^2
	Google says math.sqrt call is slow

	p0: tuple of first points coordinates
	p1: tuple of second points coordinates
	"""
	return (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2

def PartA(CoordinateDictionary):
	"""
	Greedy algorithm
	"""
	CityDict = {"Olympia, Washington": CoordinateDictionary["Olympia, Washington"], 
					"Salem, Oregon": CoordinateDictionary["Salem, Oregon"],
					"Little Rock, Arkansas": CoordinateDictionary["Little Rock, Arkansas"],
					"Madison, Wisconsin": CoordinateDictionary["Madison, Wisconsin"],
					"Sacramento, California": CoordinateDictionary["Sacramento, California"],
					"Frankfort, Kentucky": CoordinateDictionary["Frankfort, Kentucky"],
					"Concord, New Hampshire": CoordinateDictionary["Concord, New Hampshire"],
					"Raleigh, North Carolina": CoordinateDictionary["Raleigh, North Carolina"],
					"Tallahassee, Florida": CoordinateDictionary["Tallahassee, Florida"]}

	keys = CityDict.keys()
	starting_city = "Little Rock, Arkansas"
	print "Starting City: %s" %(starting_city)
	keys.remove(starting_city)

	last_city = starting_city
	Final_distances = []
	Final_Path=[]
	Final_lats=[]
	Final_longs=[]

	for k in xrange(len(keys)):
		AllPossibleCombinations = list(itertools.permutations(keys, 1))
		# print AllPossibleCombinations

		distances = []
		for i in AllPossibleCombinations:
			# print i[0]
			distances.append(FindDistanceSquared(CityDict[last_city], CityDict[i[0]]))

		last_city = AllPossibleCombinations[distances.index(min(distances))][0]
		Final_Path.append([last_city, CityDict[last_city]])
		Final_lats.append(CityDict[last_city][0])
		Final_longs.append(CityDict[last_city][1])
		Final_distances.append(min(distances))
		keys.remove(last_city)
		# print last_city
	# print Final_Path
	print "Total Distance: %s" %(math.sqrt(sum(Final_distances)))
	plt.figure()
	plt.plot(Final_lats, Final_longs, '-0')
	plt.show()

def PartB(CoordinateDictionary):
	"""
	2 opt swap
	"""
	CityDict = {"Olympia, Washington": CoordinateDictionary["Olympia, Washington"], 
					"Salem, Oregon": CoordinateDictionary["Salem, Oregon"],
					"Little Rock, Arkansas": CoordinateDictionary["Little Rock, Arkansas"],
					"Madison, Wisconsin": CoordinateDictionary["Madison, Wisconsin"],
					"Sacramento, California": CoordinateDictionary["Sacramento, California"],
					"Frankfort, Kentucky": CoordinateDictionary["Frankfort, Kentucky"],
					"Concord, New Hampshire": CoordinateDictionary["Concord, New Hampshire"],
					"Raleigh, North Carolina": CoordinateDictionary["Raleigh, North Carolina"],
					"Tallahassee, Florida": CoordinateDictionary["Tallahassee, Florida"]}

	keys = CityDict.keys()
	starting_city = "Little Rock, Arkansas"
	print "Starting City: %s" %(starting_city)
	keys.remove(starting_city)

	last_city = starting_city
	Final_distances=[]
	Final_Path=[]
	Final_lats=[]
	Final_longs=[]

	for k in xrange(len(keys)):
		AllPossibleCombinations = list(itertools.permutations(keys, 1))
		# print AllPossibleCombinations

		distances = []
		for i in AllPossibleCombinations:
			# print i[0]
			distances.append(FindDistanceSquared(CityDict[last_city], CityDict[i[0]]))

		last_city = AllPossibleCombinations[distances.index(min(distances))][0]
		Final_Path.append([last_city, CityDict[last_city]])
		Final_lats.append(CityDict[last_city][0])
		Final_longs.append(CityDict[last_city][1])
		Final_distances.append(min(distances))
		keys.remove(last_city)
		# print last_city
	# print Final_Path
	print "Total Distance: %s" %(math.sqrt(sum(Final_distances)))
	plt.figure()
	plt.plot(Final_lats, Final_longs, '-0')
	plt.show()

if __name__ == "__main__":
	start_time = time.time()
	data = GrabData()
	PartA(data)
	print "Runtime: %s seconds" %(time.time() - start_time) 