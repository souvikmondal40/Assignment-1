numbers = list(map(int, input("Enter numbers: ").split()))

target = int(input("Enter number to delete: "))

numbers.remove(target)

print("Updated list:", numbers)