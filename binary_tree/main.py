import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def showNode(self):
        print(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.connections = []

    def insert(self, value):
        new = Node(value)

        if self.root == None:
            self.root == new

        else:
            current = self.root
            while True:
                father = current
                # Left
                if value < current.value:
                    current = current.left
                    if current == None:
                        father.left = new
                        self.connections.append(str(father.value) + '->' + str(new.value))
                        return
                # Right
                else:
                    current = current.right
                    if current == None:
                        father.right = new
                        self.connections.append(str(father.value) + '->' + str(new.value))
                        return


    def search(self, value):
        current = self.root
        while current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right

            if current == None:
                return None
        return current

    #Root, left, right

    def preOrder(self, node):
        if node != None:
            print(node.value)
            self.preOrder(node.left)
            self.preOrder(node.right)

    # Left, root, right

    def ordened(self, node):
        if node != None:
            self.ordened(node.left)
            print(node.value)
            self.ordened(node.right)

    # Left, right, root

    def posOrder(self, node):
        if node != None:
            self.posOrder(node.left)
            self.posOrder(node.right)
            print(node.value)

    def delete(self, value):
        if self.root == None:
            print("ERROR: Empty tree.")
            return

        # Find node
        current = self.root
        father = self.root
        is_left = True

        while current.value != value:
            father = current

            #Left
            if value < current.value:
                is_left = True
                current = current.left

            #Right
            else:
                is_left = False
                current = current.right
            if current == None:
                return False

        if current.left == None and current.right == None:
            if current == self.root:
                self.root = None
            elif is_left == True:
                self.connections.remove(str(father.value) + '->' + str(current.value))
                father.left = None
            else:
                self.connections.remove(str(father.value) + '->' + str(current.value))
                father.right = None

        elif current.right == None:
            self.connections.remove(str(father.value) + '->' + str(current.value))
            self.connections.remove(str(current.value) + '->' + str(current.left.value))
            
            if current == self.root:
                self.root = current.left
                self.connections.append(str(root.value) + '->' + str(current.left.value))
            
            elif is_left == True:
                father.left = current.left
                self.connections.append(str(father.value) + '->' + str(current.left.value))

            else:
                father.right = current.left
                self.connections.append(str(father.value) + '->' + str(current.left.value))

        elif current.left == None:
            self.connections.remove(str(father.value) + '->' + str(current.value))
            self.connections.remove(str(current.value) + '->' + str(current.right.value))

            if current == self.root:
                self.connections.append(str(root.value) + '->' + str(current.right.value))
                self.root = current.right

            elif is_left == True:
                self.connections.append(str(father.value) + '->' + str(current.right.value))
                father.left = current.right

            else:
                self.connections.append(str(father.value) + '->' + str(current.right.value))
                father.right = current.right

        else:
            sucessor = self.get_sucessor(current)

            self.connections.remove(str(father.value) + '->' + str(current.value))
            self.connections.remove(str(current.right.value) + '->' + str(sucessor.value))
            self.connections.remove(str(current.value) + '->' + str(current.left.value))
            self.connections.remove(str(current.value) + '->' + str(current.right.value))

            if current == self.root:
                self.connections.append(str(root.value) + '->' + str(sucessor.value))
                self.root = sucessor

            elif is_left == True:
                self.connections.append(str(father.value) + '->' + str(sucessor.value))
                father.left = sucessor

            else:
                self.connections.append(str(father.value) + '->' + str(sucessor.value))
                father.value  = sucessor

            self.connections.append(str(sucessor.value) + '->' + str(current.left.value))
            self.connections.append(str(sucessor.value) + '->' + str(current.right.value))

            sucessor.left = current.left
        
        return True

    def getSucessor(self, node):
        father_sucessor = node
        sucessor = node
        current = node.right

        while current != None:
            father_sucessor = sucessor
            sucessor = current
            current = current.left

        if sucessor != node.right:
            father_sucessor.left = sucessor.right
            sucessor.right = node.right

        return sucessor


tree = BinaryTree()
tree.insert(53)
tree.insert(30)
tree.insert(14)
tree.insert(39)
tree.insert(9)
tree.insert(23)
tree.insert(34)
tree.insert(49)
tree.insert(72)
tree.insert(61)
tree.insert(84)
tree.insert(79)

print("=" * 30)
print(tree.root.left.value)

print("=" * 30)
print(tree.root.right.value)

print("=" * 30)

tree.insert(89)

print(tree.connections)
