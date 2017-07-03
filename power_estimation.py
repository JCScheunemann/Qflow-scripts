# Power estimation with qflow
#
#
#---------------
#Imports
import sys
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
	try:
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
		#for x in:
		print "Lendo o aquivo de parametros da simulacao..."
		arquivo=open("./sim_vars.sh",'r')
		dirs=arquivo.readlines()
		arquivo.close()
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
		print "lendo o arquivo spice do projeto em: "+projDir+'/'+topModule+".spc"
		arquivo=open(projDir+'/'+topModule+".spc",'r')
		spice=arquivo.readlines( )
		arquivo.close()
	except:
		print "Nao e possivel realizar a leitura dos arquivos de configuracao"
    
	
	if(len(sys.argv)>2):
		if(sys.argv[2]=="-d"):
			Lflag=False
		elif(sys.argv[2]=="-l"):
			Dflag-False
else:
    print "Lendo o arquivo "+str((sys.argv[0]))+" Test dev mode"
    #arquivo=open("D:\Eletronica\Projects\NRISC\Assembler\Test.asm",'r')#arquivo de teste