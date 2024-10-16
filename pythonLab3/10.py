def generate_tuples_with_values_on_list_index(*lists):
    max_len = max(len(lst) for lst in lists)
    for lst in lists:
            max_len = max(max_len, len(lst))
    tuples=[]
    values = []
    for lst in lists:
        for i in range(max_len):
            if len(values) <= i:
                values.append([])
            if len(lst) <= i:
                values[i].append(None)
            else:
                values[i].append(lst[i])
    for entry in values:
        tuples.append(tuple(entry))
    return tuples

# im sure there is an easier method :D

print(generate_tuples_with_values_on_list_index([1,2,3], [5,6,7], ["a", "b", "c"]))