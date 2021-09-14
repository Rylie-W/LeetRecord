# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.bfs(root)

    def bfs(self,root):
        q=[root]
        memo=[root.val]
        res=1

        while q:
            size=len(q)

            for s in range(size):
                c=q[0]
                maxv=memo[0]
                q.pop(0)
                memo.pop(0)

                if c.left:
                    if c.left.val>=maxv:
                        res+=1
                        q.append(c.left)
                        memo.append(c.left.val)
                    else:
                        q.append(c.left)
                        memo.append(maxv)

                if c.right:
                    if c.right.val>=maxv:
                        res+=1
                        q.append(c.right)
                        memo.append(c.right.val)
                    else:
                        q.append(c.right)
                        memo.append(maxv)

        return res


