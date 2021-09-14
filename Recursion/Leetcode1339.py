# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:
        modulo = pow(10, 9) + 7
        q=[root]
        res=0
        memo = dict()
        total=self.getSum(root,memo)


        while q:
            size=len(q)

            for s in range(size):
                cur=q[0]
                q.pop(0)

                if cur.left:
                    temp=self.getSum(cur.left,memo)
                    res=max(res,temp*(total-temp))
                    q.append(cur.left)
                if cur.right:
                    temp = self.getSum(cur.right,memo)
                    res = max(res, temp * (total - temp))
                    q.append(cur.right)

        return res%modulo

    def getSum(self,root,memo):
        if (root) in memo:
            return memo[(root)]

        left=right=0
        if root.left:
            left=self.getSum(root.left,memo)
        if root.right:
            right=self.getSum(root.right,memo)

        memo[(root)]=left+right+root.val
        return left+right+root.val

    # def getSum(self,root):
    #     res=0
    #     q=[root]
    #
    #     while q:
    #         size=len(q)
    #
    #         for s in range(size):
    #             c=q[0]
    #             q.pop(0)
    #
    #             res+=c.val
    #             if c.left:
    #                 q.append(c.left)
    #             if c.right:
    #                 q.append(c.right)
    #     return res
