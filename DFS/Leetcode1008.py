# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder) :
        def dfs(preorder):
            if len(preorder)==0:
                return None

            cur=TreeNode(preorder[0])
            i=1
            while i<len(preorder) and preorder[i]<preorder[0]:
                i+=1

            cur.left=dfs(preorder[1:i])
            cur.right=dfs(preorder[i:])
            return cur

        return dfs(preorder)