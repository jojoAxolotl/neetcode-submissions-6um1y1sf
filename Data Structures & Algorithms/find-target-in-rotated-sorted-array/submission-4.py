class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            # print("l: ", l)
            # print("r: ", r)
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if l == r or l+1 == r:
                return -1
            m = l + (r-l)//2
            # print("m: ", m)
            if nums[m] == target:
                return m
            # 「直覺型」寫法，核心是：什麼時候 target 在右邊？
            # 1. 右半邊是有序的，且 target 在範圍內
            # 2. 右半邊包含了旋轉點，且 target 剛好在那些比較大的數或比較小的數中
            if (nums[m] < nums[r] and nums[m] < target <= nums[r]) or \
            (nums[m] > nums[r] and (target > nums[m] or target <= nums[r])):
                l = m + 1
            else:
                r = m - 1
        return -1