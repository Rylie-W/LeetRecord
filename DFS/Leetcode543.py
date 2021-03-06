# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res=0

        def dfs(root):
            nonlocal res
            if root is None:
                return 0

            left=dfs(root.left)
            right=dfs(root.right)
            res=max(res,left+right+1)
            return max(left,right)+1

        dfs(root)
        return res