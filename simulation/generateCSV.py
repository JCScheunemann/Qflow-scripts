import sys
import os
import random

#generate_random([5*[]],'1e-9',10)
nInputs=7#sum([1,1,1,2,8,2])
npoints=1000
period='150e-12'

#def generate_random(Inputs,period,npoints):
data=[(nInputs*"0,")+"0"]
clk=0
for i in range(0,npoints):
	tmp="+"+str(period)
	for j in [k for k in [','+str(int(round(random.random()))) for x in range(0,nInputs-1)]]:
		tmp=tmp+j
	data.append(tmp+',0')
	data.append(tmp+',1')
file = open('test.txt', 'w')
for item in data:
  file.write("%s\n" % item)
file.close()