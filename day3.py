import sys, math, copy

# Read from the file
inFile = sys.argv[1]

f = open(inFile,'r') 
contents = f.read()
directions1 = []
directions2 = []

xLoc = 0
yLoc = 0
line1 = []
overlap = []
with open(inFile) as fp:
    line = fp.readline()
    cnt = 1
    for location in line.split(','):
        i = 0
        directions1.append(location)
        if "\n" in location:
            break
        if location[0] == "U":
            while i < int(location[1:]):
                yLoc = yLoc+1
                line1.append((xLoc,yLoc))
                i+=1
        if location[0] == "D":
            while i < int(location[1:]):
                yLoc = yLoc-1
                line1.append((xLoc,yLoc))
                i+=1
        if location[0] == "R":
            while i < int(location[1:]):
                xLoc = xLoc+1
                line1.append((xLoc,yLoc))
                i+=1
        if location[0] == "L":
            while i < int(location[1:]):
                xLoc = xLoc-1
                line1.append((xLoc,yLoc))
                i+=1
    xLoc = 0
    yLoc = 0
    line = fp.readline()
    line2 = []

    for location in line.split(','):
        i = 0
        directions2.append(location)
        if "\n" in location:
            break
        if location[0] == "U":
            while i < int(location[1:]):
                yLoc+=1
                line2.append((xLoc,yLoc))
                i+=1
        if location[0] == "D":
            while i < int(location[1:]):
                yLoc-=1
                line2.append((xLoc,yLoc))
                i+=1
        if location[0] == "R":
            while i < int(location[1:]):
                xLoc+=1
                line2.append((xLoc,yLoc))
                i+=1
        if location[0] == "L":
            while i < int(location[1:]):
                xLoc -=1
                line2.append((xLoc,yLoc))
                i+=1

overlap = list(set(line1) & set(line2))

minDis = float('Inf')
for combo in overlap:

    if (abs(combo[0]) + abs(combo[1]) < minDis):
        minDis = abs(combo[0]) + abs(combo[1])




# Section 2
steps = 0
dis2Intersec1 = {}
dis2Intersec2 = {}
xLoc = 0
yLoc = 0
for location in directions1:
    i = 0

    if "\n" in location:
        break
    if location[0] == "U":
        while i < int(location[1:]):
            yLoc = yLoc+1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec1:
                    dis2Intersec1[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "D":
        while i < int(location[1:]):
            yLoc = yLoc-1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec1:
                    dis2Intersec1[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "R":
        while i < int(location[1:]):
            xLoc = xLoc+1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec1:
                    dis2Intersec1[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "L":
        while i < int(location[1:]):
            xLoc = xLoc-1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec1:
                    dis2Intersec1[(xLoc,yLoc)] = steps
            i+=1

steps = 0
xLoc = 0
yLoc = 0
for location in directions2:
    i = 0
    if "\n" in location:
        break
    if location[0] == "U":
        while i < int(location[1:]):
            yLoc = yLoc+1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec2:
                    dis2Intersec2[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "D":
        while i < int(location[1:]):
            yLoc = yLoc-1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec2:
                    dis2Intersec2[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "R":
        while i < int(location[1:]):
            xLoc = xLoc+1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec2:
                    dis2Intersec2[(xLoc,yLoc)] = steps
            i+=1
    if location[0] == "L":
        while i < int(location[1:]):
            xLoc = xLoc-1
            steps +=1
            if(xLoc,yLoc) in overlap:
                if (xLoc,yLoc) not in dis2Intersec2:
                    dis2Intersec2[(xLoc,yLoc)] = steps
            i+=1

minComb = float('Inf')

    
for tup in overlap:
    if (dis2Intersec1[tup] +dis2Intersec2[tup] < minComb):
        minComb = dis2Intersec1[tup] + dis2Intersec2[tup]

print(minComb)