class Moon:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

        self.vX = 0
        self.vY = 0
        self.vZ = 0

        # temp values
        self.__tX = 0
        self.__tY = 0
        self.__tZ = 0


    def __calculateChange(self, mine, theirs):
        if (mine > theirs):
            return -1
        elif (mine < theirs):
            return 1
        else:
            return 0

    def getVelocityChanges(self, otherMoons):
        self.__tX = 0
        self.__tY = 0
        self.__tZ = 0

        for m in otherMoons:
            self.__tX += self.__calculateChange(self.x, m.x)
            self.__tY += self.__calculateChange(self.y, m.y)
            self.__tZ += self.__calculateChange(self.z, m.z)
        
        return [self.__tX, self.__tY, self.__tZ]
            
    def move(self):
        self.vX += self.__tX
        self.vY += self.__tY
        self.vZ += self.__tZ
        self.x += self.vX
        self.y += self.vY
        self.z += self.vZ


    def getPotSum(self):
        return (abs(self.x)+abs(self.y)+abs(self.z))
    
    def getKinSum(self):
        return (abs(self.vX)+abs(self.vY)+abs(self.vZ))
    
    def getPotKinProduct(self):
        return self.getPotSum()*self.getKinSum()

    def printMoon(self):
        print("pos=<x=%s, y=%s, z=%s>, vel=<x= %s, y=%s, z=%s>" % (self.x, self.y, self.z, self.vX, self.vY, self.vZ))

    def getCoordsVelocity(self):
        return [self.x, self.y, self.z, self.vX, self.vY, self.vZ]
    def getCoords(self):
        return [self.x, self.y, self.z]
    def getVelocity(self):
        return [self.vX, self.vY, self.vZ]

    