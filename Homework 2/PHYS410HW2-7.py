# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 12:24:21 2016

@author: brown_000
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
TheArray = pd.read_csv('C://Users/brown_000/Desktop/master1.csv')
TheArray.as_matrix()
TheArray = np.array(TheArray)
Test = []
for i in range(0,np.shape(TheArray)[0]):
    if TheArray[i,8] == "E-3" or TheArray[i,8] == "E-4" or TheArray[i,8] == "E-5":
        StormID = TheArray[i,0]
        Year = TheArray[i,5]
        Time = TheArray[i,6]
        Category = TheArray[i,8]
        Row = [StormID,Year,Time,Category]
        Test = np.append(Test,Row)

CatArray = np.zeros((len(Test)/4,4))
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


for i in range (0,len(Test)/4):
    CatArray[i,0] = Test[4*i]
    CatArray[i,1] = Test[4*i+1]
    CatArray[i,2] = Test[4*i+2]
    CatArray[i,3] = Test[4*i+3]
Test2 = []
for i in  range(1,np.shape(CatArray)[0]):
    if CatArray[i,0] != CatArray[i-1,0]:
        Start = CatArray[i,2]
        for j in range(0,50):
            if i+j+1 == np.shape(CatArray)[0]:
                break
            if CatArray[i+j,0] != CatArray[i+j+1,0]:
                Finish = CatArray[i+j,2]
                Duration = Finish - Start
                StormID = CatArray[i,0]
                Year = CatArray[i,1]
                Category = CatArray[i,3]
                Row = [StormID,Year,Duration,Category]
                Test2 = np.append(Test2,Row)
                break
CatArray2 = np.zeros((len(Test2)/4,4))
for i in range (0,len(Test2)/4):
    CatArray2[i,0] = Test2[4*i]
    CatArray2[i,1] = Test2[4*i+1]
    CatArray2[i,2] = Test2[4*i+2]
    CatArray2[i,3] = Test2[4*i+3]

avg1900 = np.average(CatArray2[0:10,2])
avg1910 = np.average(CatArray2[10:25,2])
avg1920 = np.average(CatArray2[25:41,2])
avg1930 = np.average(CatArray2[41:58,2])
avg1940 = np.average(CatArray2[58:79,2])
avg1950 = np.average(CatArray2[79:117,2])
avg1960 = np.average(CatArray2[117:145,2])
avg1970 = np.average(CatArray2[145:161,2])
avg1980 = np.average(CatArray2[161:178,2])
avg1990 = np.average(CatArray2[178:203,2])
avg2000 = np.average(CatArray2[203:np.shape(CatArray2)[0]-1,2])

x = (1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000)
y = (avg1900, avg1910, avg1920,avg1930,avg1940,avg1950,avg1960, avg1970, avg1980,avg1990,avg2000)


plt.figure(1)
plt.title("Length of Category 3 or Higher Storms by Decade")
plt.xlabel("Year")
plt.ylabel("Average Length")
plt.plot(x,y)
