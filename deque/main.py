import numpy as np

class Deque:
    def __init__(self, leng):
        self.leng = leng
        self.start = -1
        self.end = 0
        self.elements = 0
        self.values = np.empty(self.leng, dtype=int)

    def __isFull(self):
        return (self.start == 0 and self.end == self.leng - 1) or (self.start == self.end + 1)

    def __isEmpty(self):
        return self.start == -1

    def insertStart(self, value):
        if self.__isFull():
            print('The Deque is full!')
            return

        if self.start == -1:
            self.start = 0
            self.end = 0

        elif self.start == 0:
            self.start = self.leng - 1
        else:
            self.start -= 1

        self.values[self.start] = value

    def insertEnd(self, value):
        if self.__isFull():
            print("The Deque is full!")
            return

        if self.start == -1:
            self.start = 0
            self.end = 0

        elif self.end == self.leng - 1:
            self.end = 0

        else:
            self.end += 1

        self.values[self.end] = value

    def deleteStart(self):
        if self.__isEmpty():
            print("The Deque is empty!")
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1

        else:
            if self.start == self.leng - 1:
                self.start = 0
            else:
                self.start += 1

    def deleteEnd(self):
        if self.__isEmpty():
            print("The Deque is empty!")
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1

        elif self.start == 0:
            self.end = self.leng - 1
            
        else:
            self.end -= 1

    def getStart(self):
        if self.__isEmpty():
            print("The Deque is empty!")
            return

        return self.values[self.start]

    def getEnd(self):
        if self.__isEmpty() or self.end < 0:
            print("The Deque is empty!")
            return 
        
        return self.values[self.end]


deque = Deque(10)

deque.insertEnd(5)
print(deque.getStart(), deque.getEnd())

deque.insertEnd(20)
print(deque.getStart(), deque.getEnd())

deque.insertStart(1)
print(deque.getStart(), deque.getEnd())


