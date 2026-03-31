class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        s = list(s)

        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] == "#":
                    return 0
                elif int(s[i-1]) > 2 or s[i-1] == "0":
                    return 0
                else:
                    s[i] = "#"
                    s[i-1] = "#"

        a = [0] * len(s) # amount
        a[0] = 1
        for i in range(1, len(s)):
            if s[i] == "#":
                a[i]=a[i-1]
            elif ((s[i-1] == "1" or 
                (s[i-1] == "2" and 1 <= int(s[i]) <= 6))):
                if i-2 >= 0:
                    a[i] = a[i-1] + a[i-2]
                else:
                    a[i] = a[i-1] + 1
            else:
                a[i]=a[i-1]
        return a[len(s)-1]