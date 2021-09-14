"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') :
        if not root:
            return []

        q=[root]
        res=[[root.val]]

        while q:
            size=len(q)
            layer=list()
            for i in range(size):
                c=q[0]
                q.pop(0)

                if c.children:
                    for child in c.children:
                        layer.append(child.val)
                        q.append(child)
            if len(layer)>0:
                res.append(layer)

        return res

