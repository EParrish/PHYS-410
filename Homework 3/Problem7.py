import csv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

plt.figure()
Filtered_Image_Array = ndimage.imread("Problem5_Galaxy_Edit1.png")
plt.imshow(Filtered_Image_Array)
plt.show()
z_values = []
Filtered_Image_Array.tolist()
for i in Filtered_Image_Array:
	i.tolist()
	for j in i:
		z_values.append(j)
print min(z_values), max(z_values)
#print z_values
Filtered_Image_Array.flatten()
fig = plt.figure()
plt.hist(z_values, 100)
fig.suptitle("Pixel Value")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
