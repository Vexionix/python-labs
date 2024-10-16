def elements_appearing_x_times(*given_lists, expected_appearances):
    element_counter = {}
    for lst in given_lists:
        for element in lst:
            if element not in element_counter:
                element_counter[element] = 1
            else:
                element_counter[element] += 1

    valid_elements = []
    for element in element_counter:
        if element_counter[element] == expected_appearances:
            valid_elements.append(element)

    return valid_elements

x = 2

print("Initial lists:", [1,2,3], [2,3,4], [4,5,6], [4,1,"test"])
print("x =", x)
result =  elements_appearing_x_times([1,2,3], [2,3,4], [4,5,6], [4,1,"test"], expected_appearances=x)
print("Elements appearing", x, "times:", result)