class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 如果輸入為空，直接返回
        if not intervals:
            return []

        # 2. 按照區間的起始位置進行排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 3. 如果 merged 為空，或者當前區間與上一區間不重疊
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 4. 有重疊，合併區間：更新前一個區間的結束位置
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
