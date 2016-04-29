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

def FindPathDistance(route):
	dist = 0
	last_stop = route[0]
	Final_lats = []
	Final_longs = []

	for k in route:
		Final_lats.append(data[k][0])
		Final_longs.append(data[k][1])
		dist += FindDistanceSquared(data[last_stop], data[k])
	return dist

def FindPathCoordinates(route):
	dist = 0
	last_stop = route[0]
	Final_lats = []
	Final_longs = []

	for k in route:
		Final_lats.append(data[k][0])
		Final_longs.append(data[k][1])
		dist += FindDistanceSquared(data[last_stop], data[k])
	return dist, Final_lats, Final_longs

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
	print Final_Path
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

def TwooptSwap(current_route, i, k):
	# print len(current_route)
	newPath = []
	newCoords = []
	temp = []

	newPath.append(current_route[0:i])
	newPath.append(list(reversed(current_route[i:k+1])))
	newPath.append(current_route[k+1:])

	newPath = [item for sublist in newPath for item in sublist]
	# print len(newPath)
	return newPath

def RunTwoOptSwap(bestPath):
	best_distance = FindPathDistance(bestPath)
	for i in xrange(len(bestPath)-1):
		for j in xrange(i+1, len(bestPath)+1):
			testPath = TwooptSwap(bestPath, i, j)
			this_dist= FindPathDistance(testPath)
			if this_dist < best_distance:
				best_distance = this_dist
				bestPath = testPath
				RunTwoOptSwap(bestPath)
	return bestPath
				
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
	# keys.remove(starting_city)
	# print len(keys)

	best_path = RunTwoOptSwap(keys)
	dist, Final_lats, Final_longs = FindPathCoordinates(best_path)
	print best_path
	print "Total Distance: %s" %(math.sqrt(dist))
	plt.figure()
	plt.plot(Final_lats, Final_longs, '-0')
	plt.show()

	
	# best_distance = 99999999999999999999999
	# bestPath = keys

	# for i in xrange(len(keys)-1):
	# 	for j in xrange(i+1, len(keys)+1):
	# 		testPath = TwooptSwap(keys, i, j)
	# 		# print len(testPath)

	# 		this_dist= FindPathDistance(testPath)
	# 		# print this_dist
	# 		if this_dist < best_distance:
	# 			best_distance = this_dist
	# 			bestPath = testPath
	# print best_distance, bestPath


	# last_city = starting_city
	# Final_distances=[]
	# Final_Path=[]
	# Final_lats=[]
	# Final_longs=[]
	# distances = []

	# Final_Path.append(last_city)
	# Final_lats.append(CityDict[last_city][0])
	# Final_longs.append(CityDict[last_city][1])

	# AllPermutations = list(itertools.permutations(keys, len(keys)))

	# for i in AllPermutations:
	# 	path_dist = 0
	# 	for j in i:
	# 		path_dist += FindDistanceSquared(CityDict[last_city], CityDict[j])
	# 		last_city = j
	# 	distances.append(path_dist)
	# 	# print path_dist
	# # print min(distances), AllPermutations[distances.index(min(distances))]

	# Final_Path = AllPermutations[distances.index(min(distances))]
	# # print Final_Path

	# # for k in Final_Path:
	# # 	Final_lats.append(CityDict[k][0])
	# # 	Final_longs.append(CityDict[k][1])
	# dist, Final_lats, Final_longs = FindPathDistance(Final_Path)

	# print Final_Path
	# print "Total Distance: %s" %(math.sqrt(sum(Final_distances)))
	# plt.figure()
	# plt.plot(Final_lats, Final_longs, '-0')
	# plt.show()

	# Final_Path.append([starting_city, CoordinateDictionary[starting_city]])

	# for k in xrange(len(keys)):
	# 	AllPossibleCombinations = list(itertools.permutations(keys, 1))
	# 	# print AllPossibleCombinations

	# 	distances = []
	# 	for i in AllPossibleCombinations:
	# 		# print i[0]
	# 		distances.append(FindDistanceSquared(CityDict[last_city], CityDict[i[0]]))

	# 	#### Look at path, if it intersects with any previous paths, draw a new one.

	# 	next_city = AllPossibleCombinations[distances.index(min(distances))][0]
	# 	# print(DoTheyIntersect(CityDict[last_city], CityDict[last_city][1], CityDict[next_city][0], CityDict[next_city][1]))

	# 	last_city = next_city

	# 	Final_Path.append([last_city, CityDict[last_city]])
	# 	Final_lats.append(CityDict[last_city][0])
	# 	Final_longs.append(CityDict[last_city][1])
	# 	Final_distances.append(min(distances))
	# 	keys.remove(last_city)
	# 	# print last_city
	# print Final_Path
	# print "Total Distance: %s" %(math.sqrt(sum(Final_distances)))
	# plt.figure()
	# plt.plot(Final_lats, Final_longs, '-0')
	# plt.show()

if __name__ == "__main__":
	start_time = time.time()
	data = GrabData()
	# PartA(data)
	PartB(data)
	print "Runtime: %s seconds" %(time.time() - start_time) 