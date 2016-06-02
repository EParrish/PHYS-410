import csv
import numpy as np

def GrabData():
	longs = list(np.arange(1,360, 2))
	lats = list(np.arange(-79.5, 90, 1))
	Dates = ["2001-01-01","2001-02-01","2001-03-01","2001-04-01","2001-05-01","2001-06-01","2001-07-01","2001-08-01","2001-09-01","2001-10-01","2001-11-01","2001-12-01",
	"2002-01-01","2002-02-01","2002-03-01","2002-04-01","2002-05-01","2002-06-01","2002-07-01","2002-08-01","2002-09-01","2002-10-01","2002-11-01","2002-12-01",] # Keys for data dictionary using starting month as key
	Full_Data = {}

	with open("tos.csv", "r") as csvfile:
		# The data is actually upside down. it starts in the southern hemisphere and goes north. But that doesn't matter because of the dictionaries.
		thisreader = csv.reader(csvfile, delimiter=',')
		month = 0
		this_data_set = {}
		lat_index = 0

		for row in thisreader:
			if len(row) == 0:
				Full_Data[Dates[month]] = this_data_set
				###### New Month Data Set
				this_data_set = {}
				month+=1
				lat_index=0
				continue

			long_index=0 
			# print row
			# print lats[169]
			for val in row:
				# print month
				# print long_index, lat_index
				# print longs[long_index]
				# print lats[lat_index]
				this_data_set["%s, %s" %(longs[long_index], lats[lat_index])] = (float(val))
				long_index+=1

			lat_index+=1

	Full_Data[Dates[-1]] = this_data_set
	return Full_Data

def Part2Problem1():
	"""
	 Define 4 regions that correspond to 

	a) the equatorial pacific ocean 
	b) the Gulf of Mexico 
	c) The Nothern Indian Ocean 
	d) The southern California Coast 


	Determine the rate of temperature increase from March to September 
	in these 4 regions and plot all 4 of these temperature gradients on one plot 

	Region 1: Equatorial Pacific Ocean
			  long: -120 to -170
			  lat: 5 to -5
	Region 2: Gulf of Mexico
			  long: -100 to -80
			  lat: 30 to 15
	Region 3: Northern Indian Ocean
			  long: 40 to 135
			  lat: -30 to 25
	Region 4: Southern California Coast
			  long: -125 to -117
			  lat: 32 to 37

  	Full_Data keys:
		["2001-01-01","2001-02-01","2001-03-01","2001-04-01","2001-05-01","2001-06-01","2001-07-01","2001-08-01","2001-09-01","2001-10-01","2001-11-01","2001-12-01",
		"2002-01-01","2002-02-01","2002-03-01","2002-04-01","2002-05-01","2002-06-01","2002-07-01","2002-08-01","2002-09-01","2002-10-01","2002-11-01","2002-12-01",]

  	"""
  	Full_Data = GrabData()

  	March_to_Sept = ["2001-04-01", "2001-09-01", "2002-04-01","2002-09-01"]

  	# Region 1: Equatorial Pacific Ocean
	#	      long: -120 to -170
	#		  lat: 5 to -5

	longs1 = list(np.arange(119+180, 169+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats1 = list(np.arange(-4.5, 5.5, 1))
	diffs1 = []

	for long1 in longs1:
		for lat1 in lats1:
			diffs1.append(Full_Data[March_to_Sept[0]]["%s, %s" %(long1, lat1)] - Full_Data[March_to_Sept[1]]["%s, %s" %(long1, lat1)])
			diffs1.append(Full_Data[March_to_Sept[2]]["%s, %s" %(long1, lat1)] - Full_Data[March_to_Sept[3]]["%s, %s" %(long1, lat1)])
	avg_dif1 = np.nansum(diffs1) / float(len(diffs1))


	# Region 2: Gulf of Mexico
	# 		  long: -100 to -80
	# 		  lat: 30 to 15

	longs2 = list(np.arange(79+180, 99+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats2 = list(np.arange(14.5, 30.5, 1))
	diffs2 = []

	for long2 in longs2:
		for lat2 in lats2:
			diffs2.append(Full_Data[March_to_Sept[0]]["%s, %s" %(long2, lat2)] - Full_Data[March_to_Sept[1]]["%s, %s" %(long2, lat2)])
			diffs2.append(Full_Data[March_to_Sept[2]]["%s, %s" %(long2, lat2)] - Full_Data[March_to_Sept[3]]["%s, %s" %(long2, lat2)])
	avg_dif2 = np.nansum(diffs2) / float(len(diffs2))


	# Region 3: Northern Indian Ocean
	# 		  long: 40 to 135
	# 		  lat: -30 to 25

	longs3 = list(np.arange(49, 135, 2)) # Data is measured from 1-360 starting at meridian going east
	lats3 = list(np.arange(-29.5, 25.5, 1))
	diffs3 = []

	for long3 in longs3:
		for lat3 in lats3:
			diffs3.append(Full_Data[March_to_Sept[0]]["%s, %s" %(long3, lat3)] - Full_Data[March_to_Sept[1]]["%s, %s" %(long3, lat3)])
			diffs3.append(Full_Data[March_to_Sept[2]]["%s, %s" %(long3, lat3)] - Full_Data[March_to_Sept[3]]["%s, %s" %(long3, lat3)])
	avg_dif3 = np.nansum(diffs3) / float(len(diffs3))


	# Region 4: Southern California Coast
	# 		  long: -125 to -117
	# 		  lat: 32 to 37

	longs4 = list(np.arange(117+180, 125+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats4 = list(np.arange(31.5, 37.5, 1))
	diffs4 = []

	for long4 in longs4:
		for lat4 in lats4:
			diffs4.append(Full_Data[March_to_Sept[0]]["%s, %s" %(long4, lat4)] - Full_Data[March_to_Sept[1]]["%s, %s" %(long4, lat4)])
			diffs4.append(Full_Data[March_to_Sept[2]]["%s, %s" %(long4, lat4)] - Full_Data[March_to_Sept[3]]["%s, %s" %(long4, lat4)])
	avg_dif4 = np.nansum(diffs4) / float(len(diffs4))

  	print avg_dif1, avg_dif2, avg_dif3, avg_dif4

def Part2Problem2():
	"""
	 Define 4 regions that correspond to 

	a) the equatorial pacific ocean 
	b) the Gulf of Mexico 
	c) The Nothern Indian Ocean 
	d) The southern California Coast 


	Determine the rate of temperature increase from March to September 
	in these 4 regions and plot all 4 of these temperature gradients on one plot 

	Region 1: Equatorial Pacific Ocean
			  long: -120 to -170
			  lat: 5 to -5
	Region 2: Gulf of Mexico
			  long: -100 to -80
			  lat: 30 to 15
	Region 3: Northern Indian Ocean
			  long: 40 to 135
			  lat: -30 to 25
	Region 4: Southern California Coast
			  long: -125 to -117
			  lat: 32 to 37

  	Full_Data keys:
		["2001-01-01","2001-02-01","2001-03-01","2001-04-01","2001-05-01","2001-06-01","2001-07-01","2001-08-01","2001-09-01","2001-10-01","2001-11-01","2001-12-01",
		"2002-01-01","2002-02-01","2002-03-01","2002-04-01","2002-05-01","2002-06-01","2002-07-01","2002-08-01","2002-09-01","2002-10-01","2002-11-01","2002-12-01",]

  	"""
  	Full_Data = GrabData()

  	March_to_Sept = ["2001-04-01", "2001-09-01", "2002-04-01","2002-09-01"]

  	# Region 1: Equatorial Pacific Ocean
	#	      long: -120 to -170
	#		  lat: 5 to -5

	longs1 = list(np.arange(119+180, 169+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats1 = list(np.arange(-4.5, 5.5, 1))
	diffs1 = []

	for long1 in longs1:
		for lat1 in lats1:
			diffs1.append(Full_Data[March_to_Sept[1]]["%s, %s" %(long1, lat1)] - Full_Data[March_to_Sept[0]]["%s, %s" %(long1, lat1)])
			diffs1.append(Full_Data[March_to_Sept[3]]["%s, %s" %(long1, lat1)] - Full_Data[March_to_Sept[2]]["%s, %s" %(long1, lat1)])
	avg_dif1 = np.nansum(diffs1) / float(len(diffs1))


	# Region 2: Gulf of Mexico
	# 		  long: -100 to -80
	# 		  lat: 30 to 15

	longs2 = list(np.arange(79+180, 99+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats2 = list(np.arange(14.5, 30.5, 1))
	diffs2 = []

	for long2 in longs2:
		for lat2 in lats2:
			diffs2.append(Full_Data[March_to_Sept[1]]["%s, %s" %(long2, lat2)] - Full_Data[March_to_Sept[0]]["%s, %s" %(long2, lat2)])
			diffs2.append(Full_Data[March_to_Sept[3]]["%s, %s" %(long2, lat2)] - Full_Data[March_to_Sept[2]]["%s, %s" %(long2, lat2)])
	avg_dif2 = np.nansum(diffs2) / float(len(diffs2))


	# Region 3: Northern Indian Ocean
	# 		  long: 40 to 135
	# 		  lat: -30 to 25

	longs3 = list(np.arange(49, 135, 2)) # Data is measured from 1-360 starting at meridian going east
	lats3 = list(np.arange(-29.5, 25.5, 1))
	diffs3 = []

	for long3 in longs3:
		for lat3 in lats3:
			diffs3.append(Full_Data[March_to_Sept[1]]["%s, %s" %(long3, lat3)] - Full_Data[March_to_Sept[0]]["%s, %s" %(long3, lat3)])
			diffs3.append(Full_Data[March_to_Sept[3]]["%s, %s" %(long3, lat3)] - Full_Data[March_to_Sept[2]]["%s, %s" %(long3, lat3)])
	avg_dif3 = np.nansum(diffs3) / float(len(diffs3))


	# Region 4: Southern California Coast
	# 		  long: -125 to -117
	# 		  lat: 32 to 37

	longs4 = list(np.arange(117+180, 125+180, 2)) # Data is measured from 1-360 starting at meridian going east
	lats4 = list(np.arange(31.5, 37.5, 1))
	diffs4 = []

	for long4 in longs4:
		for lat4 in lats4:
			diffs4.append(Full_Data[March_to_Sept[1]]["%s, %s" %(long4, lat4)] - Full_Data[March_to_Sept[0]]["%s, %s" %(long4, lat4)])
			diffs4.append(Full_Data[March_to_Sept[3]]["%s, %s" %(long4, lat4)] - Full_Data[March_to_Sept[2]]["%s, %s" %(long4, lat4)])
	avg_dif4 = np.nansum(diffs4) / float(len(diffs4))

  	print avg_dif1, avg_dif2, avg_dif3, avg_dif4

if __name__ == "__main__":
	Part2Problem1()