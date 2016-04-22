# import numpy as np
# from matplotlib import pyplot as plt

# row,col,data=np.loadtxt("noisyimage.txt",unpack=True)
# rsize = int(max(row))
# csize = int(max(col))
# data=np.array(data).reshape(rsize,csize)

# def neighbors(arr,x,y,n):
#     ''' Given a 2D-array, returns an nxn array whose "center" element is arr[x,y]'''
#     arr2=np.roll(np.roll(arr,shift=-x+1,axis=0),shift=-y+1,axis=1)
#     return arr[:n,:n]

# # print(data)
# # print "\n"

# # print(neighbors(data,0,0))
# # print neighbors(data,0,0).mean(), neighbors(data,0,0).std()

# sizes = [3] # ,4,5,6,7,8]

# output_data = {}
# for i in sizes:
# 	output_data[i] = []

# # for X in xrange(data.shape[0]):
# # 	for Y in xrange(data.shape[1]):
# # 		for box_size in sizes:
# # 			this_mean = neighbors(data, X, Y, box_size).mean()
# # 			this_std = neighbors(data, X, Y, box_size).std()

# # 			output_data[box_size].append([X, Y, this_mean, this_std])

# for (X,Y), value in np.ndenumerate(data):
# 	if Y % 1000 == 0:
# 		print X
# 	this_mean = neighbors(data, X, Y, 3).mean()
# 	this_std = neighbors(data, X, Y, 3).std()

# 	output_data[3].append([X, Y, this_mean, this_std])

# print output_data

# from itertools import islice

# def window(seq, n=2):
# 	it = iter(seq)
# 	result = tuple(islice(it,n))
# 	if len(result) == n:
# 		yield result
# 	for elem in it:
# 		result = result[1:] + (elem,)
# 		yield result

# def rolling_window(seq, window_size):
# 	it = iter(seq)
# 	win = [it.next() for cnt in xrange(window_size)]
# 	yield win
# 	for e in it:
# 		win[:-1] = win[1:]
# 		win[-1] = e
# 		yield win

# if __name__ == "__main__":
# 	for w in window(xrange(6), 3):
# 		print w

# vector<int> my_array;
# int bottom_right_neighbor = tower_number - (up_diagonal * num_neighbors);
# int top_left_neighbor = tower_number + (up_diagonal * num_neighbors);
# int bottom_left_neighbor = tower_number + ((32 + 1) * num_neighbors);
# int top_right_neighbor = tower_number - ((32 + 1) * num_neighbors);

# my_array.push_back(bottom_right_neighbor); //tower_number - (up_diagonal * num_neighbors);
# my_array.push_back(top_left_neighbor);
# my_array.push_back(bottom_left_neighbor);
# my_array.push_back(top_right_neighbor);

# if ((top_left_neighbor - top_right_neighbor)%32 < window_size){    
# 	int this_tower = top_right_neighbor;
# 	while (this_tower < top_left_neighbor){
# 		my_array.push_back(this_tower + 32);
# 		this_tower += 32;
# 	}
# }
# if ((top_left_neighbor - bottom_left_neighbor)%32 < window_size){    
# 	int this_tower = top_left_neighbor;
# 	while (this_tower < bottom_left_neighbor){
# 		my_array.push_back(this_tower + 1);
# 		this_tower += 1;
# 	}

# int num_neighbors = (int) (window_size / 2);

# side_length = 32;
# updown_length = 1;
# up_diagonal = side_length - updown_length;
# down_diagonal = side_length + updown_length;
# top_left_tower = 992;
# top_right_tower = 0;
# bottom_left_tower = 1023;
# bottom_right_tower = 31;



import numpy as np
from matplotlib import pyplot as plt
import csv

# row,col,data=np.loadtxt("noisyimage.txt",unpack=True)
# rsize = int(max(row))
# csize = int(max(col))
# data=np.array(data).reshape(rsize,csize)

rsize = 1000
csize = 1000
windows = {}
window_size = 20

# for i in xrange(1, rsize):
# 	k = i - int(window_size/2)
# 	x_neighbors = []
# 	###### Grab x neighbors 
# 	while k <= i + int(window_size/2):
# 		x_neighbors.append(k)
# 		k += 1

# 	############# Loop over every y value for that x value
# 		for j in xrange(1, csize):

# 			this_window = []
# 			y_neighbors = []
		
# 			l = j - int(window_size/2)
# 			while l <= j+ int(window_size/2):
# 				y_neighbors.append(l)
# 				l += 1

# 			for m in xrange(len(x_neighbors)):
# 				for n in xrange(len(y_neighbors)):
# 					this_window.append([m,j])

# 			##### key is xpos_ypos
# 			print this_window
# 			windows["%s_%s" %(i,j)] = this_window


for i in xrange(1,rsize):
	if i < window_size:
		continue
	if i > rsize - window_size:
		continue
	for j in xrange(1,csize):
		if j < window_size:
			continue
		if j > csize - window_size:
			continue
		this_window = []
		k = i - int(window_size/2)
		x_neighbors = []
		###### Grab x neighbors 
		while k < i + int(window_size/2):
			x_neighbors.append(k)
			y_neighbors = []

			l = j - int(window_size/2)
			while l < j+ int(window_size/2):
				y_neighbors.append(l)
				l += 1

				this_window.append([k,l])
			
			windows["%s_%s" %(i,j)] = this_window
			k += 1


Image_Array = [] # [[0 for x in range(1025)] for x in range(10000)]

# noisyAnew
# noisyB
with open("noisyB.csv", "r") as csvfile:
	thisreader = csv.reader(csvfile, delimiter=',')

	# cnt = 0
	last_y_pos = 1
	this_row = []

	for row in thisreader:

		x_pos = int(row[0])
		y_pos = int(row[1])
		z_value = float(row[2])
		# print x_pos, y_pos, last_y_pos
		# print z_value

		if y_pos == last_y_pos:
			this_row.append(z_value)

		elif y_pos != last_y_pos:
			# if len(this_row) != 0:
			Image_Array.append(np.array(this_row))
			last_y_pos = y_pos
			this_row = [z_value]

		if x_pos == 1000 and y_pos == 1000:
			Image_Array.append(np.array(this_row))

# print len(Image_Array), len(Image_Array[1])

means = []
stds = []
for i in xrange(1,1000):
	if i < window_size:
		continue
	if i > rsize - window_size:
		continue
	for j in xrange(1,1000):
		if j < window_size:
			continue
		if j > csize - window_size:
			continue
		neighbors = windows["%s_%s" %(i,j)]
		neigh_z_values = []
		for neighbor in neighbors:
			neigh_x = neighbor[0]
			neigh_y = neighbor[1]
			# print neigh_x, neigh_y
			neigh_z_values.append(Image_Array[neigh_x][neigh_y])


		this_mean = sum(neigh_z_values) / len(neigh_z_values)
		means.append(this_mean)
		nparray = np.asarray(this_mean)
		this_std = nparray.std()
		stds.append(this_std)

		print window_size, i, j, this_mean, this_std


# print means
# print stds
		#.sum / len(windows["%s_%s" %(x_pos,y_pos)])