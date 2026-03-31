class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True

            # --- 關鍵修改：處理重複數字 ---
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue

            if nums[m] >= nums[l]: # left side sorted
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False
