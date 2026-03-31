class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[idx]):
                return False

            # ------ backtracking ------
            temp = board[r][c]
            board[r][c] = "#"

            res = (dfs(r + 1, c, idx + 1) or
                   dfs(r - 1, c, idx + 1) or
                   dfs(r, c + 1, idx + 1) or
                   dfs(r, c - 1, idx + 1))

            board[r][c] = temp  # 恢復現場（回溯的關鍵）
            # --------------------------

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
