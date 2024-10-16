fib_list = []

def add_fib(n: int):
    global fib_list
    if n < 0:
        return
    if n >= 1:
        fib_list.append(0)
    if n >= 2:
        fib_list.append(1)
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

# maybe ignore 0 here and print one more at the end

n = 10

add_fib(n)
print("First", n, "numbers in the fibonacci string:", fib_list)
