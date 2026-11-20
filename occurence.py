
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

target = int(input("Enter element to count: "))

count = numbers.count(target)

print(target, "occurs", count, "times")
