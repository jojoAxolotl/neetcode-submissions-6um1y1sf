class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        goal = Counter(t)
        required = len(goal) # 有多少種字元需要達標
        
        window_counts = defaultdict(int)
        formed = 0 # 目前有多少種字元已達標
        
        l, r = 0, 0
        # 紀錄最小視窗的 (長度, 左邊界, 右邊界) 
        # 把三個數值打包成一個 Tuple (元組)。在後續程式碼中，透過 ans[0]、ans[1]、ans[2] 來分別存取這三個值。
        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_counts[char] += 1

            if char in goal and window_counts[char] == goal[char]:
                formed += 1

            # 當視窗包含所有 t 中的字元時，嘗試收縮左邊界
            while l <= r and formed == required:
                char = s[l]
                # 更新目前找到的最小值
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[char] -= 1
                if char in goal and window_counts[char] < goal[char]:
                    formed -= 1
                l += 1    
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

# T: O(n+m)
# n is the length of the string s
# m is the total number of unique characters in the strings t and s.

# S: O(m)