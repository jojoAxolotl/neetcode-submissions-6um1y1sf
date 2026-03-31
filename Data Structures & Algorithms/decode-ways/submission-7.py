class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0": return 0
        s = list(s)
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] not in "12":
                    return 0
                else:
                    s[i], s[i-1] = "#", "#"

        a = [0] * len(s)
        a[0] = 1        
        for i in range(1, len(s)):
             # 11-19 and 21-26
            is_two_digit_valid = (s[i-1] == "1" and s[i] != "#") or \
                                 (s[i-1] == "2" and s[i] in "123456")
            
            if is_two_digit_valid:
                a[i] = a[i-1] + (a[i-2] if i >= 2 else 1)
            else:
                a[i] = a[i-1]
                
        return a[-1]
