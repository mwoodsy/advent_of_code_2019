import time
start_time = time.time()

import math

datafile = 'data.txt'
with open(datafile) as df:
   lines = df.readlines()

sky = [x.strip() for x in lines]

def getCounts(x, y, board):
    tempY=0
    tempX=0
    count = set()
    for r in board:
        tempX = 0
        for c in r:
            if c == '#':
                if not(tempX == x and tempY == y):
                    rad = math.atan2(tempY-y, tempX-x)
                    deg = math.degrees(rad)
                    count.add(deg)
            tempX += 1
        tempY += 1
    return(len(count))


lineofsight = []
points = [] 
y = 0
x = 0
for row in sky:
    x = 0
    for p in row:
        if p == '#':
            lineofsight.append(getCounts(x,y,sky))
        else:
            lineofsight.append(0)
        points.append([x,y])
        x += 1
    y += 1


part1 = max(lineofsight)
print("Part 1:", part1)

baseLocation = points[lineofsight.index(max(lineofsight))]

def getDistance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def getDistancesAngles(x, y, board):
    tempY=0
    tempX=0
    distAngle = []
    for r in board:
        tempX = 0
        for c in r:
            if c == '#':
                if not(tempX == x and tempY == y):
                    rad = math.atan2(tempY-y, tempX-x)
                    deg = math.degrees(rad)
                    if deg < 0:
                        deg = 360 + deg
                    deg = (deg + 90)%360
                    distAngle.append([tempX, tempY, getDistance(x,y,tempX,tempY), deg])
            tempX += 1
        tempY += 1
    
    # N:0 E:90.0 S:180 W:270
    distAngle.sort(key=lambda x: [x[3], x[2]])
    return distAngle

def getXTargetDestroyed(base, sky, count):
    targets = getDistancesAngles(base[0],base[1], sky)
    destroyed = 0
    while len(targets) != 0:
        lastAngle = -1
        remove = []
        for target in targets:
            if target[3] > lastAngle:
                lastAngle = target[3]
                remove.append(target)
                destroyed += 1
                if destroyed == 200:
                    return target[0]*100+target[1]
        for r in remove:
            targets.remove(r)
    
part2 = getXTargetDestroyed(baseLocation, sky.copy(), 200)
print("Part 2:",part2)        


print("--- %s seconds ---" % (time.time() - start_time))