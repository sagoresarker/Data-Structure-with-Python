class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_ll(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node       
        self.tail = new_node


        self.length += 1

        return True
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head

            new_node.next = self.head
            self.head = new_node

        
        self.length += 1

    

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.print_ll()

print("After prepend")
ll.prepend(100)
ll.print_ll()
