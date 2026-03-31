"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        def dfs(old_node):
            if old_node in old_to_new:
                return old_to_new[old_node]
            copy = Node(old_node.val)
            old_to_new[old_node] = copy
            for neighbor in old_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
