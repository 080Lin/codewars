def f(n):
    if n == 0:
        return 0
    d = n % 10
    m = n // 10
    return 10 * f(m) + m + sum(str(10 * m + i).count('9') for i in range(d))


def count_nines(n):
    return f(n + 1)

print(count_nines(5675842))

b = 998634
mn = b % 10
mb = b // 10
print(mn, mb)