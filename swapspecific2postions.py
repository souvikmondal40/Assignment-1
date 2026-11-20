numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

pos1 = int(input("Enter first position: "))
pos2 = int(input("Enter second position: "))

temp = numbers[pos1]
numbers[pos1] = numbers[pos2]
numbers[pos2] = temp

print("Updated list:", numbers)