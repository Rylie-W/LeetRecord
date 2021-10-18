# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Utinity.TreeGenerator as Treegenerator
class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        res=0
        memo=set()
        def dfs(root,target):
            nonlocal res
            if root is None:
                # if target==0:
                #     res+=1
                return

            if root.val==target:
                res+=1
            if root.left not in memo:
                dfs(root.left,targetSum)
                memo.add(root.left)
            if root.right not in memo:
                dfs(root.right,targetSum)
                memo.add(root.right)

            target=target-root.val
            dfs(root.left,target)
            dfs(root.right,target)

        dfs(root,targetSum)
        return res

if __name__ == '__main__':
    sol=Solution()
    tree=[1,None,2,None,3,None,4,None,5]
    root=Treegenerator.generateTrre(tree)
    targetSum = 3
    print(sol.pathSum(root,targetSum))