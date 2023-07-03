class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
            

bst = BinarySearchTree()

bst.insert(47)
bst.insert(21)
bst.insert(76)
bst.insert(38)
bst.insert(27)
bst.insert(52)
bst.insert(82)

print(bst.root.value) 
print(bst.root.left.value) 
print(bst.root.right.value) 

print(bst.contains(17))