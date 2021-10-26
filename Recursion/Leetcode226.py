# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        def recurse(root):
            if root is None:
                return root

            left=recurse(root.left)
            right=recurse(root.right)
            root.left=right
            root.right=left
            return root
        return recurse(root)
