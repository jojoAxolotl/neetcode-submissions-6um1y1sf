class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int) # uppercase English chars
        l = 0 # left ptr
        res = 0
        for r in range(len(s)): # right ptr
            cur_idx = ord(s[r]) - ord("A")
            mp[cur_idx] += 1
            if sum(mp.values()) - max(mp.values()) > k:
                mp[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
