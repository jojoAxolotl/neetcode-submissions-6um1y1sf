# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            l = []
            length = len(q)
            while length > 0:
                cur = q.popleft()
                if cur:
                    l.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                length -= 1
            if l:
                res.append(l) 
        return res
