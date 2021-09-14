# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        return self.dfs(root,targetSum)

    def dfs(self,root,target):
        # exit case
        if not root and target==0:
            return True
        elif root:
            return self.dfs(root.left,target-root.val) or self.dfs(root.right,target-root.val)
        else:
            return False

