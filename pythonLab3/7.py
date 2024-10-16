def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False

def get_palindrome_info(number_list):
    max_palindrome = -1
    palindrome_counter = 0
    for number in number_list:
        if is_palindrome(number):
            palindrome_counter += 1
            if number > max_palindrome:
                max_palindrome = number
    return palindrome_counter, max_palindrome

nr_list = [1, 111, 123, 321, 121]
print("The number of palindromes and the max palindromes in the list", nr_list, "are: ")
print(get_palindrome_info(nr_list))