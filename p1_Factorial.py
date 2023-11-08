def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))

# input numbers from user...
n = int(input("Enter the value of n:"))
k = int(input("Enter the value of k:"))

# calling power combination function...
result = combination(n, k)
print(f"The combination of {n} items taken {k} at a time is = {result}")
