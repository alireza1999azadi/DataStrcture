class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []  # For input elements
        self.dequeue_stack = []  # For output elements

    def enqueue(self, item):
        # Adding an item to the input stack
        self.enqueue_stack.append(item)

    def dequeue(self):
        # If the output stack is empty, transfer elements from the input stack to it
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return "The queue is empty"
            while self.enqueue_stack:
                # Transfer elements from the input stack to the output stack
                self.dequeue_stack.append(self.enqueue_stack.pop())
        # Now we can return the top element from the output stack (dequeue operation)
        return self.dequeue_stack.pop()


queue = QueueUsingStack()

while True:
    print("Select an option:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Exit")
    
    
    
    choice = int(input())
    
    if choice == 1:
        item = int(input("Enter the element: "))
        queue.enqueue(item)
        print(f"{item} has been added to the queue.")
    elif choice == 2:
        item = queue.dequeue()
        if item == "The queue is empty":
            print("The queue is empty.")
        else:
            print(f"{item} has been dequeued.")
    elif choice == 3:
        break
    else:
        print("Invalid input!")
