def read():
	f=open("input",'r')

	#read a
	line=f.readline()
	split=line.split()	
	print(split)
	a=float(split[2])

	#read b
	line=f.readline()
	split=line.split()	
	print(split)
	b=float(split[2])
	
	#read c
	line=f.readline()
	split=line.split()	
	print(split)
	c=float(split[2])
	
	#clean up
	f.close()

	#return a, b, c	
	return(a,b,c)
