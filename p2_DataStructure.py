class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, obj, index):
        if 0 <= index < self.size:
            self.array[index] = obj
        else:
            raise IndexError("Index out of bounds.")

    def delete(self, index):
        if 0 <= index < self.size:
            deleted_obj = self.array[index]
            self.array[index] = None
            return deleted_obj
        else:
            raise IndexError("Index out of bounds.")

    def find(self, obj):
        for i in range(self.size):
            if self.array[i] == obj:
                return i
        return -1

# Getting input from the user...
size = int(input("Enter the size of the array : "))
arr = Array(size)

# Setting values in the array...
for i in range(size):
    obj = input(f"Enter the value for index {i} : ")
    arr.insert(obj, i)

# Getting the index of a specific object...
search_obj = input("Enter the object to find it's index : ")
index = arr.find(search_obj)
if index != -1:
    print(f"The index of the object is = {index}")
else:
    print("Object not found in the array.")

# Deleting an object at a specific index...
delete_index = int(input("Enter the index to delete the object : "))
if 0 <= delete_index < size:
    deleted_object = arr.delete(delete_index)
    print(f"The deleted object is = {deleted_object}")
else:
    print("Invalid index provided.")

# Printing the length of the array...
print(f"The length of the array is = {arr.size}")
