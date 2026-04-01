import random
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate

# Time complexity: O(n)
# Space complexity: O(1)