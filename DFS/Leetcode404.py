# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(root):
            if root is None:
                return 0

            if root.left is not None and root.left.left is None and root.left.right is None:
                return root.left.val+dfs(root.right)

            return dfs(root.left)+dfs(root.right)

        return dfs(root)