# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 07:47:34 2016

@author: brown_000
"""

#First Import the Array
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
TheArray = pd.read_csv('C://Users/brown_000/Desktop/master1.csv')
TheArray.as_matrix()
TheArray = np.array(TheArray)
#Now Do the actual problem
Titles = [['StormID','Year','Final Pressure','Spin Up Time','Category']]
Test = []
for i in range(0,np.shape(TheArray)[0]-50):
    if TheArray[i,4] >= 1000:
            a=TheArray[i,6]
            for j in range(1,50):
               if TheArray[i+j,4] <= 970  and TheArray[i+j,4] > 0 and TheArray[i,0] == TheArray[i+j,0]:
                        if TheArray[i+j,8] == "E-1" or TheArray[i+j,8] == "E-2" or TheArray[i+j,8] == "E-3" or TheArray[i+j,8] == "E-4" or TheArray[i+j,8] == "E-5":
                            StormID = TheArray[i,0]
                            Year = TheArray[i,5] 
                            Final_Pressure =TheArray[i+j,4] 
                            SpinUp = TheArray[i+j,6]-TheArray[i,6]
                            Category = TheArray[i+j,8]
                            Row = [StormID,Year,Final_Pressure,SpinUp,Category]
                            #print Row
                            Test = np.append(Test,Row)
                            #print Test
                            break
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
    if Test[i] == "STORM":
        Test[i] = 0

        
SpinArray = np.zeros((len(Test)/5,5))
for i in range (0,len(Test)/5):
    SpinArray[i,0] = Test[5*i]
    SpinArray[i,1] = Test[5*i+1]
    SpinArray[i,2] = Test[5*i+2]
    SpinArray[i,3] = Test[5*i+3]
    SpinArray[i,4] = Test[5*i+4]
SpinArray = np.concatenate((Titles,SpinArray),axis = 0)

Test2 = []
for i in range(2,np.shape(SpinArray)[0]):
    if SpinArray[i-1,0] != SpinArray[i-2,0]:
        Row = SpinArray[i,:]
        Test2 = np.append(Test2,Row)
        
SpinArray2 = np.zeros((len(Test2)/5,5))
for i in range (0,len(Test2)/5):
    SpinArray2[i,0] = Test2[5*i]
    SpinArray2[i,1] = Test2[5*i+1]
    SpinArray2[i,2] = Test2[5*i+2]
    SpinArray2[i,3] = Test2[5*i+3]
    SpinArray2[i,4] = Test2[5*i+4]
SpinArray2 = np.concatenate((Titles,SpinArray2),axis = 0)

Test3 = []
for i in range(1,38):
            x = float(SpinArray[i,3])
            Test3 = np.append(Test3,x)

plt.figure(1)
plt.title("Spin Up Times of Hurricanes 1950 - 1970")
plt.xlabel("Spin Up Time (Hours)")
plt.ylabel("Occurences")
plt.hist(Test3,bins=10)

Test4 = []
for i in range(78,np.shape(SpinArray2)[0]-1):
            x = float(SpinArray[i,3])
            Test4 = np.append(Test4,x)
plt.figure(2)
plt.title("Spin Up Times of Hurricanes 1990 - 2010")
plt.xlabel("Spin Up Time (Hours)")
plt.ylabel("Occurences")
plt.hist(Test4,bins=10)

Test5 = []
for i in range(1,np.shape(SpinArray2)[0]-1):
            x = float(SpinArray[i,3])
            Test5 = np.append(Test5,x)
plt.figure(3)
plt.title("Spin Up Times of Hurricanes")
plt.xlabel("Spin Up Time (Hours)")
plt.ylabel("Occurences")
plt.hist(Test5)
