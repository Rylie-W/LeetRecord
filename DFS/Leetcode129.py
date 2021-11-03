# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def dfs(root,preVal,cur):
            val=preVal+cur.val
            if cur.right is None and cur.left is None:
                return [val] if not root else val

            res=[]
            left=dfs(False,val*10,cur.left) if cur.left is not None else None
            right=dfs(False,val*10,cur.right) if cur.right is not None else None
            res=res+left if left is not None else res
            res=res+right if right is not None else res
            return res if not root else sum(res)
        return dfs(True,0,root)