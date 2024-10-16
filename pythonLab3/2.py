def is_prime(n: int):
    if n==2:
        return True
    if n == 0 or n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def keep_prime_numbers(number_list: []):
    prime_numbers = []
    for number in number_list:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

initial_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Initial list:", initial_list)
print("List with prime numbers from initial list:", keep_prime_numbers(initial_list))
