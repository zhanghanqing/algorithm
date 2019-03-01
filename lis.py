nums = [10,9,2,5,3,7,101,18]

# example [2,3,7,101] length is 4
def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return 1

    arr = [None] * len(nums)
    arr[0] = 1

    res = arr[0]
    for i in range(1, len(nums)):
        arr[i] = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                arr[i] = max(arr[j] + 1, arr[i])

        if arr[i] > res:
            res = arr[i]

    return res

