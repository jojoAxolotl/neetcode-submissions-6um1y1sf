class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        val_amount = defaultdict(int)
        for num in nums:
            val_amount[num] += 1
        print(val_amount)
        for val1 in list(val_amount.keys()):
            val_amount[val1] -= 1
            for val2 in list(val_amount.keys()):
                if val_amount[val2] == 0:
                    continue 
                val_amount[val2] -= 1
                val3 = -(val1+val2)
                if (val3 in val_amount) and (val_amount[val3] != 0):
                    print("val1: ", val1)
                    print("val2: ", val2)
                    print("val3: ", val3)
                    print("val_amount: ", val_amount)
                    res.add(tuple(sorted([val1, val2, val3])))
                val_amount[val2] += 1
            val_amount[val1] += 1
        return [list(item) for item in list(res)]
