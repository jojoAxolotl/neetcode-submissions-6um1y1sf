class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i: int, j: int, visited: set):
            visited.add((i, j))

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < ROWS and 0 <= y < COLS and (x, y) not in visited and heights[x][y] >= heights[i][j]:
                    dfs(x, y, visited)

        for i in range(ROWS):
            dfs(i, 0, pacific)
            dfs(i, COLS - 1, atlantic)

        for j in range(COLS):
            dfs(0, j, pacific)
            dfs(ROWS - 1, j, atlantic)

        return list(pacific & atlantic)
