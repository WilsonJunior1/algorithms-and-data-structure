class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def printNode(self):
        print(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def show(self):
        if self.head ==  None:
            print("The list is empty!")
            return None

        current = self.head
        while current != None:
            current.printNode()
            current = current.next

    def delete(self):
        if self.head == None:
            print("The list is empty!")
            return None

        temp = self.head
        self.head = self.head.next
        return temp

    def search(self, value):
        if self.head == None:
            print("The list is empty!")
            return None

        current = self.head
        while current.value != value:
            if current.next == None:
                print("Element not found!")
                return None
            else:
                current = current.next
        return current

    def deletePosition(self, value):
        current = self.head
        previous = self.head

        while current.value != value:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.head:
            self.head = self.head.next
        else:
            previous.next = current.next

        return current

list = LinkedList()

for i in range(10):
    list.insert(i)

list.show()

print("=" * 30)

for i in range(3):
    list.delete()

list.show()

print("=" * 30)

search = list.search(9)

if search != None:
    print("Sucess!")
else:
    print("ERROR: Element not found.")

list.deletePosition(2)

list.show()
