# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        def recurse(start,end,memo):
            # if end==1 or start==end:
            #     memo[(start,end)]=[None]
            #     return [None]

            if memo.get((start,end)):
                return memo[(start,end)]

            res=[]
            for i in range(start,end):
                left=recurse(start,i,memo) if not(i==1 or start==i) else [-1]
                right=recurse(i+1,end,memo) if not(end==1 or i+1==end) else [-1]
                for l in left:
                    for r in right:
                        res.append(TreeNode(i,l if l!=-1 else None,r if r !=-1 else None))
            memo[(start,end)]=res
            return res
        memo=dict()
        recurse(1,n+1,memo)
        return memo[(1,n+1)]


