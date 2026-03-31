class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def str_to_dict(w):
            w_dict = dict()
            for i in range(len(w)):
                if w[i] in w_dict:
                    w_dict[w[i]] += 1
                else:
                    w_dict[w[i]] = 1
            return w_dict

        if str_to_dict(s) == str_to_dict(t):
            return True
        else:
            return False
            
        