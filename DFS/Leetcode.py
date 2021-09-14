# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        res=list()
        self.dfs([],res,root,targetSum)
        return res

    def dfs(self,path,res,root,target):
        if not root.left and not root.right:
            if root.val==target:
                res.append(path+[target])
            return

        if root.left:
            self.dfs(path+[root.val],res,root.left,target-root.val)
        if root.right:
            self.dfs(path+[root.val],res,root.right,target-root.val)

        return


