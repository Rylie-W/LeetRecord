# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        def dfs(cur):
            left = dfs(cur.left) if cur.left is not None else None
            right = dfs(cur.right) if cur.right is not None else None
            res = [cur.val, cur.val]
            if left is not None and left[0] >= 0:
                res[0] += left[0]
            if right is not None and right[0] >= 0:
                res[0] += right[0]

            res[1] = max(res[0],
                         max(left[1] if left is not None else cur.val,
                             right[1] if right is not None else cur.val))
            return res

        return dfs(root)[1]
