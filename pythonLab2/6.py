def extract_number_from_str(str):
    number = 0
    index = 0
    flag = 0
    while index < len(str):
        if str[index].isdigit():
            number = number * 10 + int(str[index])
            flag = 1
        elif flag == 1:
            break
        index += 1
    if flag == 0:
        return "No number found!"
    return number

print("Enter the string from which you want to extract the first number from:")
string = input()
print("The first number in the given input string is", extract_number_from_str(string))