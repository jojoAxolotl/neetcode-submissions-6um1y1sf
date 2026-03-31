class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r:
                return nums[l]
            if r-l == 1:
                return (nums[l] if nums[l]<nums[r] else nums[r])
            m = l + (r-l)//2
            if nums[m]>nums[l]>nums[r]:
                l = m+1
                # r = r
            elif nums[l]>nums[r]>nums[m]:
                l = l+1
                r = m
            elif nums[r]>nums[m]>nums[l]:
                # l = l
                r = m-1
            else:
                print("ERROR")
                return 0
        