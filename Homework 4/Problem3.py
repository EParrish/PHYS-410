import numpy as np
from matplotlib import pyplot as plt



row,col,data=np.loadtxt("noisyimage.txt",unpack=True)
rsize = int(max(row))
csize = int(max(col))
data=np.array(data).reshape(rsize,csize)

def neighbors(arr,x,y,n):
    ''' Given a 2D-array, returns an nxn array whose "center" element is arr[x,y]'''
    arr=np.roll(np.roll(arr,shift=-x+1,axis=0),shift=-y+1,axis=1)
    return arr[:n,:n]

# print(data)
# print "\n"

# print(neighbors(data,0,0))
# print neighbors(data,0,0).mean(), neighbors(data,0,0).std()

sizes = [3] # ,4,5,6,7,8]

output_data = {}
for i in sizes:
	output_data[i] = []

for X in xrange(data.shape[0]):
	for Y in xrange(data.shape[1]):
		for box_size in sizes:
			this_mean = neighbors(data, X, Y, box_size).mean()
			this_std = neighbors(data, X, Y, box_size).std()

			output_data[box_size].append([X, Y, this_mean, this_std])

print output_data