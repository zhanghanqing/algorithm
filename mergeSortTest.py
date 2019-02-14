import random

lyst = []
for i in range(20):
    lyst.append(random.randint(1,100))


def mergeSort(lyst, l, h):

    if l < h:
        m = (l + h) // 2
        mergeSort(lyst, l, m)
        mergeSort(lyst, m + 1, h)
        merge(lyst, l, m, h)

def merge(lyst, l, m, r):
    li = l
    ri = m + 1

    buffer = [None] * len(lyst)
    print(buffer)

    for i in range(l, r + 1):
        if li > m:
            buffer[i] = lyst[ri]
            ri += 1
        elif ri > r:
            buffer[i] = lyst[li]
            li += 1
        elif lyst[ri] > lyst[li]:
            buffer[i] = lyst[li]
            li += 1
        else:
            buffer[i] = lyst[ri]
            ri += 1

    for i in range(l, r + 1):
        lyst[i] = buffer[i]


mergeSort(lyst, 0, len(lyst) - 1)
print(lyst)

