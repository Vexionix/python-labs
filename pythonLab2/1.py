def read_numbers():
    numbers = []
    print("Enter the numbers of which you want to find the gcd of: ")
    numbers_string = input()
    for number in numbers_string.split(' '):
        numbers.append(int(number))
    return numbers

def gcd(first, second):
    while first != 0:
        rest = second % first
        second = first
        first = rest
    return second

def gcd_of_multiple_numbers(numbers):
    index = 1
    if len(numbers) < 1:
        return "Error! No numbers provided"
    if len(numbers) == 1:
        return numbers[0]
    gcd_value = numbers[0]
    while index < len(numbers):
        gcd_value = gcd(gcd_value, numbers[index])
        index += 1
    return gcd_value

numbers = read_numbers()
print("The gcd of the inputed  numbers is", gcd_of_multiple_numbers(numbers))