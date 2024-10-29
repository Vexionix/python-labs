def compare_dictionaries(first, second):
    if type(first) != type(second):
        return False

    if isinstance(first, dict):
        if first.keys() != second.keys():
            return False
        return all(compare_dictionaries(first[key], second[key]) for key in first)

    if isinstance(first, list):
        if len(first) != len(second):
            return False
        return all(compare_dictionaries(item1, item2) for item1, item2 in zip(first, second))

    if isinstance(first, set):
        return first == second

    return first == second

first_dictionary = {
    "first_key": {
        "sub_dictionary": { "a" : 5, "b" : 2, "c": 7 },
        "subkey": {"subkey_sub_dictionary": { "a" : 4, "b" : 1 }}
    },
    "second_key": [1,2,3,4],
    "third_key": 17
}

second_dictionary = {
    "first_key": {
        "sub_dictionary": {"a": 5, "b": 2, "c": 7},
        "subkey": {"subkey_sub_dictionary": {"a": 4, "b": 1}}
    },
    "second_key": [1, 2, 3, 4],
    "third_key": 17
}

third_dictionary = {
    "random_key": 0
}

print("Comparing first with second")
if compare_dictionaries(first_dictionary, second_dictionary):
    print("The given dictionaries are equal")
else:
    print("The given dictionaries are NOT equal")

print("Comparing first with third")
if compare_dictionaries(first_dictionary, third_dictionary):
    print("The given dictionaries are equal")
else:
    print("The given dictionaries are NOT equal")

