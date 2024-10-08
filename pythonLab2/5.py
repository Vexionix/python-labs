def is_palindrome(number):
    number_copy = number
    reversed_number = 0
    while number_copy > 0:
        reversed_number = reversed_number * 10 + number_copy % 10
        number_copy //= 10
    return reversed_number == number

print("Enter the number for which you want to check whether or not it is a palindrome:")
number_string = input()
number = int(number_string)
if is_palindrome(number) == True:
    print("It is a palindrome")
else:
    print("It is not a palindrome")