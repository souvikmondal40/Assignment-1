main_list = list(map(int, input("Enter main list: ").split()))
sub_list = list(map(int, input("Enter sublist: ").split()))

count = 0

for i in range(len(main_list)):
    if main_list[i:i+len(sub_list)] == sub_list:
        count = 1
        break

if count == 1:
    print("Sublist found")
else:
    print("Sublist not found")