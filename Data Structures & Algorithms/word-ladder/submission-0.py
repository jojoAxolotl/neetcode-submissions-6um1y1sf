class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        
        # create adjacent table
        wordList.append(beginWord)
        adj_table = {}
        n, m = len(wordList), len(beginWord)

        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern in adj_table:
                    adj_table[pattern].append(word)
                else:
                    adj_table[pattern] = [word]
        
        # find shortest path by BFS
        visit = set()
        visit.add(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1
        
        while q:
            for i in range(len(q)): # means each layer
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(m):
                    pattern = word[:i] + "*" + word[i+1:]
                    for adj in adj_table[pattern]:
                        if adj not in visit:
                            visit.add(adj)
                            q.append(adj)
            res += 1 # search next layer
        return 0
