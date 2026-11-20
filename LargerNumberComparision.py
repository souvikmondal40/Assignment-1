input_list = list(map(int, input("Enter numbers: ").split()))

output_list = []

for i in range(len(input_list)):
    found = False

    for j in range(i + 1, len(input_list)):
        if input_list[j] > input_list[i]:
            output_list.append(input_list[j])
            found = True
            break

    if found == False:
        output_list.append(-1)

print("Original list:", input_list)
print("Output list:", output_list)