import numpy as np

class OrderedVector():
    def __init__(self, leng):
        self.leng = leng
        self.last_position = -1
        self.values = np.empty(self.leng, dtype=int)

    def printValues(self):
        if self.last_position == -1:
            print(f"The vector is empty!\n")
        else:
            for i in range(self.last_position + 1):
                print(f"Index: {i} - Value: {self.values[i]}")
    def insert(self, value):
        if self.last_position == self.leng - 1:
            print("Maximum capacity reached!")
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

    def binarySearch(self, value):
        min = 0
        max = self.last_position

        while True:
            mid = int(( min + max ) / 2)
            
            if self.values[mid] == value:
                return mid
            elif min > max:
                return -1
            else:
                if self.values[mid] < value:
                    min = mid + 1
                else:
                    max = mid - 1

    def delete(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1

vector = OrderedVector(10)
vector.insert(5)
vector.insert(25)   
vector.insert(87)
vector.insert(92)
vector.insert(7)
vector.insert(15)
vector.insert(34)
vector.insert(66)
vector.insert(83)
vector.insert(91)
vector.printValues()
print("=" * 30)

print(vector.binarySearch(7))
print(vector.binarySearch(15))
print(vector.binarySearch(66))
print(vector.binarySearch(91))
print(vector.binarySearch(0))
