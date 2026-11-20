def reverse_tuples(tuples):
    result = []

    for item in tuples:
        result.append(item[::-1])

    return result


tuples = [(1, 2), (3, 4), (5, 6)]

output = reverse_tuples(tuples)

print("Reversed tuples:", output)