# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        return self.recurse(nums,0,len(nums)-1)

    def recurse(self,nums,start,end):
        if end<start:
            return None

        mid=int(start+(end-start)/2)
        root=TreeNode(val=nums[mid],left=self.recurse(nums,start,mid-1),right=self.recurse(nums,mid+1,end))
        return root

    def forward(self,root):
        if not root:
            return
        print(root.val)
        self.forward(root.left)
        self.forward(root.right)

if __name__ == '__main__':
    sol=Solution()
    nums = [-10, -3, 0, 5, 9]
    root=sol.sortedArrayToBST(nums)
    sol.forward(root)