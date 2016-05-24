from __future__ import division
import csv
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
# from numpy.fft import fft, fftfreq
from math import sin
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

	plt.plot(times, new_data)
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
	rand_value1 = filtered_data[rand_index1]
	rand_time1 = times[rand_index1]
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
	m2 = (filtered_data[-1] - line1_values[-1]) / (times[-1] - times[670])
	line2_values = [m2*(x-times[670])+line1_values[-1] for x in xrange(670, len(times))]

	###############################################

	################## Sine Fits ##################
	# y = A*sin(B (x-C)) + D
	# Use linear fit as midline, so no need for D

	####### Works, but not the greatest. 
	####### Need to figure out periods (easiest would be to make random choice)
	####### Amplitudes for second sine function seem way too large.


	Amplitudes1 = [abs(filtered_data[point] - line1_values[point]) for point in xrange(len(line1_times))]
	A1 = sum(Amplitudes1)/(len(Amplitudes1))
	sin1_values = [A1*sin(line1_times[x]) + line1_values[x] for x in xrange(len(line1_times))]

	Amplitudes2 = [abs(filtered_data[point] - line2_values[point]) for point in xrange(len(line2_times))]
	A2 = sum(Amplitudes2)/(len(Amplitudes2))
	sin2_values = [A2*sin(line2_times[x]) + line2_values[x] for x in xrange(len(line2_times))]

	###############################################

	plt.figure()
	plt.plot(times, filtered_data)
	plt.plot(line1_times, line1_values)
	plt.plot(line2_times, line2_values)
	plt.plot(line1_times, sin1_values)
	plt.plot(line2_times, sin2_values)
	plt.title("Fitted Data")
	plt.axis([0,1003,6000,10000])
	plt.show()
	return

if __name__ == "__main__":
	# Part1Problem2()
	Part1Problem3()