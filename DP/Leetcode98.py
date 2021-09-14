# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    t = 2 ** 32
    d = -2 ** 31 - 1

    def isValidBST(self, root) -> bool:
        return self.isValid(root, self.t, self.d)

    def isValid(self, root, top, bottom):
        if not root:
            return True
        if root.val >= top or root.val <= bottom:
            return False

        if root.left and root.val <= root.left.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValid(root.left, root.val, bottom) and self.isValid(root.right, top, root.val)
