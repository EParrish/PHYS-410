from __future__ import division
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# from numpy.fft import fft, fftfreq
# from math import ceil
import numpy as np

def GetData():

	times = []
	values = []

	with open("100x.csv", "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:
			times.append(float(row[0]))
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

	f = interp1d(times, values, kind='cubic')

	new_times = [i for i in xrange(1,950, 2)]
	new_data = f(new_times)


	plt.plot(new_times, new_data)
	plt.show()

def Part1Problem3():
	"""
	Write a function fitter: 
		The simplest one is a sine wave + linear equation and sum the two together. 
		Obviously you will need more than one linear equation because of the slope change. 
		Alternatively you might be able to fit a higher order curve to whatever you think 
		the baseline is, but the only way to fit the harmonics is with a sin wave. 

		linear:
			y = m(x-x1) + y1

		sine:
			y = A sin(B (x - C)) + D
	"""
	return

if __name__ == "__main__":
	Part1Problem2()