from math import sqrt


def fraqs(start, seq):
    l = reversed(seq)
    n = 0
    d = 1
    for i in l:
        n += i * d
        (n, d) = (d, n)
    n += d * start
    return (n, d)


def periodic_root(number):
    if int(sqrt(number))**2 == number:
        return None
    seq = []
    a = int(sqrt(number))
    initial = a
    d = -a

    n = a
    d = number - abs(d)**2

    a = 0
    while n - d >= -initial:
        a += 1
        n -= d
    seq.append(a)

    while True:
        f = fraqs(initial, seq)

        if f[0]**2 - number * f[1]**2 == 1:
            return number, f

        oldn = n
        (n, d) = (d, n)

        d = number - abs(d)**2
        if n > 1:
            d = int(d / n)
        n = -oldn

        a = 0
        while n - d >= -initial:
            a += 1
            n -= d
        seq.append(a)


i = 0
l = []
while i <= 1000:
    i += 1
    if int(sqrt(i))**2 == i: continue
    l.append(periodic_root(i))

print(max(l, key=lambda x: x[1][0]))




