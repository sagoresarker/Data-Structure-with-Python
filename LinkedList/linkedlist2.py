# class Node:
#     def __init__(self, value):
#         self.value =  value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# a = LinkedList(4)
# b = LinkedList(5)
# c = LinkedList(6)
# d = LinkedList(7)

# #print(a.head.value)

# for i in [a, b, c, d]:
#     print(i.head.value)
#     print(i.tail.next)

class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

ll = LinkedList(4)

print(ll.head.value)