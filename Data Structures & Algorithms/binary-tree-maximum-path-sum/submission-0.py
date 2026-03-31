# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        # return max path sum without split
        def dfs(node):
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # compute max path sum WITH split
            current_sum = node.val + leftMax + rightMax
            res[0] = max(res[0], current_sum)

            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

        