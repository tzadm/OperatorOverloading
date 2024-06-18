class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        if  isinstance(other, int):
            return self.numberOfFloors == other
        else:
            return self.buildingType == self.numberOfFloors

eq1 = Building(3,7)
eq2 = Building(5,6)
print(eq1.__eq__(3))
print(eq2.__eq__(5))