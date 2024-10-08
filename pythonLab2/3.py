def count_substr_appearances_in_str(substr, str):
    return str.count(substr)

print("Enter the string:")
string = input()
print("Enter the substring:")
substring = input()
print("The given substring appears", count_substr_appearances_in_str(substring, string), "times in the given string.")
