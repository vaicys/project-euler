

def eseq(n):
    seq = 0
    num = 0
    while n > 0:
        seq += 1
        if seq == 4:
            seq = 1
        if seq == 1 or seq == 3:
            yield 1
        else:
            num += 2
            yield num
        n -= 1


def fraqs(start, seq):
    l = reversed(seq)
    n = 0
    d = 1
    for i in l:
        n += i * d
        (n, d) = (d, n)
    n += d * start
    return (n, d)


#print(fraqs(1, [2, 2, 2]))
res = fraqs(2, list(eseq(100 - 1)))

print(sum([int(x) for x in str(res[0])]))

