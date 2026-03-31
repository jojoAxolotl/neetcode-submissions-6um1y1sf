class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c): # 用於淹沒
            # 檢查邊界以及是否為水
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == "0"):
                return
            
            # 將走過的陸地變成 "0" (淹沒島嶼)，避免重複計算
            grid[r][c] = "0"
            
            # 向四個方向探索
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # 發現一個新島嶼的前端
                    res += 1
                    # 當發現一塊陸地（"1"）時，就啟動 DFS 「淹沒」 整個島嶼。
                    dfs(r, c) 
                    
        return res
