class stack:
    def __init__(self):
        self.stack=[]
    top=-1
    def push(self,iteam):
        self.stack.append(iteam)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            print("stack is empty so you cant pop")
            return None
    def isempty(self):
        return len(self.stack)==0
    def peek(self):
        if self.isempty():
            raise IndexError("stackk is empty & cant peek")
        else:
            return self.stack[self.top]

mystack=stack()

mystack.push(5)
mystack.push(1)
mystack.push(7)
mystack.peek()

print(f"peaked element:{mystack.peek()}")
mystack.pop()
mystack.pop()
print(f"peaked element:{mystack.peek()}")

    
    