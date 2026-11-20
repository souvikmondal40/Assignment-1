
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) >= 2:
    temp = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = temp

print("Updated list:", numbers)
