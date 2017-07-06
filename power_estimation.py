# Power estimation with qflow
#
#
#---------------
#Imports
import sys
import os
#globals
Dflag=True
Lflag=True
projDir=""
topModule=""
vestaOpt=""
var=""
In=[]
SizeIn=[]
Out=[]
SizeOut=[]
InOut=[]
SizeInOut=[]
#begin
print sys.argv
if(len(sys.argv)>1):
	topModule=sys.argv[1]
	print "Procurando os arquivos de configuracao do projeto ..."
	#=======================Leitura dos arquivos de configuracao======================
	try:
		#==========================read qflow vars========================
		print "Lendo a lista de diretorios..."
		arquivo=open("./qflow_vars.sh",'r')
		dirs=arquivo.readlines()
		arquivo.close()
		print "Procurando o diretorio de sintese"
		for x in dirs:
			if("synthdir" in x):
				projDir=(x.split('='))[1]
				projDir=projDir[0:len(projDir)-1]
				print "Encontrado o diretorio:'"+projDir+"'"
				break
		#==========================read cfg file===========================
		print "Lendo os arquivos de configuracao do projeto..."
		arquivo=open("./project_vars.sh",'r')
		projcfg=arquivo.readlines()
		arquivo.close()
		projcfg.reverse()
		for x in projcfg:
			if("vesta_options" in x):
				vestaOpt=(x.split('='))[1].split('"')[1]
				print "Parametros de time:'"+vestaOpt+"'"
				break
		#==========================read sim param=========================
		print "Lendo o aquivo de parametros da simulacao..."
		arquivo=open("./sim_vars.sh",'r')
		dirs=arquivo.readlines()
		arquivo.close()
		#==========================read RTL===============================
		print "lendo o arquivo RTL do projeto em: "+projDir+'/'+topModule+".rtl.v"
		arquivo=open(projDir+'/'+topModule+".rtl.v",'r')
		rtl=arquivo.readlines()
		arquivo.close()
		print "Mapeando entradas/saidas do module..."
		for x in rtl:
				if("input" in x):
					size=1
					if(":" in x):	#verifica se eh um vetor
						tmp=[int(g) for g in x[7:].split(']')[0].split(':')]	#pega o tamanho dos campos [n:m]
						size=tmp[0]+1 if(tmp[0]>tmp[1]) else tmp[1]+1 			#calcula o tamanho do vetor n ou m +1
					if(',' not in x):
						In.append(x[6:].split(']')[1][1:-2] if(']' in x) else x[6:-2] )
						SizeIn.append(size)
					else:
						for k in (x[6:].split(']')[1].split(',') if(']' in x) else x[5:].split(',')):
							In.append(k[1:-2] if(';' in k) else k[1:])
							SizeIn.append(size)
				elif("output" in x):
					size=1
					if(":" in x):	#verifica se eh um vetor
						tmp=[int(g) for g in x[8:].split(']')[0].split(':')]	#pega o tamanho dos campos [n:m]
						size=tmp[0]+1 if(tmp[0]>tmp[1]) else tmp[1]+1 			#calcula o tamanho do vetor n ou m +1
					if(',' not in x):
						Out.append(x[6:].split(']')[1][1:-2] if(']' in x) else x[7:-2] )
						SizeOut.append(size)
					else:
						for k in (x[6:].split(']')[1].split(',') if(']' in x) else x[5:].split(',')):
							Out.append(k[1:-2] if(';' in k) else k[1:])
							SizeOut.append(size)
				elif("inout" in x):
					size=1
					if(":" in x):	#verifica se eh um vetor
						tmp=[int(g) for g in x[7:].split(']')[0].split(':')]	#pega o tamanho dos campos [n:m]
						size=tmp[0]+1 if(tmp[0]>tmp[1]) else tmp[1]+1 			#calcula o tamanho do vetor n ou m +1
					if(',' not in x):
						InOut.append(x[6:].split(']')[1][1:-2] if(']' in x) else x[6:-2] )
						SizeInOut.append(size)
					else:
						for k in (x[6:].split(']')[1].split(',') if(']' in x) else x[5:].split(',')):
							InOut.append(k[1:-2] if(';' in k) else k[1:])
							SizeInOut.append(size)
		print "Mapeamento de entradas/saidas completo..."
		print "Encontrado "+str(len(In))+(" entradas:" if(len(In)>1) else " entrada:")
		print "\tNome\tsize"
		for i in range(0, len(In)):
			print "\t"+In[i]+"\t"+str(SizeIn[i])
		print "Encontrado "+str(len(Out))+(" saidas:" if(len(Out)>1) else " saida:")
		print "\tNome\tsize"
		for i in range(0, len(Out)):
			print "\t"+Out[i]+"\t"+str(SizeOut[i])
		if(len(InOut)!=[]):
			print "Encontrado "+str(len(InOut))+(" inout's:" if(len(InOut)>1) else " inout:")
			print "\tNome\tsize"
			for i in range(0, len(InOut)):
				print "\t"+InOut[i]+"\t"+str(SizeInOut[i])
		#==========================read spice===============================
		print "lendo o arquivo spice do projeto em: "+projDir+'/'+topModule+".spc"
		arquivo=open(projDir+'/'+topModule+".spc",'r')
		spice=arquivo.readlines( )
		arquivo.close()
	except:
		print "Nao e possivel realizar a leitura dos arquivos de configuracao"
	#ensina a medir a potencia no spice
    #https://sourceforge.net/p/ngspice/discussion/133842/thread/c59954ff/
	
	if(len(sys.argv)>2):
		if(sys.argv[2]=="-d"):
			Lflag=False
		elif(sys.argv[2]=="-l"):
			Dflag-False
	#=======================Inicio da estimativa de potencia======================
	try:
		os.system("qflow sta "+topModule+">./report/time.txt") 
		arquivo=open("./report/time.txt,'r')
		tmp=arquivo.readlines()
		arquivo.close()
		for x in tmp:
			if("to output pin out delay" in x):
				time=x.split(" ps")[0].split(" ")[-1] #get minimum period time
				break
		#=======================inicio da criação do arquivo spice da simulacao======
	except:
		print "\tErro 42, reservado para quando eu tiver saco de resolver ele."
else:
    print "Lendo o arquivo "+str((sys.argv[0]))+" Test dev mode"
    #arquivo=open("D:\Eletronica\Projects\NRISC\Assembler\Test.asm",'r')#arquivo de teste