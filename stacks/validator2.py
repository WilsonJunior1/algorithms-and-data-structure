import numpy as np

class Stack:
    def __init__(self, leng):
        self.leng = leng
        self.top = -1
        self.values = np.chararray(self.leng, unicode=True)

    def isFull(self):
        if self.top == self.leng - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def push(self, value):
        if self.isFull():
            print("The Stack is full.")
        else:
            self.top += 1
            self.values[self.top] = value

    def pop(self):
        if self.isEmpty():
            print("The Stack is empty.")
        else:
            value = self.values[self.top]
            self.top -= 1
            return value

    def printTop(self):
        if self.top != -1:
            print(f"Top: {self.values[self.top]}")
        else:
            return -1


expression = str(input("Enter an expression:"))
stack = Stack(len(expression))

for i in expression:
    if i == "(" or i == "[" or i == "{":
        stack.push(i)
    
    elif i == ")" or i == "]" or i == "}":
        if not stack.isEmpty():
            ch = str(stack.pop())
            if (i == "(" and ch != ")") or (i == "[" and ch != "]") or (i == "{" and ch != "}"):
                print("Error: invalid expression.")
                break
        else:
            print("Error: invalid expression.") 
if not stack.isEmpty():
    print("Error")








