even_list = []
odd_list = []

for num in range(151):
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)