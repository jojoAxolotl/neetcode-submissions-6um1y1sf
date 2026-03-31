# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == []: # end case
            return None

        inorder_map = dict()
        for idx, value in enumerate(inorder):
            inorder_map[value] = idx

        value = preorder[0]
        length = len(preorder)

        cur = TreeNode(value)
        idx = inorder_map.get(value)

        cur.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        cur.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return cur

        