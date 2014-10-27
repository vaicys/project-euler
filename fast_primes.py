def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * int(n / 3)
    sieve[0] = False
    for i in range(int(int(n ** 0.5) / 3 + 1)):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = [False] * ((n / 6 - (k * k) / 6 - 1) / k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = [False] * int(
                ((n / 6 - (k * k + 4 * k - 2 * k * (i & 1)) / 6 - 1) / k + 1))
        return [2, 3] + [3 * i + 1 | 1 for i in range(1, int(n / 3 - correction)) if sieve[i]]


primes = rwh_primes2(1000000)
print(primes[0:100])