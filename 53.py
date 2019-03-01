

nums = [-2,1,-3,4,-1,2,1,-5,4]


res = -9999999
def solve(nums, idx):
    if len(nums) == 0:
        return 0

    if idx == 0:
        return 1

    temp = max(solve(nums, idx - 1) + nums[idx], nums[idx])
    global res
    if res < temp :
        res = temp
    return temp

solve(nums, len(nums) - 1)
print(res)


class Solution:

    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]


        arr = [None] * len(nums)
        arr[0] = nums[0]

        res = arr[0]
        for i in range(1, len(nums)):
            arr[i] = max(arr[i - 1] + nums[i], nums[i])
            if arr[i] > res:
                res = arr[i]


        return res
