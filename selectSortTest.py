def selectSort(lists):
    for i in range(len(lists) - 1):        # 有多少个"排位"需要被确定合适的数据
        minIndex = i
        for j in range(i + 1, len(lists)): # 为了确定一个排位需要进行多少次比较
            if lists[j] < lists[minIndex]:
                minIndex = j

        if minIndex != i:
            lists[i], lists[minIndex] = lists[minIndex], lists[i]

    return lists

print(selectSort([2,1,6,7,4,0,5,10,-1]))
print(selectSort([23, 21, 13, 34, 5, 100, 92, 37, 1, 6]))




















