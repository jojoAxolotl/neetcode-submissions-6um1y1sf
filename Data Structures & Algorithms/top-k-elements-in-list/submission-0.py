class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        l = sorted(list(d.items()), key = lambda x:x[1],reverse = True)[:k]
        for i in range(len(l)):
            l[i] = l[i][0]
        return l
