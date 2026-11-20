mixed_list = input("Enter elements separated by spaces: ").split()

integer_list = []
string_list = []
float_list = []

for num in mixed_list:

    try:
        if "." in num:
            float_list.append(float(num))
        else:
            integer_list.append(int(num))

    except ValueError:
        string_list.append(num)

print("Integer list:", integer_list)
print("String list:", string_list)
print("Float list:", float_list)