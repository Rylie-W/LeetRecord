# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:
        if not root:
            return False

        memo=dict()
        q=[root]

        while q:
            size=len(q)
            for s in range(size):
                cur=q[0]
                q.pop(0)

                if memo.get(cur.val):
                    memo[cur.val].add(cur)
                else:
                    memo[cur.val]={cur}

                t=k-cur.val
                if t==cur.val:
                    continue
                elif t<cur.val:
                    if self.find(cur.left,t,memo,cur):
                        return True
                else:
                    if self.find(cur.right,t,memo,cur):
                        return True

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return False




    def find(self,root,target,memo,mark):
        if memo.get(target):
            for i in memo[target]:
                if i!=mark:
                    return True

        if not root:
            return False

        if target==root.val:
            return True

        if memo.get(root.val):
            memo[root.val].add(root)
        else:
            memo[root.val]={root}
        return self.find(root.left,target,memo,mark) if target<root.val else self.find(root.right,target,memo,mark)

