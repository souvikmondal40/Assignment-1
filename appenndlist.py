list1 = list(map(int, input("Enter first list: ").split()))

list2 = list(map(int, input("Enter second list: ").split()))

list2.extend(list1)

print("Combined list:", list2)