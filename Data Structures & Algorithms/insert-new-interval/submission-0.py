class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        first = True
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if first:
                    res.append(newInterval)
                    first = False
                res.append(interval)
            else:
                if first:
                    res.append(newInterval)
                    first = False
                if res[-1][0] > interval[0]:
                    res[-1][0] = interval[0]
                    newInterval[0] = interval[0]
                if res[-1][1] < interval[1]:
                    res[-1][1] = interval[1]
                    newInterval[1] = interval[1]
        if first:
            res.append(newInterval)
            first = False
        return res
