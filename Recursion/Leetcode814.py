# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root):
        #exit case
        if root==None:
            return root

        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)

        if not (root.left or root.right or root.val==1):
            return None
        else:
            return root