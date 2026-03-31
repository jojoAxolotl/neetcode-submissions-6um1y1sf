class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # 初始化結果、當前最大值和當前最小值
        res = max_so_far = min_so_far = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # 如果當前是負數，最大值和最小值會互換
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # 關鍵：當前最大值是 (當前值) 和 (之前最大值 * 當前值) 中的較大者
            # 這自動處理了遇到 0 時重置的情況
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            
            # 更新全局最大值
            res = max(res, max_so_far)
            
        return res