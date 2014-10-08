from decimal import *
from math import sqrt

max_seq = 200
getcontext().prec = 1000


def periodic_root(number):
    j = Decimal(number).sqrt()
    seq = []
    while len(seq) < max_seq:
        i = int(j)
        j = 1 / (j - i)
        seq.append(i)
    return (number,) + find_repeating_seq(seq)


def find_repeating_seq(seq):
    i = 0
    l = len(seq)
    while i < max_seq / 2:
        j = i
        while True:
            j += 1
            if j >= l:
                break
            if seq[i] != seq[j]:
                continue
            # match found
            offset = j - i
            k = i
            match = True
            while k + offset * 2 < l:
                if seq[k:k+offset] != seq[k+offset:k+offset*2]:
                    match = False
                    break
                k += offset
            if not match or k == i:
                continue
            return offset, seq[i:i+offset]
        i += 1
    return None


# print(periodic_root(5))
count = 0
#for i in range(2, 10001):
for i in range(2, 10001):
    if sqrt(i) == int(sqrt(i)):
        continue
    result = periodic_root(i)
    if result[1] % 2 != 0:
        count += 1
    print(result)

print('Final count: ', count)

