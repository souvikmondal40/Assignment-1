numbers = list(map(int, input("Enter numbers: ").split()))

first = 0
second = 0
third = 0

for num in numbers:

    if num > first:
        third = second
        second = first
        first = num

    elif num > second:
        third = second
        second = num

    elif num > third:
        third = num

print("Third largest number:", third)