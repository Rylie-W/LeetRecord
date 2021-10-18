# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        if root is None:
            return False

        memo=dict()
        def finddepth(root,depth,target,pre):
            if root is None:
                return None

            if root.val==target:
                return (depth,pre)

            memo[root.val]=(depth,pre)
            left=finddepth(root.left,depth+1,target,root)
            right=finddepth(root.right,depth+1,target,root)
            return left if left is not None else right

        x=finddepth(root,0,x,None)
        y=finddepth(root,0,y,None) if memo.get(y) is None else memo[y]

        return True if (x[0]==y[0] and x[1]!=y[1]) else False
