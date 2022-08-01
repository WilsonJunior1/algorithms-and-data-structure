class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None

    def printNode(self):
        print(self.value)


class DeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __isEmpty(self):
        return self.head == None

    def insertBeginning(self, value):
        new = Node(value)
        if self.__isEmpty():
            self.tail = new

        new.next = self.head
        self.head = new

    def insertEnd(self, value):
        new = Node(value)
        if self.__isEmpty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    def deleteBeginning(self):
        if self.__isEmpty():
            print("ERROR: Empty list.")
            return 
        
        temp = self.head
        if self.head.next == None:
            self.tail = None
        self.head =  self.head.next
        return temp

    def show(self):
        if self.__isEmpty():
            print("ERROR: Empty list.")
            return 

        current = self.head
        while current != None:
            current.printNode()
            current = current.next

list = DeList()

list.insertBeginning(1)

print(list.head, list.tail)

for i in range(5):
    list.insertBeginning(i)

list.show()

list.insertEnd(10)
list.insertEnd(15)

list.show()

for i in range(3):
    list.deleteBeginning()

list.show()

for i in range(10):
    list.deleteBeginning()

