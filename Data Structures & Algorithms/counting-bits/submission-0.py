class Solution:
    def countBits(self, n: int) -> List[int]:
        # 初始化長度為 n + 1 的陣列，初始值為 0
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i] 等於「去掉最右邊一個 1 之後的數字」的 1 個數再加 1
            ans[i] = ans[i & (i - 1)] + 1
        return ans
