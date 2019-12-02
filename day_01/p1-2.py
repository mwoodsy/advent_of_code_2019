def returnFuel1(mass):
    return (mass//3)-2

def returnFuel2(mass):
    fuel = 0
    while mass > 5:
        temp = (mass//3)-2
        fuel += temp
        mass = temp
    return fuel

datafile = 'data.txt'
with open(datafile) as df:
   lines = df.readlines()

part1 = [returnFuel1(int(x.strip())) for x in lines] 
part2 = [returnFuel2(int(x.strip())) for x in lines] 

print("Part 1:", str(sum(part1)))
print("Part 2:", str(sum(part2)))

