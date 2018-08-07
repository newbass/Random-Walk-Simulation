from random import *
import matplotlib.pyplot as plt

n = int(raw_input())
m = int(raw_input())
a = [0.0 for x in range(m+1)] 
#print(a)
for i in range(0,n):
	count1=0
	count2=0
	for j in range(1,m+1):
		num = random()
		if num >=0.5:
			count1=count1+1
		else:
			count1=count1-1

		num = random()
		if num >=0.5:
			count2=count2+1
		else:
			count2=count2-1

		if count1==count2:
			a[j]=a[j]+1

a[0] = n
#print(a)

for i in range(0,m+1):
	plt.scatter(i,a[i]/n)
plt.show()
