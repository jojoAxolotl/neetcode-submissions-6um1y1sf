class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # 存儲完整的單詞，方便找到時直接提取

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie for words
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            curr_node = node.children[char]
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None 
            
            board[r][c] = "#"
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, curr_node)
            
            board[r][c] = char

            if not curr_node.children:
                node.children.pop(char)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return res
