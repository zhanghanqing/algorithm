def insertSort(lists):
    for i in range(1, len(lists)):      # i 待插入数据索引的范围
        j = i - 1                       # 总是从待插入数据的前一位索引进行比较
        key = lists[i]

        while lists[j] > key:
            lists[j + 1] = lists[j]     # 挪位置
            if j == 0:
                j -= 1                  # 因为有后面提到的"回退机制", 所以在J == 0时, 在break之前需要多"向前一步"
                break

            j -= 1                      # 待挪动的索引依次递减

        lists[j + 1] = key              # 待挪动的索引依次递减但之后一次递减后 已经不再满足lists[j] > key的条件, 所以需要将最后插入的位置回退一位
    return lists


ls = [2, 5, 1, 22, 11, 4, 7]
ls = [3,2,1]

print(insertSort(ls))
