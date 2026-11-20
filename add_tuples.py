def add_tuples(list1, list2):
    result = []

    for i in range(len(list1)):
        a = list1[i]
        b = list2[i]

        new_tuple = (a[0] + b[0], a[1] + b[1])

        result.append(new_tuple)

    return result


list1 = [(1, 2), (3, 4)]
list2 = [(5, 6), (7, 8)]

output = add_tuples(list1, list2)

print("Result:", output)