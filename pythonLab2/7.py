def count_1_bits(number):
    number_in_base_2 = bin(number)
    count = 0
    for bit in number_in_base_2:
        if bit == "1":
            count += 1
    return count

print("Enter the number to compute the number of 1 bits of:")
number = int(input())
print("The given number has", count_1_bits(number), "bits with the value of 1.")