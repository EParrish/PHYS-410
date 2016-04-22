from ROOT import *
import csv

gStyle.SetOptStat(0)
h1 = TH2D("h1", "Picture A Mean Box Values;Box Size;Mean Pixel Intensity;Number of Occurances", 30, 0, 30, 250, 0, 250)
h2 = TH2D("h2", "Picture A STD Box Values;Box Size;STD;Number of Occurances", 30, 0, 30, 50, 0, 50)

with open("Problem3Output_A_20.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=' ')
	for row in thisreader:

		box_size = float(row[0])
		x = float(row[1])
		y = float(row[2])
		mean = float(row[3])
		std = float(row[4])
		# print mean
		h1.Fill(box_size, mean)
		h2.Fill(box_size, std)

with open("Problem3Output_A_4.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')
	for row in thisreader:

		box_size = float(row[0])
		x = float(row[1])
		y = float(row[2])
		mean = float(row[3])
		std = float(row[4])

		h1.Fill(box_size, mean)
		h2.Fill(box_size, std)

with open("Problem3Output_A_10.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=' ')
	for row in thisreader:

		box_size = float(row[0])
		x = float(row[1])
		y = float(row[2])
		mean = float(row[3])
		std = float(row[4])

		h1.Fill(box_size, mean)
		h2.Fill(box_size, std)

with open("Problem3Output_A_16.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=' ')
	for row in thisreader:

		box_size = float(row[0])
		x = float(row[1])
		y = float(row[2])
		mean = float(row[3])
		std = float(row[4])

		h1.Fill(box_size, mean)
		h2.Fill(box_size, std)

c1 = TCanvas("c1")
c1.SetRightMargin(0.13)
h1.Draw("COLZ")

c2 = TCanvas("c2")
c2.SetRightMargin(0.13)
h2.Draw("COLZ")
raw_input("Press Enter to Quit")