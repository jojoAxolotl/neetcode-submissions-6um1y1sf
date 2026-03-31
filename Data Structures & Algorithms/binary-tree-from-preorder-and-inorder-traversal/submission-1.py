# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # 只建立一次 map
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left, in_right): # by 2 pointers
            nonlocal pre_idx
            if in_left > in_right: 
                return None

            val = preorder[pre_idx]
            root = TreeNode(val)
            pre_idx += 1

            # 利用 map 快速分割左右子樹邊界
            idx = inorder_map[val]

            # 遞迴構建
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)
