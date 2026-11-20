numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers) + 1):
        print(numbers[i:j])