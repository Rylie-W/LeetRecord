# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Utility.TreeHelper as TreeHelper
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        count=0
        def recurse(root):
            if root is None:
                return
            nonlocal count
            left=recurse(root.left)
            if left is not None:
                return left
            count+=1
            if count==k:
                return root.val
            right=recurse(root.right)
            if right is not None:
                return right
        return recurse(root)

if __name__ == '__main__':
    sol=Solution()
    root = [5, 3, 6, 2, 4,None, None, 1]
    print(sol.kthSmallest(TreeHelper.generateTrre(root),3))
