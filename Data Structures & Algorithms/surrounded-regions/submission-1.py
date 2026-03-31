class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        print("ROWS:", ROWS)
        print("COLS:", COLS)

        def dfs(r, c):
            print("r: ", r)
            print("c: ", c)
            if board[r][c] == "O":
                print(r, c)
                board[r][c] = "S"
                print(board)
                if r+1 < ROWS: dfs(r+1, c)
                if r-1 >= 0: dfs(r-1, c)
                if c+1 < COLS: dfs(r, c+1)
                if c-1 >= 0: dfs(r, c-1)
        
        # up down edge
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS-1, i)
        # left right edge
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS-1)
                
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
