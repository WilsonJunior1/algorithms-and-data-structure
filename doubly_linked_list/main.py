class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def printNode(self):
        print(self.value)

class dbLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __isEmpty(self):
        return self.head == None

    def insertBeginning(self, value):
        new = Node(value)
        if self.__isEmpty():
            self.tail = new
        else:
            self.head.previous = new
        new.next = self.head
        self.head = new

    def insertEnd(self, end):
        new = Node(value)
        if self.__isEmpty():
            self.head = new
        else:
            self.tail.next = new
            new.previous = self.tail
        self.tail = new

    def deleteBeginning(self):
        temp = self.head
        if self.head.next == None:
            self.tail = None
        else:
            self.head.next.previous = None
        self.head = self.head.next
        return temp

    def deleteEnd(self):
        temp = self.tail
        if self.head.next == None:
            self.head = None
        else:
            self.tail.previous.next = None
        self.tail = self.tail.previous
        return temp

    def deletePosition(self, value):
        current = self.head
        while current.value != value:
            current = current.next
            if current == None:
                return None
        if current == self.head:
            self.head = current.next
        else:
            current.previous.next = current.next

        if current == self.tail:
            self.tail = current.previous
        else:
            current.next.previous = current.previous
        return current

    def showFront(self):
        current = self.head
        while current != None:
            current.printNode()
            current = current.next

    def showBack(self):
        current = self.tail
        while current != None:
            current.printNode()
            current = current.previous


list = dbLinkedList()

for i in range(10):
    list.insertBeginning(i)

list.showFront()
print("=" * 30)
list.showBack()
