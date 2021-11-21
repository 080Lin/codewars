def sum_fibs(n):
    num_1, num_2 = 0, 1
    fib_list = []
    for i in range(n + 1):
        fib_list.append(num_1)
        num_3 = num_1
        num_1 = num_2
        num_2 += num_3
    return sum([num for num in fib_list if num % 2 == 0])
    

print(sum_fibs(10))