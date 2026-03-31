class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for i in range(len(nums)):
            if nums[i] in exist:
                return True
            else:
                exist.add(nums[i])
        return False
