# Faça um programa que leia uma expressão, o programa deverá validar os carácteres
# () {} e [], na primeira ocorrência de abertura de um caráctere, empilhe, na primeira
# ocorrência de fechamento, desempilhe, retorne um erro caso não haja um caráctere correspondente
# Se no final a pilha estiver vazia, então a expressão é válida.

class Stack:
    def __init__(self):
        self.top = 0
        self.values = []

    def isEmpty(self):
        if self.top == 0:
            return True
        else:
            return False

    def showTop(self):
        print(f"Top: {self.values}")
        print(self.top)

    def push(self, value):
        self.top += 1
        self.values.append(value)

    def pop(self):
        if self.isEmpty():
            print("Invalid expression.")
        else:
            self.top -= 1
            self.values.pop()

stack = Stack()

expression = input("Enter an expression:")

for i in expression:
    if i == "(":
        stack.push(i)
    elif i == "[":
        stack.push(i)
    elif i == "{":
        stack.push(i)
    else:
        if i == ")":
            stack.pop()
        elif i == "]":
            stack.pop()
            stack.showTop()
        elif i == "}":
            stack.pop()

if stack.isEmpty():
    print("Valid expression.")
else:
    print("Invalid expression.")


