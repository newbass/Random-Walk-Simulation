import math
import matplotlib.pyplot as plt
from random import *

men = int(raw_input())
steps = int(raw_input())
a = [0 for i in range(0,max(men,steps)+1)]

for i in range(0,men):
	xtot = 0
	ytot = 0
	for j in range(1,steps+1):
		x = random()
		sign = random()
		if sign >= 0.5:
			signx = 1
		else:
			signx = -1
		
		sign = random()
		if sign >= 0.5:
			signy = 1
		else:
			signy = -1
		y = math.sqrt(1 - (x*x))
		x = x*signx
		y = y*signy
		xtot += x
		ytot += y
	a[int(math.ceil(math.sqrt((xtot*xtot) + (ytot*ytot))))] += 1

for i in range(0,steps+1):
	plt.scatter(i,a[i])

plt.show()

