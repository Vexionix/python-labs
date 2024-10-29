def set_operations(*sets):
    result_dictionary = {}
    list_of_sets = list(sets)

    for i in range(len(list_of_sets)-1):
        for j in range(i + 1, len(list_of_sets)):
            set_a = list_of_sets[i]
            set_b = list_of_sets[j]
            result_dictionary[f"{set_a} | {set_b}"] = set_a | set_b
            result_dictionary[f"{set_a} & {set_b}"] = set_a & set_b
            result_dictionary[f"{set_a} - {set_b}"] = set_a - set_b
            result_dictionary[f"{set_b} - {set_a}"] = set_b

    return result_dictionary

sets = [{1,2}, {2, 3}]
result = set_operations(*sets)
for k, v in result.items():
    print(f"{k}: {v}")
