def group_by_rhyme(words):
    result = {}

    for word in words:
        rhyme_key = word[-2:] if len(word) > 1 else word

        if rhyme_key in result:
            result[rhyme_key].append(word)
        else:
            result[rhyme_key] = [word]

    return list(result.values())

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))