#Takes the sizes of each line in the input points textfile (500000.txt), determines its size (in KB) and randomly selects the sizes of polygonA and polygonB
#to the same sizes (based on KB)

import random
points = True
polygonA = True
polygonB = True
#set the seed of each data (points, polygonA, and polygonB) creation the same.
seedNo = 2;

inputfilepoints = "500000.txt"
inputfilepolygonA = "start_a.txt"
inputfilepolygonB = "start_b.txt"

pointArray = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
pointsizesArray = []
polyAsizesArray = []
polyBsizesArray = []

if (points == True):
	random.seed(seedNo)
	#load the big file
	with open(inputfilepoints) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	random.shuffle(content)

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

if (polygonA == True):
	random.seed(seedNo)
	#load the big file
	with open(inputfilepolygonA) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	random.shuffle(content)

	x = 0
	#for each of our dataset sizes
	for size in pointsizesArray:
		y=0
		#create a file
		fout = open('output/polyA/'+str(pointArray[x])+'.txt','w')
		#and dump the first N rows into that file
		output = "MULTIPOLYGON("
		while (len(output)<size) and y<len(content):
			output+=content[y].rstrip()+","
			y+=1
		output=output[:-1]
		output+=")"
		polyAsizesArray.append(len(output))
		fout.write(output)
		fout.close()
		x+=1


if (polygonB == True):
	random.seed(seedNo)
	#load the big file
	with open(inputfilepolygonB) as f:
		content = f.readlines()
	f.close()

	#reorder all the rows randomly
	random.shuffle(content)

	x = 0
	#for each of our dataset sizes
	for size in pointsizesArray:
		y=0
		#create a file
		fout = open('output/polyB/'+str(pointArray[x])+'.txt','w')
		#and dump the first N rows into that file
		output = "MULTIPOLYGON("
		while (len(output)<size) and y<len(content):
			output+=content[y].rstrip()+","
			y+=1
		output=output[:-1]
		output+=")"
		polyBsizesArray.append(len(output))
		fout.write(output)
		fout.close()
		x+=1

fresults = open("output/unionSizes.txt",'w')
for x in range(0,len(pointArray)):
	fresults.write(str(pointArray[x])+","+str(pointsizesArray[x])+","+str(polyAsizesArray[x])+","+str(polyBsizesArray[x])+"\n")
fresults.close()