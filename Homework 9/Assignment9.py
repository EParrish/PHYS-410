from __future__ import division
import csv
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
# from numpy.fft import fft, fftfreq
from math import sin, pi
import numpy as np
from random import randint

def GetData():

	times = []
	values = []

	with open("100x.csv", "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:
			times.append(int(row[0]))
			values.append(float(row[1]))

	return times, values

def Part1Problem2():
	"""
	Smooth the data using any procedure that you want 
	you need to balance your smooth width with reduced noise 
	vs loss of feature resolution. 
	Your smoothed data set should look something like this: 
	"""
	times, values = GetData()


	# Interpolation didn't work very well
	# f = interp1d(times, values, kind='cubic')

	# new_times = [i for i in xrange(1,950, 2)]
	# new_data = f(new_times)

	# Gaussian filtering from Eryn's suggestion
	sigma_gaussian = 1.5
	new_data = gaussian_filter(values, sigma_gaussian)

	# plt.plot(times, values, color="b")
	plt.plot(times, new_data, color="r")
	plt.title("Filtered Data")
	plt.axis([0,1003,6000,10000])
	plt.show()
	return times, new_data

def Part1Problem3():
	"""
	Write a function fitter: 
		The simplest one is a sine wave + linear equation and sum the two together. 
		Obviously you will need more than one linear equation because of the slope change. 
		Alternatively you might be able to fit a higher order curve to whatever you think 
		the baseline is, but the only way to fit the harmonics is with a sin wave. 

		linear:
			y = mx+b

		sine:
			y = A sin(B (x - C)) + D


	I apologize in advance, this code is super hard to read, 
	but I think it will speed it up the way it is written.

	Right now the sine functions are dependent on the lines drawn.
	Their midlines are the linear fits, so the amplitudes it finds 
	are based on the goodness of the linear fits.
	"""
	times, values = GetData()
	sigma_gaussian = 1.5
	filtered_data = gaussian_filter(values, sigma_gaussian)

	################## Linear Fits ##################
	# y = mx+b 
	# y = m(x-x1) + y1

	b1 = filtered_data[0]
	rand_index1 = randint(0, 671)
	rand_value1 = 9500 # filtered_data[rand_index1]
	rand_time1 = 671 # times[rand_index1]
	m1 = (rand_value1 - filtered_data[0]) / (rand_time1 - times[0])
	line1_times = [i for i in xrange(0,671)]
	line1_values = [m1*x+b1 for x in xrange(0, 671)]
	# print len(line1_times), len(line1_values)

	##### Not what we want, this will make the second line random, we want them to connect
	# rand_index2 = randint(670, len(times))
	# rand_time2 = times[rand_index2]
	# rand_value2 = filtered_data[rand_index2]
	# m2 = (filtered_data[-1] - rand_value2) / (times[-1] - rand_time2)
	# line2_times = [i for i in xrange(672, len(times))]
	# line2_values = [m2*(x-rand_time2)+rand_value2 for x in xrange(672, len(times))]

	#### Connects the lines within rounding
	line2_times = [i for i in xrange(670, len(times))]
	average=0
	for i in xrange(975,line2_times[-1]+1):
		average+=filtered_data[i]
	average = average / ((line2_times[-1]+1) - 975)
	m2 = (average - filtered_data[670]) / (times[-1] - times[670])
	line2_values = [m2*(x-times[670])+filtered_data[670] for x in xrange(670, len(times))]

	###############################################

	################## Sine Fits ##################
	# y = A*sin(B (x-C)) + D
	# Use linear fit as midline, so no need for D
 
	####### Works, but not the greatest. 
	####### Need to figure out periods (easiest would be to make random choice)
	####### Amplitudes for second sine function seem way too large.

	Amplitudes1 = [abs(filtered_data[point] - line1_values[point]) for point in xrange(len(line1_times))]
	A1 = sum(Amplitudes1)/(len(Amplitudes1))
	B1 = (2*pi)/47
	sin1_values = [A1*sin(B1*line1_times[x]-pi/2) + line1_values[x] for x in xrange(len(line1_times))]

	Amplitudes2 = []
	for point in xrange(len(line2_times)):
		Amplitudes2.append(abs(filtered_data[point+670] - line2_values[point]))

	B2 = (2*pi)/47
	A2 = sum(Amplitudes2)/(len(Amplitudes2))
	sin2_values = [A2*sin(B2*line2_times[x]+pi/2) + line2_values[x] for x in xrange(len(line2_times))]

	del sin2_values[0]
	FinalFit_Values = sin1_values + sin2_values

	###############################################

	################## Chi Squared ################

	numerator = [((filtered_data[x] - FinalFit_Values[x])**2)/(FinalFit_Values[x]) for x in xrange(len(filtered_data))]
	ChiSqrd = sum(numerator)
	print "Chi Squared Value is: %s" %ChiSqrd
	###############################################

	plt.figure()
	plt.plot(times, filtered_data)
	# plt.plot(line1_times, line1_values)
	# plt.plot(line2_times, line2_values)
	plt.plot(times, FinalFit_Values, color='red')
	# plt.plot(line1_times, sin1_values)
	# plt.plot(line2_times, sin2_values)
	plt.title("Fitted Data")
	plt.axis([0,1003,6000,10000])
	plt.show()
	return

def Part1Problem4(filtered_data, line1fits, line2fits, sine1fits, sine2fits):
	"""
	You will want to write code which will immediately pass through your parameter changes 
	(line slopes, periods, amplitude, etc) and draw the function through the data so you 
	can iterate manually towards some approximate solution. 
	"""
	##################################################### Start fixing here

	################## Linear Fits ##################
	# y = mx+b 
	# y = m(x-x1) + y1

	b1 = line1fits[1]
	m1 = line1fits[0]
	line1_times = [i for i in xrange(0,671)]
	line1_values = [m1*x+b1 for x in xrange(0, 671)]

	########################################## What do want to do with this line? Connect or anchor on left and search slopes?
	# right now it's written to search slopes
	m2 = line2fits[0]
	line2_times = [i for i in xrange(670, len(times))]
	line2_values = [m2*(x-line2_times[-1]+1)+filtered_data[-1] for x in xrange(670, len(times))]

	###############################################

	################## Sine Fits ##################
	# y = A*sin(B (x-C)) + D
	# Use linear fit as midline, so no need for D

	A1 = sine1fits[0]
	B1 = sine1fits[1]
	sin1_values = [A1*sin(B1*line1_times[x]-pi/2) + line1_values[x] for x in xrange(len(line1_times))]

	A2 = sine2fits[0]
	B2 = sine2fits[1]
	sin2_values = [A2*sin(B2*line2_times[x]+pi/2) + line2_values[x] for x in xrange(len(line2_times))]

	del sin2_values[0]
	FinalFit_Values = sin1_values + sin2_values

	###############################################

	################## Chi Squared ################

	numerator = [((filtered_data[x] - FinalFit_Values[x])**2)/(FinalFit_Values[x]) for x in xrange(len(filtered_data))]
	ChiSqrd = sum(numerator)
	print ChiSqrd
	###############################################

	plt.figure()
	plt.plot(times, filtered_data)
	plt.plot(times, FinalFit_Values)
	plt.title("Fitted Data")
	plt.axis([0,1003,6000,10000])
	plt.show()
	return

def Part1Problem6():
	"""
	With your approximate fit now write a blind random search algorithm, 
	as explained in class, using your now best guesses for parameters min and max, 
	and then choose your random step size to add to the min parameter per iteration. 
	You will want to output your chi squared values per iteration so you can see if you're
	converging or not.
	"""
	times, values = GetData()
	sigma_gaussian = 1.5
	filtered_data = list(gaussian_filter(values, sigma_gaussian))
	
	data_set1 = filtered_data[:670]
	time_set1 = times[:670]
	data_set2 = filtered_data[670:]
	time_set2 = times[670:]

	################## First Slope Range #################
	max_index1 = data_set1.index(max(data_set1))
	max_m1 = (data_set1[max_index1] - filtered_data[0]) / (time_set1[max_index1] - times[0])
	min_index1 = data_set1.index(min(data_set1))
	min_m1 = (data_set1[min_index1] - filtered_data[0]) / (time_set1[min_index1] - times[0])
	######################################################

	################## Second Slope Range ################
	max_index2 = data_set2.index(max(data_set2))
	max_m2 = (data_set2[max_index2] - filtered_data[-1]) / (time_set2[max_index2] - (times[-1]+1))
	min_index2 = data_set2.index(min(data_set2))
	min_m2 = (data_set2[min_index2] - filtered_data[-1]) / (time_set2[min_index2] - (times[-1]+1))
	######################################################

	print min_m1, max_m1
	print min_m2, max_m2

if __name__ == "__main__":
	# Part1Problem2()
	# Part1Problem3()
	Part1Problem6()