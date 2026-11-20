divisible_by_4 = []
divisible_by_6 = []
divisible_by_8 = []
divisible_by_10 = []
divisible_by_3 = []
divisible_by_5 = []
divisible_by_7 = []
divisible_by_9 = []

for num in range(151):

    if num % 4 == 0:
        divisible_by_4.append(num)

    if num % 6 == 0:
        divisible_by_6.append(num)

    if num % 8 == 0:
        divisible_by_8.append(num)

    if num % 10 == 0:
        divisible_by_10.append(num)

    if num % 3 == 0:
        divisible_by_3.append(num)

    if num % 5 == 0:
        divisible_by_5.append(num)

    if num % 7 == 0:
        divisible_by_7.append(num)

    if num % 9 == 0:
        divisible_by_9.append(num)

print("Divisible by 4:", divisible_by_4)
print("Divisible by 6:", divisible_by_6)
print("Divisible by 8:", divisible_by_8)
print("Divisible by 10:", divisible_by_10)
print("Divisible by 3:", divisible_by_3)
print("Divisible by 5:", divisible_by_5)
print("Divisible by 7:", divisible_by_7)
print("Divisible by 9:", divisible_by_9)