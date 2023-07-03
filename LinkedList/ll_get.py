class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node

        self.length = 1

    def print_ll(self):
        if self.head is None:
            return None
        temp = self.head

        while temp.next is not None:
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
        
        # temp = self.head
        # pre = self.head

        # while temp.next:
        #     pre = temp
        #     temp = temp.next
        
        # pre.next = new_node
        # new_node.next = None

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node

        self.length += 1
    
    def pop(self):
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

    def pop_first(self):
        if self.length==0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.tail = None
            
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next
        
        return temp.value


ll = LinkedList(1)


ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
print('After Append')
ll.print_ll()

print('After index')
print(ll.get(1))