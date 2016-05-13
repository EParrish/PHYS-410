from __future__ import division
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy.fft import fft, fftfreq
from math import ceil
import numpy as np

def GetData(flag):
	if flag.lower() == "ice":
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

	elif flag.lower() == "cascadia":
		years=[]
		values=[]

		with open("Cascadia.csv", "r") as csvfile:
			thisreader = csv.reader(csvfile, delimiter=',')

			for row in thisreader:
				years.append(int(row[0]))
				before_average=[]
				for i in xrange(len(row)):
					if i == 0:
						continue
					elif row[i] == "":
						continue
					else:
						before_average.append(float(row[i]))
				values.append(sum(before_average)/len(before_average))
		
		return None, years, values, None

def Problem2():
	'''
	a) Report the number of lines
	b) Make a plot of D vs time.
	c) Demonstrate that the data are not evenly spread
	'''
	depth, iceage, deltaD, tempdiff = GetData("Ice")
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

	depth, iceage, deltaD, tempdiff = GetData("Cascadia")
	
	max_year = int(max(iceage))

	numbins = 2**N
	# print numbins
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	# cut_deltaD = deltaD[:len(new_data)]

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

def Problem4(N):
	depth, iceage, deltaD, tempdiff = GetData("Ice")
	
	max_year = int(max(iceage))

	numbins = 2**N
	# print numbins
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	cut_deltaD = deltaD[:len(new_data)]

	x = fft(new_data)
	print "FFT Sum: %s Original Sum: %s" %(x[0].real, sum(deltaD))
	
	return

def Problem5(N):
	depth, iceage, deltaD, tempdiff = GetData("Ice")
	
	max_year = int(max(iceage))

	numbins = 2**N
	
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	cut_deltaD = deltaD[:len(new_data)]

	x = fft(new_data)
	
	Amplitudes=[]

	for i in xrange(x.size):
		if i == 0:
			continue
		if i <= x.size/2:
			a = x[i].real
			b = x[i].imag
			new_val = a**2+b**2
			Amplitudes.append(new_val)
		else:
			break

	Amplitudes = np.asarray(Amplitudes)
	freq = fftfreq(new_data.shape[-1])
	freq = freq[:freq.size/2]

	plt.figure()
	plt.plot(freq, Amplitudes/(max(Amplitudes)))
	# plt.plot(freq, x.real, freq, x.imag)
	plt.title("N = %s"%(N))
	plt.ylabel("Amplitude [Normalized To Max Value]")
	plt.xlabel("Frequency [Hz]")
	if N == 7:
		plt.xlim(0,0.5)
	elif N == 11:
		plt.xlim(0,0.05)
	elif N == 15:
		plt.xlim(0,0.004)

	plt.show()

	return

def Problem6(N):
	depth, iceage, deltaD, tempdiff = GetData("Ice")
	
	max_year = int(max(iceage))

	numbins = 2**N
	
	spacing = int(ceil(max_year/numbins)) 
	new_years = [i for i in xrange(0,max_year,spacing)]
	
	f = interp1d(iceage, deltaD)

	new_data = f(new_years)
	cut_deltaD = deltaD[:len(new_data)]

	x = fft(new_data)
	
	Amplitudes=[]

	for i in xrange(x.size):
		if i == 0:
			continue
		if i <= x.size/2:
			a = x[i].real
			b = x[i].imag
			new_val = a**2+b**2
			Amplitudes.append(new_val)
		else:
			break

	Amplitudes = np.asarray(Amplitudes)
	freq = fftfreq(new_data.shape[-1])
	freq = freq[:50]
	Amplitudes = Amplitudes[:50]

	plt.figure()
	plt.plot(freq, Amplitudes/(max(Amplitudes)))
	# plt.plot(freq, x.real, freq, x.imag)
	plt.title("N = %s"%(N))
	plt.ylabel("Amplitude [Normalized To Max Value]")
	plt.xlabel("Frequency [Hz]")
	if N == 7:
		plt.xlim(0,max(freq))
	elif N == 11:
		plt.xlim(0,max(freq))
	elif N == 15:
		plt.xlim(0,max(freq))

	plt.show()

if __name__ == '__main__':
	# Problem2()
	Problem3(7)
	Problem3(11)
	Problem3(15)
	# Problem4(7)
	# Problem4(11)
	# Problem4(15)
	# # Problem5(7)
	# # Problem5(11)
	# # Problem5(15)
	# Problem6(7)
	# Problem6(11)
	# Problem6(15)
