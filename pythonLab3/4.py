def compose(musical_strings: [], moves: [], start_pos: int):
    pos = start_pos
    composed_string = [musical_strings[pos]]
    for move in moves:
        pos = (pos + move) % len(musical_strings)
        composed_string.append(musical_strings[pos])
    return composed_string

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

