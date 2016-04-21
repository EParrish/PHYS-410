import numpy as np
from matplotlib import pyplot as plt



row,col,data=np.loadtxt("noisyimage.txt",unpack=True)
rsize = int(max(row))
csize = int(max(col))
data=np.array(data).reshape(rsize,csize)

print rsize, csize

def DefineWindows(Towers, window_size):
	"""
	"""
	dphi_window = (window_size*0.2)/2
	deta_window = (window_size*0.2)/2
	Windows = {}
	for tower1 in Towers.keys():
		thisWindow = []
		for tower2 in Towers.keys():
			if tower1 == tower2: 
				continue
			deltaEta = abs(Towers[tower1].Eta() - Towers[tower2].Eta())
			deltaPhi = abs(Towers[tower1].Phi() - Towers[tower2].Phi())
			if deltaPhi > pi:
				deltaPhi = 2*pi - deltaPhi
			if deltaEta <= deta_window:
				if deltaPhi <= dphi_window:
					thisWindow.append(Towers[tower2].Tower())

		Windows[tower1] = thisWindow

	return Windows