from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(x, y):
            # print("x", x)
            # print("y", y)
            # print("x + y: ", x + y)
            # print("y + x: ", y + x)
            
            if int(x + y) > int(y + x):
                return -1 # x 要排在比較前面
            else:
                return 1 # y 要排在比較後面
        nums = sorted(nums, key = cmp_to_key(compare)) # 重點！
        # cmp(x,y) 函數用於比較2個對象，
        # 如果 x < y (在list裡面放x放在y前面) 返回 -1, 
        # 如果 x == y 返回 0, 
        # 如果 x > y (在list裡面放x放在y後面) 返回 1。
        return str(int("".join(nums)))

