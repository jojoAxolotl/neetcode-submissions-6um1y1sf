# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def divide(in_left, in_right, post_left, post_right):
            if in_left > in_right:
                return None
            
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            index = idx_map[root_val]
            left_size = index - in_left
            
            root.left = divide(in_left, index - 1, post_left, post_left + left_size - 1)
            root.right = divide(index + 1, in_right, post_left + left_size, post_right - 1)
            
            return root

        return divide(0, len(inorder) - 1, 0, len(postorder) - 1)