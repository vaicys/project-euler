

primes = []


def is_prime(n):
    if n == 2:
        primes.append(2)
        return True
    if n % 2 == 0:
        return False
    for p in primes:
        if n % p == 0:
            return False
    primes.append(n)
    return True


def prime_fraqs(n):
    i = 0
    fraqs = []
    while n != 1:
        if n % primes[i] == 0:
            n = int(n/primes[i])
            fraqs.append(primes[i])
        else:
            i += 1
    return fraqs


def gcd(n, m):
    if n < m:
        (n, m) = (m, n)
    while True:
        r = n % m
        if r == 0:
            return m
        (n, m) = (m, r)


def phi_pk(p, k):
    return int(p**k * (p - 1) / p)


def totient_seq(limit):
    i = 2
    seq = dict()
    while i <= limit:
        if is_prime(i):
            count = i - 1
        else:
            fraqs = prime_fraqs(i)
            count = 1
            j = 0
            while j < len(fraqs):
                f = fraqs[j]
                c = fraqs.count(f)
                if c == 1:
                    count *= seq[f]
                else:
                    count *= phi_pk(f, c)
                while j < len(fraqs) and fraqs[j] == f:
                    j += 1
        seq[i] = count
        i += 1
    return seq


seq = totient_seq(1000000)
maximum = max(seq, key=lambda x: x/seq[x])
print(maximum)