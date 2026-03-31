class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Max size = 26
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            res = max(res, r - l + 1)
        return res
