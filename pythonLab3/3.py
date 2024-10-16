def list_operations(a: [], b: []):
    intersection = []
    for i in a:
        if i in b:
            intersection.append(i)

    reunion = []
    for i in a:
        reunion.append(i)
    for i in b:
        if i not in reunion:
            reunion.append(i)

    a_minus_b = []
    for i in a:
        if i not in b:
            a_minus_b.append(i)

    b_minus_a = []
    for i in b:
        if i not in a:
            b_minus_a.append(i)

    return [intersection, reunion, a_minus_b, b_minus_a]

a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 6, 7]

result = list_operations(a, b)

print("a:", a)
print("b:", b)
print("Intersection:", result[0])
print("Reunion:", result[1])
print("a-b:", result[2])
print("b-a:", result[3])