import time
start_time = time.time()

from moon import Moon

def currentPositions(m):
    print("After %s steps:"% m)
    io.printMoon()
    europa.printMoon()
    ganymede.printMoon()
    callisto.printMoon()

io = Moon(13,-13,-2)
europa = Moon(16,2,-15)
ganymede = Moon(7,-18,-12)
callisto = Moon(-3,-8,-8)

move = 0

for x in range(1000):
    io.getVelocityChanges([europa,ganymede,callisto])
    europa.getVelocityChanges([io,ganymede,callisto])
    ganymede.getVelocityChanges([io,europa,callisto])
    callisto.getVelocityChanges([io,europa,ganymede])

    io.move()
    europa.move()
    ganymede.move()
    callisto.move()

    move += 1

part1 = io.getPotKinProduct() + europa.getPotKinProduct() + ganymede.getPotKinProduct()+callisto.getPotKinProduct()
print("Part 1:", part1)


io = Moon(13,-13,-2)
europa = Moon(16,2,-15)
ganymede = Moon(7,-18,-12)
callisto = Moon(-3,-8,-8)

move = 0
part2 = 0
import copy

ioOriginal = copy.deepcopy(io)
europaOriginal = copy.deepcopy(europa)
ganymedeOriginal = copy.deepcopy(ganymede)
callistoOriginal = copy.deepcopy(callisto)


xmoves = 0
ymoves = 0
zmoves = 0
while True:
    io.getVelocityChanges([europa,ganymede,callisto])
    europa.getVelocityChanges([io,ganymede,callisto])
    ganymede.getVelocityChanges([io,europa,callisto])
    callisto.getVelocityChanges([io,europa,ganymede])

    io.move()
    europa.move()
    ganymede.move()
    callisto.move()

    move += 1


    if xmoves == 0:
        if io.vX==ioOriginal.vX and io.x == ioOriginal.x:
            if europa.vX==europaOriginal.vX and europa.x==europaOriginal.x:
                if ganymede.vX==ganymedeOriginal.vX and ganymede.x==ganymede.x:
                    if callisto.vX==callistoOriginal.vX and callisto.x==callistoOriginal.x:              
                        xmoves = move
                    
    if ymoves == 0:
        if io.vY==ioOriginal.vY and io.y == ioOriginal.y:
            if europa.vY==europaOriginal.vY and europa.y==europaOriginal.y:
                if ganymede.vY==ganymedeOriginal.vY and ganymede.y==ganymede.y:
                    if callisto.vY==callistoOriginal.vY and callisto.y==callistoOriginal.y:             
                        ymoves = move

    if zmoves == 0:            
        if io.vZ==ioOriginal.vZ and io.z == ioOriginal.z:
            if europa.vZ==europaOriginal.vZ and europa.z==europaOriginal.z:
                if ganymede.vZ==ganymedeOriginal.vZ and ganymede.z==ganymede.z:
                    if callisto.vZ==callistoOriginal.vZ and callisto.z==callistoOriginal.z:         
                            zmoves = move
    
    if xmoves > 0:
        if ymoves > 0:
            if zmoves > 0:
                break
     


import numpy as np
part2 = np.lcm.reduce([xmoves, ymoves, zmoves])
print("Part 2:", part2)

print("--- %s seconds ---" % (time.time() - start_time))