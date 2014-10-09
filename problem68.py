from itertools import permutations


def gon5():
    start = set(list(range(1, 11)))
    for i in permutations(start, 3):
        s = sum(i)
        r1 = start.copy() - set(i)
        for j in permutations(r1, 2):
            if sum(j) + i[2] != s:
                continue
            r2 = r1.copy() - set(j)
            for k in permutations(r2, 2):
                if sum(k) + j[1] != s:
                    continue
                r3 = r2.copy() - set(k)
                for l in permutations(r3, 2):
                    if sum(l) + k[1] != s:
                        continue
                    (r4,) = r3.copy() - set(l)
                    if r4 + l[1] + i[1] != s:
                        continue
                    yield i, (j[0], i[2], j[1]), (k[0], j[1], k[1]), (l[0], k[1], l[1]), (r4, l[1], i[1])


def tuple_to_str(t):
    s = ''
    for i in t:
        s += str(i)
    return s


def rotate(l, n):
    return l[n:] + l[:n]


l = []
for i in gon5():
    m = min(map(lambda x: x[0], i))
    while i[0][0] != m:
        i = rotate(i, 1)
    l.append(tuple_to_str(i[0]) + tuple_to_str(i[1]) + \
            tuple_to_str(i[2]) + tuple_to_str(i[3]) + tuple_to_str(i[4]))

l = list(map(lambda x: int(x), filter(lambda x: len(x) == 16, l)))

print(max(l))

