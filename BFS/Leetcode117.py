"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if root is None:
            return
        q=[root]

        while q:
            size=len(q)
            for s in range(size):
                cur=q[0]
                q.pop(0)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            for i in range(0,len(q)-1):
                q[i].next=q[i+1]
        return root
