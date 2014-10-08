from math import sqrt


def periodic_root(number):
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
    print("a = ", a, "frac = ", n, "/", d)

    oldn = n
    (n, d) = (d, n)

    d = number - abs(d)**2
    if n > 1:
        d = int(d / n)
    n = -oldn

    a = 0
    while n - d > -initial:
        a += 1
        n -= d
    print("a = ", a, "frac = ", n, "/", d)

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
    print("a = ", a, "frac = ", n, "/", d)



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
    print("a = ", a, "frac = ", n, "/", d)


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
    print("a = ", a, "frac = ", n, "/", d)




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
    print("a = ", a, "frac = ", n, "/", d)




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
    print("a = ", a, "frac = ", n, "/", d)



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
    print("a = ", a, "frac = ", n, "/", d)



print(periodic_root(2))