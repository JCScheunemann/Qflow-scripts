import sys
import os
import random

#generate_random([5*[]],'1e-9',10)
Inputs=5*['']
npoints=10
period='1e-9'

#def generate_random(Inputs,period,npoints):
data=[(len(Inputs)*"0,")+"0"]
for i in range(0,npoints):
	tmp="+"+str(period)
	for j in [k for k in [','+str(int(round(random.random()))) for x in range(0,len(Inputs))]]:
		tmp=tmp+j
	data.append(tmp)
file = open('test.txt', 'w')
for item in data:
  file.write("%s\n" % item)
file.close()