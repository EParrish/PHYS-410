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

def DoTheyIntersect(p0, p1, p2, p3):
	"""
	returns True if lines intersect and False if they do not intersect
	Finds lines first, then solves the equations for intersection point. 
	Check if intersection is in the range/domain of segments.
	p0: first line, first point
	p1: first line, second point
	p2: second line, first point
	p3: second line, second point
	"""
	x0 = p0[0]; y0 = p0[1];
	x1 = p1[0];	y1 = p1[1];
	x2 = p2[0]; y2 = p2[1];
	x3 = p3[0]; y3 = p3[1];

	if x0 == x1:
		# First line is vertical. Slope will not work.
		pass
	if x2 == x3:
		# Second line is vertical. Slope will not work.
		pass

	slope1 = (p1[0] - p0[0]) / (p1[1] - p0[1])
	slope2 = (p3[0] - p2[0]) / (p3[1] - p2[1])

	if slope1 == slope2:
		# lines are parallel. They never intersect
		return False

	# Taken from Wikipedia https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection 
	xintersect = ((x0*y1 - y0*x1)*(x2-x3) - (x0-x1)*(x3*y3-y2*x3)) / ((x0-x1)*(y2-y3) - (y0-y1)*(x2-x3))

	yintersect = ((x0*y1-y0*x1)*(y2-y3) - (y0-y1)*(x2*y3-y2*x3)) / ((x0-x1)*(y2-y3) - (y0-y1)*(x2-x3))

	bigger_x1 = max([x0,x1]); smaller_x1 = min([x0,x1]);
	bigger_y1 = max([y0,y1]); smaller_y1 = min([y0,y1]);

	bigger_x2 = max([x2,x3]); smaller_x2 = min([x2,x3]);
	bigger_y2 = max([y2,y3]); smaller_y2 = min([y2,y3]);


	if xintersect >= smaller_x1 and xintersect <= bigger_x1:
		if xintersect >= smaller_x2 and xintersect <= bigger_x2:
			if yintersect >= smaller_y1 and yintersect <= bigger_y1:
				if yintersect >= smaller_y2 and yintersect <= bigger_y2:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False


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

		#### Look at path, if it intersects with any previous paths, draw a new one.



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