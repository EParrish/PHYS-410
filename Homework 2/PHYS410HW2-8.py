# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 16:29:24 2016

@author: brown_000
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
TheArray = pd.read_csv('C://Users/brown_000/Desktop/master1.csv')
TheArray.as_matrix()
TheArray = np.array(TheArray)
#Now Do the actual problem

for i in range(0,np.shape(TheArray)[0]):
    if TheArray[i,1] <=7:
        TheArray[i,1] = 10*TheArray[i,1]
    if TheArray[i,2] >=-10:
        TheArray[i,2] = 10*TheArray[i,2]
Test=[]
for i in range(0,np.shape(TheArray)[0]):
    if TheArray[i,1] >=15 and TheArray[i,1] <= 22 and TheArray[i,2] >= -65 and TheArray[i,2] <= -50:
        StormID = TheArray[i,0]
        Year = TheArray[i,5]
        Lat = TheArray[i,1]
        Category = TheArray[i,8]
        Row = [StormID, Year, Lat, Category]
        Test = np.append(Test,Row)

for i in range(0,len(Test)):
    if Test[i] == "E-1":
        Test[i] = 1
    if Test[i] == "E-2":
        Test[i] = 2
    if Test[i] == "E-3":
        Test[i] = 3
    if Test[i] == "E-4":
        Test[i] = 4
    if Test[i] == "E-5":
        Test[i] = 5
    if Test[i] == "STORM" or Test[i] == "DEPRESSION":
        Test[i] = 0

LatArray = np.zeros((len(Test)/4,4))
for i in range (0,len(Test)/4):
    LatArray[i,0] = Test[4*i]
    LatArray[i,1] = Test[4*i+1]
    LatArray[i,2] = Test[4*i+2]
    LatArray[i,3] = Test[4*i+3]
print LatArray
Test2 = [371., 1900.,16.1,0] 
for i in range(1,np.shape(LatArray)[0]):
    if LatArray[i,0] != LatArray[i-1,0]:
        Row = LatArray[i,:]
        Test2 = np.append(Test2,Row)

LatArray2 = np.zeros((len(Test2)/4,4))

for i in range (0,len(Test2)/4):
    LatArray2[i,0] = Test2[4*i]
    LatArray2[i,1] = Test2[4*i+1]
    LatArray2[i,2] = Test2[4*i+2]
    LatArray2[i,3] = Test2[4*i+3]
    
Storms1900 = 15
Storms1910 = 11
Storms1920 = 13
Storms1930 = 22
Storms1940 = 14
Storms1950 = 29
Storms1960 = 21
Storms1970 = 11
Storms1980 = 15
Storms1990 = 21
Storms2000 = 18
x=(1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000)
y = (15,11,13,22,14,29,21,11,15,21,18)

plt.figure(1)
plt.title("Storms Per Year in the Carribean")
plt.xlabel("Year")
plt.ylabel("Number of Sotrms")
plt.plot(x,y)