class WordNode:
    def __init__(self):
        self.children = {}
        self.is_end= False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        # We use a helper function to allow recursion for the '.' wildcard
        def dfs(index, current_node):
            curr = current_node
            
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # Try every possible child path
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False # No path worked
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
