numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = ""

for num in numbers:
    result += str(num)

result = int(result)

print("Combined integer:", result)