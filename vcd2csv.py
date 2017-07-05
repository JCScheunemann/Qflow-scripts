#get a vcd file and export input signals to csv format
#imports
import sys
import os
#globals

#code start
arquivo=open("./simulation/test.vcd","r")
vcdfile=arquivo.readlines()
arquivo.close()
i=0
Inputs=["clk","reset","out"]
simbol=len(Inputs)*['']
tmp=len(Inputs)*['']
data=[''];
flag=1
for x in vcdfile:
	if("$var" in x):
		signal=x.split(" ")[-2] if("[" not in x) else x.split(" ")[-3]
		if(signal in Inputs):
			simbol[Inputs.index(signal)]=(x.split(" ")[-3] if("[" not in x) else x.split(" ")[-4])
	elif("$dumpvars" in x):
		flag=1
	elif(flag):
		