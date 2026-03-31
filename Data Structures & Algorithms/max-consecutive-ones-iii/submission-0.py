class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        cur = 0 # current amount of 0 
        for r in range(len(nums)):
            if nums[r] == 0:
                if cur < k:
                    cur += 1
                else: # cur = k
                    while nums[l] != 0:
                        l += 1
                    l += 1
            res = max(res, r-l+1)    
        return res
