# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        res = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return res
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            cur = q.popleft()
            # print("cur.val: ", cur.val)
            # print("subRoot.val: ", subRoot.val)
            if cur.val == subRoot.val:
                if self.isSameTree(cur, subRoot):
                    return True
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        return False