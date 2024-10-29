def unique_and_duplicate_counts(given_list):
    set_from_list = set(given_list)
    duplicate_count = len(given_list) - len(set_from_list)
    return len(set_from_list), duplicate_count

my_list = [7, 7, 1, 7, 3, 3, 2]
print("For", my_list, "the unique and duplicate counts are:")
print(unique_and_duplicate_counts(my_list))
