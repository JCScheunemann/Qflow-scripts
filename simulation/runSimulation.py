import sys
import os
#globals
topModule="mux"
j=0


#start code
#modify spice circuit file
arquivo=open('./'+topModule+".spc",'r')
spice=arquivo.readlines( )
arquivo.close()
tmp=spice
tmp.reverse()
for x in tmp:
	j+=1
	if((".subckt "+topModule) in x):
		break
tmp.reverse()
os.system("rm -y -f "+topModule+".spc")
arquivo=open('./'+topModule+".spc",'r')
for item in tmp[0:-j]:
  arquivo.write("%s\n" % item)
arquivo.close()
#start create spice power estimation file
