import numpy as np

class Queue:
    def __init__(self, leng):
        self.leng = leng
        self.start = 0
        self.end = -1
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
        
        if self.end == self.leng - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.elements += 1

    def dequeue(self):
        if self.__isEmpty():
            print("The Queue is empty!")
            return
        
        temp = self.values[self.start]
        self.start += 1

        if self.start == self.leng - 1:
            self.start = 0
        self.elements -= 1
        return temp

    def printFirstItem(self):
        if self.__isEmpty():
            return -1
        return self.values[self.start]

queue = Queue(10)
print(queue.printFirstItem())

for i in range(len(queue.values)):
    queue.enqueue(i)

print(queue.printFirstItem())

print(queue.values)

for i in range(0, 4):
    queue.dequeue()

queue.enqueue(10)
queue.enqueue(11)

print(queue.values)
print(queue.end)
print(queue.values[queue.end])
print(queue.printFirstItem())







