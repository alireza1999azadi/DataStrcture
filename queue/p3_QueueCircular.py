class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, obj):
        new_node = Node(obj)
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        if not self.front:
            raise IndexError("Queue is empty. Cannot dequeue.")
        removed_obj = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        return removed_obj

    def peek(self):
        if not self.front:
            raise IndexError("Queue is empty. Cannot peek.")
        return self.front.data

    def reverse_queue(self):
        if not self.front:
            raise IndexError("Queue is empty. Cannot reverse.")
        prev_node = None
        current_node = self.front
        next_node = self.front.next

        while next_node != self.front:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

        current_node.next = prev_node
        self.front = current_node
        self.rear = next_node

    def is_empty(self):
        return not self.front

    def is_full(self):
        return False

# Getting input from the user...
size = int(input("Enter the size of the circular queue: "))
my_circular_queue = CircularQueue()

# Enqueue elements based on user input
for i in range(size):
    obj = input(f"Enter the value to enqueue at index {i}: ")
    my_circular_queue.enqueue(obj)

# Print the front element
print(f"Peeked element: {my_circular_queue.peek()}")

# Dequeue an element
try:
    dequeued_element = my_circular_queue.dequeue()
    print(f"Dequeued element: {dequeued_element}")
except IndexError as e:
    print(e)

# Reverse the circular queue
try:
    my_circular_queue.reverse_queue()
    print("Reversed queue:", end=" ")
    while not my_circular_queue.is_empty():
        print(my_circular_queue.dequeue(), end=" ")
except IndexError as e:
    print(e)

# Check if the circular queue is empty
print("\nIs the circular queue empty?", my_circular_queue.is_empty())
