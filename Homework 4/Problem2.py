import numpy as np
from matplotlib import pyplot as plt


row,col,data=np.loadtxt("noisyimage.txt",unpack=True)
rsize = int(max(row))
csize = int(max(col))
data=np.array(data).reshape(rsize,csize)
plt.imshow(data, interpolation='None',cmap=plt.cm.Greys_r)
plt.show()