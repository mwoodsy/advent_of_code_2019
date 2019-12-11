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


#[13,17]
part1 = max(lineofsight)
print("Part 1:", part1)

baseLocation = points[lineofsight.index(max(lineofsight))]

def getDistance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

tests = []
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
                    #tests.append(abs(rad))
                    deg = math.degrees(rad)
                    if deg < 0:
                        deg = 360 + deg
                    deg = (deg + 90)%360
                    tests.append(deg)
                    distAngle.append([tempX, tempY, getDistance(x,y,tempX,tempY), deg])
            tempX += 1
        tempY += 1
    return(distAngle)

# N:0 E:90.0 S:180 W:270
targets = getDistancesAngles(baseLocation[0],baseLocation[1], sky)
#targets = getDistancesAngles(11,13, sky)
targets.sort(key=lambda x: [x[3], x[2]])

destroyed = 0
part2 = 0
while len(targets) != 0:
    lastAngle = -1
    remove = []
    for target in targets:
        if target[3] > lastAngle:
            lastAngle = target[3]
            remove.append(target)
            destroyed += 1
            if destroyed == 200:
                part2 = target[0]*100+target[1]
    for r in remove:
        targets.remove(r)

print("Part 2:",part2)        


print("--- %s seconds ---" % (time.time() - start_time))