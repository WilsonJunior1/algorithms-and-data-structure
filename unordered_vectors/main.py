import numpy as np

class UnorderedVector():
    def __init__(self, leng):
        self.leng = leng
        self.last_position = -1
        self.values =np.empty(self.leng, dtype=int)

    def printValues(self):
        if self.last_position == -1:
            print(f"The vector is empty!\n")
        else:
            for i in range(self.last_position + 1):
                print(f'Index: {i} - Value: {self.values[i]}')

    def insert(self, value):
        if self.last_position == self.leng - 1:
            print("Maximum capacity reached!\n")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    def search(self, value):
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i
        return -1

    def delete(self, value):
        position = self.search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            
            self.last_position -= 1

vector = UnorderedVector(5)
vector.printValues()
vector.insert(2)
vector.printValues()
print("-"*30)
vector.insert(7)
vector.insert(5)
vector.insert(1)
vector.insert(4)
vector.printValues()
vector.insert(3)
print("-"*30)
print(vector.search(1))
print(vector.search(2))
print(vector.search(9))
print("-"*30)
vector.delete(5)
vector.printValues()
print("-"*30)
vector.delete(4)
vector.printValues()
print("-"*30)
vector.delete(2)
vector.printValues()
print("-"*30)




