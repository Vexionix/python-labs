def vowel_count(str):
    vowel_count_var = 0
    for ch in str:
        if "AEIOUaeiou".find(ch) != -1 :
            vowel_count_var += 1
    return vowel_count_var


print("Enter the string you want to compute the number of vowels for:")
string = input()
print("Vowels found in \"" + string + "\" :", vowel_count(string))