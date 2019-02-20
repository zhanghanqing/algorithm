'''
首先使用暴力方法解决
n: 抢劫到了第几家店；
nums: 每一家店有多少钱

假设从最后一家金店开始从后往前抢劫

需要思考暴力搜索的决策， 在本问题中即为 "抢还是不抢"

时间复杂度分析，在每次的递归里有两种决策，分为抢一家店或者是不抢一家店
因为有N家店，每次都可以进行2次决策，所以总共可以进行的决策为2^n次
递归的时间复杂度分析，一般底数为每一层递归有多少计算量，指数为总共要进行多次层递归
'''


#暴力算法
def solve(idx, nums): # idx -> 抢劫第几家金店  nums -> 每一家店有多少钱
    if idx < 0:
        return 0
    return max((nums[idx] + solve(idx + 2, nums)), solve(idx + 1, nums))

def rob(nums):
    result = [-1] * len(nums)
    return solve(len(nums) - 1, nums, result)



# idx -> 抢劫第几家金店  nums -> 每一家店有多少钱
def rob(nums: 'List[int]') -> 'int':
    result = [-1] * len(nums)
    return solve(len(nums) - 1, nums, result)

"""
时间复杂度分析
因为每一种状态都只被搜索了一次 所以时间复杂度就是O(n)
记忆化搜索又被称之为“备忘录”

"""
# 记忆化搜索
def solve(idx, nums, result): # idx -> 抢劫第几家金店  nums -> 每一家店有多少钱
    if idx < 0:
        return 0

    if result[idx] >= 0:
        return result[idx]

    result[idx] = max((nums[idx] + solve(idx - 2, nums, result)), solve(idx - 1, nums, result))
    return result[idx]


# 动态规划
# 将递归改为递推, 有明确的搜索路径
def solve()










