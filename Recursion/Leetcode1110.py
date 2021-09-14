# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        to_delete=set(to_delete)
        res=list()
        def recurse(root,flag,pre,left):
            if root is None:
                return

            if root.val not in to_delete:
                if flag:
                    res.append(root)
                recurse(root.left,False,root,True)
                recurse(root.right,False,root,False)
                return

            else:
                if left and not (pre is None):
                    pre.left=None
                elif not(pre is None):
                    pre.right=None
                recurse(root.left,True,None,True)
                recurse(root.right,True,None,False)
                return


        recurse(root,True,None,False)
        return res

