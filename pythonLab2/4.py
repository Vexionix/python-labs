def convert_UpperCamelCase_to_snake_case(str):
    new_str = ""
    index = 0
    while index < len(str) :
        if str[index].isupper():
            if index != 0:
                new_str += "_" + str[index].lower()
            else:
                new_str += str[index].lower()
        else:
            new_str += str[index]
        index += 1
    return new_str

print("Enter the UpperCamelCase string you want to convert:")
string = input()
print("The converted string from Upper Camel Case to snake_case is \"" + convert_UpperCamelCase_to_snake_case(string) + "\"")