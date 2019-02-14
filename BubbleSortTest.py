


def bubbleSort(theList):
    for i in range(len(theList)):           # 总共有多少个数需要进行排序
        for j in range(len(theList) - 1):   # 每一轮排序需要经历多少次比较
            if theList[j] > theList[j + 1]:
                temp = theList[j]
                theList[j] = theList[j + 1]
                theList[j + 1] = temp

    return theList

print(bubbleSort([2, 8, 1, 45, 6, 3, 7, 9]))