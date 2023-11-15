class Queue:
    def __init__(self, capacity):
        # Constructor to initialize the queue with a given capacity
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, obj):
        if self.is_full():
            raise IndexError("Queue is full. Cannot enqueue.")
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = obj

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue.")
        removed_obj = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return removed_obj

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek.")
        return self.queue[self.front]

    def reverse_queue(self):
        reversed_queue = Queue(self.capacity)
        while not self.is_empty():
            reversed_queue.enqueue(self.dequeue())
        return reversed_queue

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.capacity - 1

# Getting input from the user for the queue capacity...
capacity = int(input("Enter the capacity of the queue: "))
my_queue = Queue(capacity)

# Enqueue elements based on user input
for i in range(capacity):
    obj = input(f"Enter the value to enqueue at index {i}: ")
    my_queue.enqueue(obj)

# Print the front element
print(f"Peeked element: {my_queue.peek()}")

# Dequeue an element
dequeued_element = my_queue.dequeue()
print(f"Dequeued element: {dequeued_element}")

# Reverse the queue
reversed_queue = my_queue.reverse_queue()
print("Reversed queue:", end=" ")
while not reversed_queue.is_empty():
    print(reversed_queue.dequeue(), end=" ")

# Check if the queue is empty or full
print("\nIs the queue empty?", my_queue.is_empty())
print("Is the queue full?", my_queue.is_full())
