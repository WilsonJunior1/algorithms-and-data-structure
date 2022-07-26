import numpy as np

class Pqueue:
    def __init__(self, leng):
        self.leng = leng
        self.elements = 0
        self.values = np.empty(self.leng, dtype=int)

    def __isEmpty(self):
        return self.elements == 0
    
    def __isFull(self):
        return self.elements == self.leng

    def enqueue(self, value):
        if self.__isFull():
            print("The Queue is full!")
            return 
        
        if self.elements == 0:
            self.values[self.elements] = value
            self.elements += 1
        else:
            y = self.elements - 1
            while y >= 0:
                if value > self.values[y]:
                    self.values[y + 1] = self.values[y]
                else:
                    break
                y -= 1
            self.values[y + 1] = value
            self.elements += 1

    def dequeue(self):
        if self.__isEmpty():
            print("The Queue is empty!")
            return

        value = self.values[self.elements - 1]
        self.elements -= 1
        return value

    def printFirstElement(self):
        if self.__isEmpty():
            return -1
        return self.values[self.elements - 1]

pQueue = Pqueue(10)
print(pQueue.printFirstElement())

for i in range(len(pQueue.values)):
    pQueue.enqueue(i + 10)

print(pQueue.values)
print(pQueue.printFirstElement())

for i in range(5):
    pQueue.dequeue()

print(pQueue.printFirstElement())
pQueue.enqueue(2)
print(pQueue.printFirstElement())
print(pQueue.values)
