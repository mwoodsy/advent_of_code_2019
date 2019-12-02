datafile = 'data.txt'
with open(datafile) as df:
   data = df.readline()

opcodes = [int(n) for n in data.split(',')]



def getFinalZeroPosition(tOpcodes, n, v):
    index = 0
    tOpcodes[1] = n 
    tOpcodes[2] = v

    while True:
        if tOpcodes[index]==99:
            return tOpcodes[0]
        else:
            oc = tOpcodes[index]
            in1 = tOpcodes[index+1]
            in2 = tOpcodes[index+2]
            in3 = tOpcodes[index+3]

            if oc == 1:
                tOpcodes[in3] = tOpcodes[in1]+tOpcodes[in2]

            elif oc == 2:
                tOpcodes[in3] = tOpcodes[in1]*tOpcodes[in2]

            else:
                print("something is wrong",oc, index)
                return -1
            index = index+4

print("Part 1:",getFinalZeroPosition(opcodes.copy(),12,2))

for n in range(100):
    for v in range(100):
        if getFinalZeroPosition(opcodes.copy(),n,v) == 19690720:
            print("Part 2:", (100*n)+v)
            quit()
