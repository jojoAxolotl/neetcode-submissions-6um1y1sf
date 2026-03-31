class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": # edge case
            return 0
        res = 1
        chars = set()
        pt1, pt2 = 0, 1
        chars.add(s[0])
        while pt2 < len(s):
            if s[pt2] in chars:
                while s[pt1] != s[pt2]:
                    chars.remove(s[pt1])
                    pt1 += 1
                pt1 += 1
            else:
                chars.add(s[pt2])
                res = max(res,pt2-pt1+1)
            pt2 += 1
        return res
