def loop(mapping):
    result = []
    visited_keys = set()

    current_key = 'start'
    while current_key not in visited_keys:
        visited_keys.add(current_key)
        current_value = mapping[current_key]
        result.append(current_value)
        current_key = current_value

    return result

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
