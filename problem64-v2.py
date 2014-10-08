from math import sqrt


def periodic_root(number):
    if int(sqrt(number))**2 == number:
        return None
    seq = []
    fraq_seq = []
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
    fraq_seq.append((n, d))

    while True:

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
        fraq = (n, d)
        if fraq in fraq_seq:
            i = fraq_seq.index(fraq)
            return seq[i:-1]
        fraq_seq.append(fraq)


count = 0
for i in range(1, 10000 + 1):
    result = periodic_root(i)
    if result is not None:
        #print(i, result)
        if len(result) % 2 != 0:
            count += 1

print(count)