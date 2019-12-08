import time
start_time = time.time()


datafile = 'data.txt'
#datafile = 'ed.txt'
#datafile = 'example.txt'
with open(datafile) as df:
   lines = df.readlines()
data = tuple((x.strip()).split(')') for x in lines) 
solarsystem = {}
for i in data:
    planet, orbit = i
    solarsystem[planet] = { 'id': planet }
    solarsystem[orbit] = { 'id': orbit }

for i in data:
    planet, orbit = i
    satellite = solarsystem[orbit]
    parent_planet = solarsystem[planet]
    if not 'orbits' in parent_planet:
        parent_planet['orbits'] = []
    satellites = parent_planet['orbits']
    satellites.append(satellite)

def returnTotalOrbits(planet, count):
    sum = count
    if 'orbits' in planet:
        for p in planet['orbits']:
            sum += returnTotalOrbits(p, count + 1)
    return sum



part1 = returnTotalOrbits(solarsystem["COM"],0)
print("Part 1:", part1)

def returnPath(planet, dest, path):    
    path.append(planet["id"])
    if dest == path[-1]:
        return path
    elif 'orbits' in planet:
        for p in planet['orbits']:
            t = returnPath(p, dest, path.copy())
            if isinstance(t, list):
                if len(t) > 0:
                    path = t.copy()
                    break
        if dest == path[-1]:        
            return path
        else: 
            return -1
    else:
        return -1
 
santa = returnPath(solarsystem["COM"],"SAN",[])   
you = returnPath(solarsystem["COM"],"YOU",[])   

diffs = set(santa).symmetric_difference(set(you))
part2 = len(diffs)-2 # -2 to remove YOU and SAN, connecting planet missing but who cares.


print("part 2:",part2)


print("--- %s seconds ---" % (time.time() - start_time))