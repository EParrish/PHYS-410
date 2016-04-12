import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# hurricane_data = open("/home/elliot/PHYS 410/TEST.csv","r+")
# print hurricane_data
# print(hurricane_data.read())
# hurricane_data.readline()


# for line in hurricane_data:
# 	print "HELLO"	
# # 	# if line[3] == "NAMED":
# # 	print line[3]
# # 	# print len(line)

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def SortHurricane(declist, desc2, year):
	if desc2 == 1:
		declist[0]+=1
	elif desc2 == 2:
		declist[1]+=1
	elif desc2 == 3:
		declist[2]+=1
	elif desc2 == 4:
		declist[3]+=1
	elif desc2 == 5:
		declist[4]+=1

	return

Number2Dict={}
Number3Dict={}
Number4Dict={}

with open("master1.csv", "r+") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')
	# linecnt = 0

	for row in thisreader:
		ID = int(row[0])
		lattitude = float(row[1])
		longitude = float(row[2])
		wind_speed = float(row[3])
		pressure = float(row[4])
		year = int(row[5])
		run_time = float(row[6])
		descript1 = row[7] 
		descript2 = row[8]

		if lattitude <= 7:
			lattitude = 10*lattitude
		if longitude >= -10:
			longitude = 10*longitude

		###################################### Question 2
		if year < 1900:
			continue

		if descript1 == "HURRICAN":
			if ID not in Number2Dict.keys():
				Number2Dict[ID]=[year]
			else:
				if year not in Number2Dict[ID]:
					Number2Dict[ID].append(year)

Number2FinalData = []

for storm in Number2Dict.keys():
	for i in Number2Dict[storm]:
		Number2FinalData.append(i)

fig2 = plt.figure()
fig2.suptitle("Frequency of Hurricanes")

counts, bins, bars = plt.hist(Number2FinalData, 11)

bins = [1905, 1915, 1925, 1935, 1945, 1955, 1965, 1975, 1985, 1995, 2005]
print len(counts), len(bins)
plt.xlabel("Year")
plt.ylabel("Number of Hurricanes")
m,b = polyfit(bins, counts,1)
# plot(bins, counts, "yo", bins, m*bins+b, '--k')
print m,b
fig2_2 = plt.figure()
plot(bins, counts)

regress=[]
for i in bins:
	regress.append(m*i+b)
print(m*2030+b)

plot(bins, regress)
plt.show()
##################################################

		########################################## Question 3
# 		if year < 1950:
# 			continue
# 		if year not in Number3Dict.keys():
# 			Number3Dict[year]=0.0
# 		else:
# 			if lattitude >= 24.5 and lattitude <= 31:

# 				if longitude >= -87.6 and longitude <= -79.8:
# 					Number3Dict[year]+=0.25*wind_speed
					
# 			# else:
# 			# 	print "HELLO"

# Number3FinalDataYear=[]
# Number3FinalDataImpactFactor=[]
# for year in Number3Dict.keys():
# 	Number3FinalDataYear.append(year)
# 	Number3FinalDataImpactFactor.append(Number3Dict[year])
# 	# print year, Number3Dict[year]

# fig3 = plt.figure()
# plt.plot(Number3FinalDataYear, Number3FinalDataImpactFactor)
# fig3.suptitle("Impact Factor in Florida")
# plt.xlabel("Year")
# plt.ylabel("Impact Factor")
# plt.show()	

		######################################### Question 4
# 		if ID not in Number4Dict.keys():
# 			if pressure == 0.0:
# 				Number4Dict[ID] = 99999999999
# 			else:
#  				Number4Dict[ID] = pressure
# 		if pressure < Number4Dict[ID] and pressure != 0.0:
# 			Number4Dict[ID] = pressure

# Number4FinalData=[]
# for hurricane in Number4Dict.keys():
# 	if Number4Dict[hurricane] == 99999999999:
# 		continue
# 	Number4FinalData.append(Number4Dict[hurricane])
# 	# print hurricane, Number4Dict[hurricane]
# # print len(Number4FinalData)
# fig4 = plt.figure()
# plt.hist(Number4FinalData, 50)
# fig4.suptitle("Minimum Central Pressure")
# plt.xlabel("Minimum Central Pressure")
# plt.ylabel("Number of Storms")
# plt.show()

# print np.mean(Number4FinalData)
# print np.std(Number4FinalData)

###### Florida Corrdinates 24.5N to 31N, 79.8W to 87.6W


# ######################################## Question 5
# dec0=[0,0,0,0,0]
# dec1=[0,0,0,0,0]
# dec2=[0,0,0,0,0]
# dec3=[0,0,0,0,0]
# dec4=[0,0,0,0,0]
# dec5=[0,0,0,0,0]
# dec6=[0,0,0,0,0]
# dec7=[0,0,0,0,0]
# dec8=[0,0,0,0,0]
# dec9=[0,0,0,0,0]
# dec10=[0,0,0,0,0]
# Number5Dict={}
# ########

# with open("master1.csv", "r+") as csvfile:
# 	thisreader = csv.reader(csvfile, delimiter=',')
# 	# linecnt = 0

# 	for row in thisreader:
# 		ID = int(row[0])
# 		lattitude = float(row[1])
# 		longitude = float(row[2])
# 		wind_speed = float(row[3])
# 		pressure = float(row[4])
# 		year = int(row[5])
# 		run_time = float(row[6])
# 		descript1 = row[7] 
# 		descript2 = row[8]

# 		if "E-" in descript2:
# 			if ID not in Number5Dict.keys():
# 				Number5Dict[ID] = [int(descript2[-1:]), year]
# 			else:
# 				if Number5Dict[ID][0] < int(descript2[-1:]):
# 					Number5Dict[ID] = [int(descript2[-1:]), year]

# for storm in Number5Dict.keys():

# 	descript2 = Number5Dict[storm][0]
# 	year = Number5Dict[storm][1]

# 	if year >= 1900 and year < 1910:
# 		SortHurricane(dec0, descript2, year)

# 	elif year >= 1910 and year < 1920:
# 		SortHurricane(dec1, descript2, year)

# 	elif year >= 1920 and year < 1930:
# 		SortHurricane(dec2, descript2, year)	

# 	elif year >= 1930 and year < 1940:
# 		SortHurricane(dec3, descript2, year)

# 	elif year >= 1940 and year < 1950:
# 		SortHurricane(dec4, descript2, year)

# 	elif year >= 1950 and year < 1960:
# 		SortHurricane(dec5, descript2, year)

# 	elif year >= 1960 and year < 1970:
# 		SortHurricane(dec6, descript2, year)	

# 	elif year >= 1970 and year < 1980:
# 		SortHurricane(dec7, descript2, year)

# 	elif year >= 1980 and year < 1990:
# 		SortHurricane(dec8, descript2, year)

# 	elif year >= 1990 and year < 2000:
# 		SortHurricane(dec9, descript2, year)

# 	elif year >= 2000 and year < 2010:
# 		SortHurricane(dec10, descript2, year)

# labels = ["Cat 1", "Cat 2", "Cat 3", "Cat 4", "Cat 5"]

# fig5_0 = plt.figure()
# plt.pie(dec0, labels=labels,autopct='%1.1f%%')
# fig5_0.suptitle("1900-1910")
# plt.show()

# fig5_1 = plt.figure()
# plt.pie(dec1, labels=labels,autopct='%1.1f%%')
# fig5_1.suptitle("1910-1920")
# plt.show()

# fig5_2 = plt.figure()
# plt.pie(dec2, labels=labels,autopct='%1.1f%%')
# fig5_2.suptitle("1920-1930")
# plt.show()

# fig5_3 = plt.figure()
# plt.pie(dec3, labels=labels,autopct='%1.1f%%')
# fig5_3.suptitle("1930-1940")
# plt.show()

# fig5_4 = plt.figure()
# plt.pie(dec4, labels=labels,autopct='%1.1f%%')
# fig5_4.suptitle("1940-1950")
# plt.show()

# fig5_5 = plt.figure()
# plt.pie(dec5, labels=labels,autopct='%1.1f%%')
# fig5_5.suptitle("1950-1960")
# plt.show()

# fig5_6 = plt.figure()
# plt.pie(dec6, labels=labels,autopct='%1.1f%%')
# fig5_6.suptitle("1960-1970")
# plt.show()

# fig5_7 = plt.figure()
# plt.pie(dec7, labels=labels,autopct='%1.1f%%')
# fig5_7.suptitle("1970-1980")
# plt.show()

# fig5_8 = plt.figure()
# plt.pie(dec8, labels=labels,autopct='%1.1f%%')
# fig5_8.suptitle("1980-1990")
# plt.show()

# fig5_9 = plt.figure()
# plt.pie(dec9, labels=labels,autopct='%1.1f%%')
# fig5_9.suptitle("1990-2000")
# plt.show()

# fig5_10 = plt.figure()
# plt.pie(dec10, labels=labels,autopct='%1.1f%%')
# fig5_10.suptitle("2000-2009")
# plt.show()

# # print(dec0)
# # print(dec1)
# # print(dec2)
# # print(dec3)
# # print(dec4)
# # print(dec5)
# # print(dec6)
# # print(dec7)
# # print(dec8)
# # print(dec9)
# # print(dec10)
