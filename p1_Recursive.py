def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# input numbers from user...
base = float(input("Enter base number:"))
exponent = int(input("Enter exponent number:"))

# call power function...
result = power(base, exponent)
print(f"Number to {base} the power of {exponent} is equal = {result}")
