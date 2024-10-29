def char_occurrences(string):
    occurrences = {}

    for ch in string:
        if ch in occurrences:
            occurrences[ch] += 1
        else:
            occurrences[ch] = 1

    return occurrences

print(char_occurrences("Ana has apples."))