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

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp.value
    
    def totalLength(self):
        ll_length = 0
        temp = self.head

        while temp:
            ll_length += 1
            temp = temp.next

        return ll_length

    def middleOfLL(self):
        total_length = self.totalLength()
        half = 0

        if total_length % 2 == 0:
            half = total_length // 2 
        else:
            half = total_length // 2

        return self.get(half)


ll = LinkedList(2)

ll.append(4)
ll.append(6)
ll.append(7)
ll.append(5)
#ll.append(1)

ll.print_list()

print('\n Middle of ll\n')

print(ll.middleOfLL())