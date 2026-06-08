class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        listOfCars = []

        for i in range(len(position)):
            tup = (position[i], speed[i])
            listOfCars.append(tup)

        listOfCars.sort(reverse=True)

        fleetStack = []

        for c in listOfCars:
            mark = (target - c[0]) / c[1]
            if not fleetStack:
                fleetStack.append(mark)
            else:
                # if mark != fleetStack[-1]:
                if mark > fleetStack[-1]:
                    fleetStack.append(mark)
        
        return len(fleetStack)