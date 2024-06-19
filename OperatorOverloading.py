class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


eq1 = Building(4, 4)
eq2 = Building(7, 5)
eq3 = Building(4, 4)
print(eq1.__eq__(eq2))
print(eq1.__eq__(eq3))
