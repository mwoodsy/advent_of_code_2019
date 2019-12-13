import time
start_time = time.time()

import sys
sys.path.insert(0, '../shared_modules')
import opcode

data = '3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99'
#data = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
#data = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
opcodes = [int(n) for n in data.split(',')]


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
        temp.append(opcode.getErrorCode(opcodes.copy(),[previous,int(x)],[0],[0]))
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

    outA = opcode.getErrorCode(ampA,  [0,   int(inst[0])],   ind1,[0])
    outB = opcode.getErrorCode(ampB,  [outA,int(inst[1])],   ind2,[0])
    outC = opcode.getErrorCode(ampC,  [outB,int(inst[2])],   ind3,[0])
    outD = opcode.getErrorCode(ampD,  [outC,int(inst[3])],   ind4,[0])
    outE = opcode.getErrorCode(ampE,  [outD,int(inst[4])],   ind5,[0])
    while isinstance(outE, int):
        outA = opcode.getErrorCode(ampA,[outE],ind1,[0])
        outB = opcode.getErrorCode(ampB,[outA],ind2,[0])
        outC = opcode.getErrorCode(ampC,[outB],ind3,[0])
        outD = opcode.getErrorCode(ampD,[outC],ind4,[0])
        outE = opcode.getErrorCode(ampE,[outD],ind5,[0])
    outputs.append(max(outE))
best = outputs.index(max(outputs))
part2 = max(outputs)
print("Part 2:", part2)
print("--- %s seconds ---" % (time.time() - start_time))
        