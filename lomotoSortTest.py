import random

lyst = []
for i in range(20):
    lyst.append(random.randint(1,100))

def quick(ls, p, r):
    if p < r:
        q = partition(ls, p, r)
        quick(ls, p, q - 1)
        quick(ls, q + 1, r)

def partition(ls, low, high):
    key = ls[high]
    i = low - 1                     # i 指向的数据永远小于或者等于key值，所以第一次在不知道ls[i] 是否 <= key的情况下往后退一步
                                    # 如果 i 最初指向 low, 例子 [1, 12, 3, 4, 5] => [12 , 1]

    for j in range(low, high):
        if ls[j] < key:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]    # 当ls[j] <= key值时，ls[i]和ls[j]会重复相互赋值

    ls[i + 1], ls[high] = ls[high], ls[i + 1]
    return i + 1


quick(lyst, 0, len(lyst) - 1)
print(lyst)