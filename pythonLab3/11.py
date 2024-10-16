def reorder_list_by_tuple_member(tuples):
    for i in range(len(tuples)-1):
        for j in range(i, len(tuples), 1):
            if tuples[i][1][2] > tuples[j][1][2]:
                aux = tuples[i]
                tuples[i] = tuples[j]
                tuples[j] = aux
    return tuples

print(reorder_list_by_tuple_member([('abc', 'bcd'), ('abc', 'zza')]))