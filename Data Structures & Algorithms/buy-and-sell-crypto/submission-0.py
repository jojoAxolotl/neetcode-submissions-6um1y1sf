class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        pt1, pt2 = 0, 0
        while pt2 < len(prices)-1:
            pt2 += 1
            if prices[pt2] < prices[pt1]:
                pt1 = pt2
                continue
            if prices[pt2] > prices[pt1]:
                res = max(res, prices[pt2]-prices[pt1])
        return res