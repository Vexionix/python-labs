def count_words(str):
    return len(str.split())

print("Enter the string of which you want the count the number of words:")
string = input();
print("The given string has", count_words(string), "words.")