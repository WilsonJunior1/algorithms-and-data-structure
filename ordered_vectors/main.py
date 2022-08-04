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
                print(f'Index: {i} - Value: {self.values[i]}')

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
    
    def search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1
    
    def delete(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1

vector = OrderedVector(10)
vector.printValues()
vector.insert(4)
vector.printValues()
vector.insert(5)
vector.printValues()
vector.insert(1)
vector.printValues()
vector.insert(2)
vector.printValues()
print(vector.search(4))
print(vector.search(1))
vector.delete(5)
vector.printValues()
