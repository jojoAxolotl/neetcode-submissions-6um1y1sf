class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str_to_dict(s):
            d = {}
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
            return d
        # print(str_to_dict(strs[0])) # ok
        rst_dict = {}
        for s in strs:
            temp_d = str_to_dict(s)
            # print(temp_d.items())
            # print(tuple(sorted(list(temp_d.items()))))
            temp_key = tuple(sorted(list(temp_d.items())))
            if temp_key in rst_dict:
                rst_dict[temp_key].append(s)
            else:
                rst_dict[temp_key] = [s]
        # print(rst_dict)
        rst = list(rst_dict.values())
        # print(rst)
        return rst