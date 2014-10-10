def gcd(n, m):
    if n < m:
        (n, m) = (m, n)
    while True:
        q = int(n / m)
        r = n % m
        if r == 0:
            return m
        (n, m) = (m, r)


print(gcd(1, 9))
