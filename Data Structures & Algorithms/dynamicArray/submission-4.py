class DynamicArray:
    
    def __init__(self, capacity: int):
        self.pointer = 0
        self.capacity = capacity
        self.filled = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if i <= self.pointer:
            return self.array[i]
        
        return 0

    def set(self, i: int, n: int) -> None:
        if i < self.capacity and i <= self.pointer:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.pointer == self.capacity:
            self.resize()

        self.array[self.pointer] = n
        self.pointer += 1
        self.filled += 1

    def popback(self) -> int:
        num = self.array[self.pointer - 1]
        self.array[self.pointer - 1] = 0
        self.pointer -= 1
        self.filled -= 1
        return num

    def resize(self) -> None:
        self.array.extend([0] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.filled
    
    def getCapacity(self) -> int:
        return self.capacity