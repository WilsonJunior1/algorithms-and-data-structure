import numpy as np

class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adjacents = []

    def addAdjacent(self, adjacent):
        self.adjacents.append(adjacent)

    def showAdjacents(self):
        for i in self.adjacents:
            print(i.vertex.label, i.cost)

class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost

class Graph:
  arad = Vertex('Arad')
  zerind = Vertex('Zerind')
  oradea = Vertex('Oradea')
  sibiu = Vertex('Sibiu')
  timisoara = Vertex('Timisoara')
  lugoj = Vertex('Lugoj')
  mehadia = Vertex('Mehadia')
  dobreta = Vertex('Dobreta')
  craiova = Vertex('Craiova')
  rimnicu = Vertex('Rimnicu')
  fagaras = Vertex('Fagaras')
  pitesti = Vertex('Pitesti')
  bucharest = Vertex('Bucharest')
  giurgiu = Vertex('Giurgiu')

  arad.addAdjacent(Adjacent(zerind, 75))
  arad.addAdjacent(Adjacent(sibiu, 140))
  arad.addAdjacent(Adjacent(timisoara, 118))

  zerind.addAdjacent(Adjacent(arad, 75))
  zerind.addAdjacent(Adjacent(oradea, 71))

  oradea.addAdjacent(Adjacent(zerind, 71))
  oradea.addAdjacent(Adjacent(sibiu, 151))

  sibiu.addAdjacent(Adjacent(oradea, 151))
  sibiu.addAdjacent(Adjacent(arad, 140))
  sibiu.addAdjacent(Adjacent(fagaras, 99))
  sibiu.addAdjacent(Adjacent(rimnicu, 80))

  timisoara.addAdjacent(Adjacent(arad, 118))
  timisoara.addAdjacent(Adjacent(lugoj, 111))

  lugoj.addAdjacent(Adjacent(timisoara, 111))
  lugoj.addAdjacent(Adjacent(mehadia, 70))

  mehadia.addAdjacent(Adjacent(lugoj, 70))
  mehadia.addAdjacent(Adjacent(dobreta, 75))

  dobreta.addAdjacent(Adjacent(mehadia, 75))
  dobreta.addAdjacent(Adjacent(craiova, 120))

  craiova.addAdjacent(Adjacent(dobreta, 120))
  craiova.addAdjacent(Adjacent(pitesti, 138))
  craiova.addAdjacent(Adjacent(rimnicu, 146))

  rimnicu.addAdjacent(Adjacent(craiova, 146))
  rimnicu.addAdjacent(Adjacent(sibiu, 80))
  rimnicu.addAdjacent(Adjacent(pitesti, 97))

  fagaras.addAdjacent(Adjacent(sibiu, 99))
  fagaras.addAdjacent(Adjacent(bucharest, 211))

  pitesti.addAdjacent(Adjacent(rimnicu, 97))
  pitesti.addAdjacent(Adjacent(craiova, 138))
  pitesti.addAdjacent(Adjacent(bucharest, 101))

  bucharest.addAdjacent(Adjacent(fagaras, 211))
  bucharest.addAdjacent(Adjacent(pitesti, 101))
  bucharest.addAdjacent(Adjacent(giurgiu, 90))

graph = Graph()

graph.arad.showAdjacents()

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1

        self.__values = np.empty(self.__capacity, dtype=object)

    def __isFull(self):
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def __isEmpty(self):
        if self.__top == -1:
            return True
        else:
            return False

    def stackUp(self, value):
        if self.__isFull():
            print("ERROR: Full Stack.")
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def unstack(self):
        if self.__isEmpty():
            print("ERROR: Empty Stack.")
            return None
        else:
            temp = self.__values[self.__top]
            self.__top -= 1
            return temp

    def showTop(self):
        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1

class DeepSearch:
    def __init__(self, start):
        self.start = start
        self.start.visited = True
        self.stack = Stack(20)
        self.stack.stackUp(start)

    def search(self):
        top = self.stack.showTop()
        print(f"Top: {top.label}")

        for adjacent in top.adjacents:
            print(f"Top is: {top.label}. {adjacent.vertex.label} has already been visited? {adjacent.vertex.visited}")
            if adjacent.vertex.visited == False:
                adjacent.vertex.visited = True
                self.stack.stackUp(adjacent.vertex)
                print(f"Stack Up: {adjacent.vertex.label}")
                self.search()
        print(f"Unstack: {self.stack.unstack().label}")
        print()

deep_search = DeepSearch(graph.arad)
deep_search.search()

class CircleQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.elements = 0

        self.values = np.empty(self.capacity, dtype=object)

    def __isEmpty(self):
        return self.elements == 0

    def __isFull(self):
        return self.elements == self.capacity

    def enqueue(self, value):
        if self.__isFull():
            print("ERROR: Full Queue.")
            return
        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.elements += 1

    def unqueue(self):
        if self.__isEmpty():
            print("ERROR: Empty Queue.")
            return 

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity - 1:
            self.start = 0
        self.elements -= 1
        return temp

    def first(self):
        if self.__isEmpty():
            return -1
        return self.values[self.start]

class BreadthSearch():
    def __init__(self, start):
        self.start = start
        self.start.visited = True
        self.queue = CircleQueue(20)
        self.queue.enqueue(start)

    def search(self):
        first = self.queue.first()
        print("-" * 30)
        print(f"First in line: {first.label}")
        temp = self.queue.unqueue()
        print(f"Dequeue: {temp.label}")
        for adjacent in first.adjacents:
            print(f"First in line: {temp.label}. {adjacent.vertex.label} Already visited?: {adjacent.vertex.visited}")
            if adjacent.vertex.visited == False:
                adjacent.vertex.visited = True
                self.queue.enqueue(adjacent.vertex)
                print(f"Enqueue: {adjacent.vertex.label}")
            if self.queue.elements > 0:
                self.search()

breadth_search = BreadthSearch(graph.arad)
breadth_search.search()


