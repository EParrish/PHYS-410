# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 19:52:26 2016

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
    if Test[i] == "STORM" or Test[i] == "DEPRESSION" or Test[i] == "nan":
        Test[i] = 0

LatArray = np.zeros((len(Test)/4,4))
for i in range (0,len(Test)/4):
    LatArray[i,0] = Test[4*i]
    LatArray[i,1] = Test[4*i+1]
    LatArray[i,2] = Test[4*i+2]
    LatArray[i,3] = Test[4*i+3]
 
Test4 = []
for i in range(1,np.shape(LatArray)[0]):
    if LatArray[i,0] != LatArray[i-1,0]:
        Row = LatArray[i,:]
        Test3 = [] 
        for j in range(0,30):
            if i+j == np.shape(LatArray)[0]:
                break
            else:    
                Test3 = np.append(Test3,LatArray[i+j,3])
        Row[3] = np.amax(Test3)
        Test4 = np.append(Test4,Row)

LatArray2 = np.zeros((len(Test4)/4,4))
for i in range (0,len(Test4)/4):
    LatArray2[i,0] = Test4[4*i]
    LatArray2[i,1] = Test4[4*i+1]
    LatArray2[i,2] = Test4[4*i+2]
    LatArray2[i,3] = Test4[4*i+3]
    
Year = []
Lat = []
Cat = []

for i in range(73,np.shape(LatArray2)[0]):
    Year = np.append(Year,LatArray2[i,1])
    Lat = np.append(Lat,LatArray2[i,2])
    Cat = np.append(Cat,LatArray2[i,3])
        
Array = np.zeros((117,3))

for i in range(0,116):
    Array[i,0] = Year[i]
    Array[i,1] = Lat[i]
    Array[i,2] = Cat[i]

np.savetxt("Bubbles.csv", Array, delimiter=",")
  