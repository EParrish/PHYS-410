from __future__ import division
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy.fft import fft
from math import ceil

def GetData():
	depth = []
	iceage = []
	deltaD = []
	tempdiff = []

	with open("Icecore.csv", "r") as csvfile:
		thisreader = csv.reader(csvfile, delimiter=',')

		for row in thisreader:
			depth.append(float(row[0]))
			iceage.append(float(row[1]))
			deltaD.append(float(row[2]))
			tempdiff.append(float(row[3]))
	return depth, iceage, deltaD, tempdiff

def Problem2():
	'''
	a) Report the number of lines
	b) Make a plot of D vs time.
	c) Demonstrate that the data are not evenly spread
	'''
	depth, iceage, deltaD, tempdiff = GetData()
	plt.plot(iceage, deltaD)
	plt.ylabel("$\delta$ D")
	plt.xlabel("Time [years since present]")
	plt.show()


	plt.plot(iceage, depth)
	plt.ylabel("Depth [m]")
	plt.xlabel("Time [years since present]")
	plt.show()

	return

def Problem3(N):
	'''
	Rebin D into 2n data points that are evenly spaced in time.
	
	'''

	depth, iceage, deltaD, tempdiff = GetData()
	
	max_year = int(max(iceage))

	numbins = 2**N
	# print numbins
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	cut_deltaD = deltaD[:len(new_data)]

	print len(new_data)

	plt.figure()
	plt.plot(iceage, deltaD, label="Raw Data", linewidth=0.5)
	plt.plot(new_years, new_data, label="Interpolated Data", linewidth=0.5)
	plt.title("N = %s"%(N))
	plt.ylabel("$\delta$ D")
	plt.xlabel("Time [years since present]")
	plt.legend()
	plt.show()
	
	return

def Problem4():
	depth, iceage, deltaD, tempdiff = GetData()
	
	max_year = int(max(iceage))

	numbins = 2**N
	# print numbins
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	cut_deltaD = deltaD[:len(new_data)]



if __name__ == '__main__':
	# Problem2()
	# Problem3(7)
	# Problem3(11)
	# Problem3(15)
	Problem4()
