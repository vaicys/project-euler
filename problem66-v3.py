from math import sqrt


def is_square(n):
    return int(sqrt(n))**2 == n


def diophantine(limit):
    seq = []
    d = 1
    while d < limit:
        d += 1
        if is_square(d):
            continue
        x = 2
        while True:
            y = sqrt((1 - x**2) / -d)
            if int(y) == y:
                seq.append((d, x))
                break
            x += 1

    return seq


print(diophantine(100 + 1))