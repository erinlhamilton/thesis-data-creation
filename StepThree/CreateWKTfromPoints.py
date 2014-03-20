#Takes the inputs of the points, lines, and polygon well-known text and shuffles the features of the polygons and lines files to create output wkt as close as possible in size (in KB)
#to the points file.
from random import shuffle
points = True
lines = True
polygons = True

inputfilepoints = "500000.txt"
inputfilelines = "150000.txt"
inputfilepolygons = "45000.txt"

pointArray = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
pointsizesArray = []
linesizesArray = []
polysizesArray = []

if (points == True):
	#load the big file
	with open(inputfilepoints) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	shuffle(content)

	#for each of our dataset sizes
	for points in pointArray:
		#create a file
		fout = open('output/points/'+str(points)+'.txt','w')
		#and dump the first N rows into that file
		output = "MULTIPOINT("
		for x in range(0,points):
			output+=content[x].rstrip()
			if (x<points-1):
				output+=","
		output +=")"
		pointsizesArray.append(len(output))
		fout.write(output)
		fout.close()

if (lines == True):
	#load the big file
	with open(inputfilelines) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	shuffle(content)

	x = 0
	#for each of our dataset sizes
	for size in pointsizesArray:
		y=0
		#create a file
		fout = open('output/lines/'+str(pointArray[x])+'.txt','w')
		#and dump the first N rows into that file
		output = "MULTILINESTRING("
		while (len(output)<size) and y<len(content):
			output+=content[y].rstrip()+","
			y+=1
		output=output[:-1]
		output+=")"
		linesizesArray.append(len(output))
		fout.write(output)
		fout.close()
		x+=1


if (polygons == True):
	#load the big file
	with open(inputfilepolygons) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	shuffle(content)

	x = 0
	#for each of our dataset sizes
	for size in pointsizesArray:
		y=0
		#create a file
		fout = open('output/polygons/'+str(pointArray[x])+'.txt','w')
		#and dump the first N rows into that file
		output = "MULTIPOLYGON("
		while (len(output)<size) and y<len(content):
			output+=content[y].rstrip()+","
			y+=1
		output=output[:-1]
		output+=")"
		polysizesArray.append(len(output))
		fout.write(output)
		fout.close()
		x+=1

fresults = open("output/sizes.txt",'w')
for x in range(0,len(pointArray)):
	fresults.write(str(pointArray[x])+","+str(pointsizesArray[x])+","+str(linesizesArray[x])+","+str(polysizesArray[x])+"\n")
fresults.close()