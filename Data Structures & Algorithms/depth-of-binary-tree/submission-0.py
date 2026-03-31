# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        res = 0
        while q:
            res += 1
            tmp_q = collections.deque()
            while q:
                tmp_n = q.popleft()
                if tmp_n.left:
                    tmp_q.append(tmp_n.left)
                if tmp_n.right:
                    tmp_q.append(tmp_n.right)
            q = tmp_q
        return res
