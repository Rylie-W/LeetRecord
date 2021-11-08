# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Utility.TreeHelper as TreeHelper
class Solution:
    def convertBST(self, root):
        sum=0
        def dfs(root):
            if root is None:
                return 0
            dfs(root.right)
            nonlocal sum
            root.val+=sum
            sum=root.val
            dfs(root.left)
            return root

        return dfs(root)

if __name__ == '__main__':
    sol=Solution()
    tree=[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root=TreeHelper.generateTrre(tree)
    sol.convertBST(root)