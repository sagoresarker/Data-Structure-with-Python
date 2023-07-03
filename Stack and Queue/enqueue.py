# FIFO

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)

        self.first = new_node
        self.last = new_node

        self.length = 1

    def print_queue(self):
        temp = self.first

        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None

        self.length -= 1

q = Queue(11)

q.enqueue(3)
q.enqueue(23)
q.enqueue(7)

q.print_queue()
print("\nlength of Queue: ", q.length)

q.dequeue()

q.print_queue()

print("\nafter deque \n")
q.dequeue()

q.print_queue()

print("\nafter deque \n")
q.dequeue()

q.print_queue()

print("\nafter deque \n")
q.dequeue()

q.print_queue()
print(q.length)