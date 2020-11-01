class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            return False
        
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            return False
        
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

"""
[빠른 풀이]
- addCar 부분 한번으로 줄일 수 있었는데 생각을 못함...

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.arr  =[big,medium,small]
    def addCar(self, carType: int) -> bool:
        if(self.arr[carType-1]):
            self.arr[carType-1]-=1
            return True
        return False
"""