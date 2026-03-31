class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            goal_v = target - nums[i]
            if goal_v in d:
                return [d[goal_v], i]
            else:
                d[nums[i]] = i
# Time Complexity: O(n)
# Space complexity: O(n)
