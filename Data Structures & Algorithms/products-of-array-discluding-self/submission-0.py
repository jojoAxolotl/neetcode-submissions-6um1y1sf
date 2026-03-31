class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        temp_prefix = 1
        for i in range(len(nums)):
            temp_prefix = temp_prefix * nums[i]
            prefix[i] = temp_prefix
        suffix = [0]*len(nums)
        temp_suffix = 1
        for i in range(len(nums)-1, -1, -1):
            temp_suffix = temp_suffix * nums[i]
            suffix[i] = temp_suffix
        res = [0]*len(nums)
        # for out of index
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, len(nums)-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res 

        