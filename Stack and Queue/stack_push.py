class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class Statck:
    def __init__(self, value):
        new_node  = Node(value)

        self.top = new_node
        self.height = 1
    
    def print_ll(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node  = Node(value)

        if self.top is None:
            self.top = new_node
        
        new_node.next = self.top
        self.top = new_node

        self.height += 1


s = Statck(100)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_ll()

print("\nHeight of Stack is : ", s.height)
