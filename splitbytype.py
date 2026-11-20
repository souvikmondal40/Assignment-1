mixed_list = input("Enter elements separated by spaces: ").split()

integer_list = []
string_list = []
float_list = []

for item in mixed_list:
    try:
        if "." in item:
            float_list.append(float(item))
        else:
            integer_list.append(int(item))
    except ValueError:
        string_list.append(item)

print("Integer list:", integer_list)
print("String list:", string_list)
print("Float list:", float_list)