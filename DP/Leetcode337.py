# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root) -> int:
        memo=dict()
        return self.helper(root,memo)

    def helper(self,start,memo):
        #exit case
        if not start:
            return 0

        if memo.get(start):
            return memo[start]
        # include start
        include = start.val
        # exlude start
        exclude = 0
        if start.left:
            include+=self.helper(start.left.left,memo)+self.helper(start.left.right,memo)
            exclude+=self.helper(start.left,memo)
        if start.right:
            include += self.helper(start.right.left,memo) + self.helper(start.right.right,memo)
            exclude += self.helper(start.right,memo)

        memo[start]=max(exclude,include)
        return memo[start]


