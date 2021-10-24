import Utility.TreeHelper as TreeHelper
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
        memo=dict()
        def dfs(root,count):
            if root is None:
                memo[count]=memo[count]+1 if memo.get(count) is not None else 1
                return

            dfs(root.left,count+1)
            dfs(root.right,count+1)

        dfs(root,0)
        key=min(list(memo.keys()))
        return pow(2,key+1)-1-memo[key]

if __name__ == '__main__':
    sol=Solution()
    tree=TreeHelper.generateTrre([1,2,3,4,5,6,None])
    print(sol.countNodes(tree))


