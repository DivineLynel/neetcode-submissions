class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacit = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.capacit[i]

    def set(self, i: int, n: int) -> None:
        self.capacit[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.capacit):
            self.resize()
        self.capacit[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.capacit[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        self.capacit *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.capacit)
