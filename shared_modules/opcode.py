def getModes(op):
    t = str(op)
    t = t.zfill(5)
    o = [int(t[3:]),int(t[2]),int(t[1]),int(t[0])]
    return o

def getIndexByMode(mode, inputValue, index, rIndex):
    if mode == 0:
        return inputValue
    elif mode == 1:
        return index
    elif mode == 2:
        return rIndex + inputValue
    else:
        print("Bad Mode value")
        return 'Error'

def increaseArray(atleast, tOpcodes):
    while atleast > len(tOpcodes)-1:
        tOpcodes.append(0)

def getErrorCode(tOpcodes, dCode, indexList):
    index = indexList[0]
    relIndex = 0
    while True:
        oc = getModes(tOpcodes[index])
        if oc[0]==99:
            return tOpcodes
        else:
            in1 = getIndexByMode(oc[1], tOpcodes[index+1], index+1, relIndex)
            increaseArray(in1, tOpcodes)
            
            try:
                in2 = getIndexByMode(oc[2], tOpcodes[index+2], index+2, relIndex)
                increaseArray(in2, tOpcodes)
            except IndexError:
                in2 = 0
            
            try:
                in3 = getIndexByMode(oc[3], tOpcodes[index+3], index+3, relIndex)
                increaseArray(in3, tOpcodes)
            except IndexError:
                in3 = 0
            if oc[0] == 1:
                tOpcodes[in3] = tOpcodes[in1]+tOpcodes[in2]
                index = index+4
            elif oc[0] == 2:
                tOpcodes[in3] = tOpcodes[in1]*tOpcodes[in2]
                index = index+4
            elif oc[0] == 3:
                tOpcodes[in1] = dCode.pop()
                index = index+2
            elif oc[0] == 4:
                indexList[0] = index+2
                return tOpcodes[in1]
            elif oc[0] == 5:
                if tOpcodes[in1] != 0:
                    index = tOpcodes[in2]
                else:
                    index = index + 3
            elif oc[0] == 6:
                if tOpcodes[in1] == 0:
                    index = tOpcodes[in2]
                else:
                    index = index + 3
            elif oc[0] == 7:
                tOpcodes[in3] = 1 if tOpcodes[in1] < tOpcodes[in2] else 0
                index = index + 4
            elif oc[0] == 8:
                tOpcodes[in3] = 1 if tOpcodes[in1] == tOpcodes[in2] else 0
                index = index+4
            elif oc[0] == 9:
                relIndex = relIndex + tOpcodes[in1]
                index = index+2
            else:
                print("something is wrong",oc, index)
                return -1