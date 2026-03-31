class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        print(set_nums)
        lcs = 0
        for i in range(len(nums)):
            if nums[i]-1 not in set_nums:
                num = nums[i]
                tmp_lcs = 1
                while num+1 in set_nums:
                    num += 1
                    tmp_lcs += 1
                if tmp_lcs > lcs:
                    lcs = tmp_lcs
        return lcs
