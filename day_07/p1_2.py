import time
start_time = time.time()

data = '3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99'
#data = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
#data = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
opcodes = [int(n) for n in data.split(',')]


def getModes(op):
    t = str(op)
    t = t.zfill(5)
    return [int(t[3:]),int(t[2]),int(t[1]),int(t[0])]

def getErrorCode(tOpcodes, dCode, indexList):
    index = indexList[0]
    while True:
        oc = getModes(tOpcodes[index])
        if oc[0]==99:
            return str(max(tOpcodes))
        else:
            in1 = tOpcodes[index+1] if oc[1]==0 else index+1
            if oc[0] == 1:
                in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                in3 = tOpcodes[index+3] if oc[3]==0 else index+3
                tOpcodes[in3] = tOpcodes[in1]+tOpcodes[in2]
                index = index+4
            elif oc[0] == 2:
                in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                in3 = tOpcodes[index+3] if oc[3]==0 else index+3
                tOpcodes[in3] = tOpcodes[in1]*tOpcodes[in2]
                index = index+4
            elif oc[0] == 3:
                tOpcodes[in1] = dCode.pop()
                index = index+2
            elif oc[0] == 4:
                #if tOpcodes[in1] != 0:
                indexList[0] = index+2
                return tOpcodes[in1]
                #index = index+2
            elif oc[0] == 5:
                if tOpcodes[in1] != 0:
                    in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                    index = tOpcodes[in2]
                else:
                    index = index + 3
            elif oc[0] == 6:
                if tOpcodes[in1] == 0:
                    in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                    index = tOpcodes[in2]
                else:
                    index = index + 3
            elif oc[0] == 7:
                in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                in3 = tOpcodes[index+3] if oc[3]==0 else index+3
                tOpcodes[in3] = 1 if tOpcodes[in1] < tOpcodes[in2] else 0
                index = index + 4
            elif oc[0] == 8:
                in2 = tOpcodes[index+2] if oc[2]==0 else index+2
                in3 = tOpcodes[index+3] if oc[3]==0 else index+3
                tOpcodes[in3] = 1 if tOpcodes[in1] == tOpcodes[in2] else 0
                index = index+4
            else:
                print("something is wrong",oc, index)
                return -1
            

import itertools
s='12340'
t=list(itertools.permutations(s,len(s)))
tests=[]
for i in range(0,len(t)):
    tests.append(''.join(t[i]))
outputs = []

for inst in tests:
    previous = 0
    temp = []
    for x in inst:
        temp.append(getErrorCode(opcodes.copy(),[previous,int(x)],[0]))
        previous = int(temp[-1])
    outputs.append(temp[-1])

part1 = max(outputs)
print("Part 1:", part1)



r='98765'
q=list(itertools.permutations(r,len(r)))
tests=[]
for i in range(0,len(q)):
    tests.append(''.join(q[i]))
outputs = [1]
for inst in tests:
    ampA = opcodes.copy()
    ampB = opcodes.copy()
    ampC = opcodes.copy()
    ampD = opcodes.copy()
    ampE = opcodes.copy()

    ind1 = [0]
    ind2 = [0]
    ind3 = [0]
    ind4 = [0]
    ind5 = [0]

    outA = getErrorCode(ampA,  [0,   int(inst[0])],   ind1)
    outB = getErrorCode(ampB,  [outA,int(inst[1])],   ind2)
    outC = getErrorCode(ampC,  [outB,int(inst[2])],   ind3)
    outD = getErrorCode(ampD,  [outC,int(inst[3])],   ind4)
    outE = getErrorCode(ampE,  [outD,int(inst[4])],   ind5)
    while isinstance(outE, int):
        outA = getErrorCode(ampA,[outE],ind1)
        outB = getErrorCode(ampB,[outA],ind2)
        outC = getErrorCode(ampC,[outB],ind3)
        outD = getErrorCode(ampD,[outC],ind4)
        outE = getErrorCode(ampE,[outD],ind5)
    outputs.append(int(outE))
best = outputs.index(max(outputs))
part2 = max(outputs)
print("Part 2:", part2)
print("--- %s seconds ---" % (time.time() - start_time))
        