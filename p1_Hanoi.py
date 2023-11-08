def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)

# input numbers from user...
n = int(input("Enter the number of disks: "))
source = input("Enter the source tower :(e.g. => 'A'): ")
target = input("Enter the target tower :(e.g. => 'C'): ")
auxiliary = input("Enter the auxiliary tower :(e.g. => 'B'): ")

# calling the hanoi function...
hanoi(n, source, target, auxiliary)
