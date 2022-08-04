import numpy as np

class Stack:
    def __init__(self, leng):
        self.__leng = leng
        self.__top = -1
        self.__values = np.empty(self.__leng, dtype=int)

    def __isFull(self):
        if self.__top == self.__leng - 1:
            return True
        else:
            return False

    def __isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def push(self, value):
        if self.__isFull():
            print("The Stack is full.")
        else:
            self.__top += 1 
            self.__values[self.__top] = value

    def pop(self):
        if self.__isEmpty():
            print("The Stack is empty.")
        else:
            self.__top -= 1
    
    def showTop(self):
        print(f"Top: {self.__values[self.__top]}")


stack = Stack(5)
stack.push(4)
stack.push(1)
stack.push(6)
stack.push(8)
stack.push(9)

# Full
stack.push(2)
stack.push(1)

stack.showTop()

stack.pop()
stack.pop()

stack.showTop()

stack.pop()
stack.pop()
stack.pop()
stack.pop()

