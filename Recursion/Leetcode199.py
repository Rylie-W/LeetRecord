# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        left=self.rightSideView(root.left)
        right=self.rightSideView(root.right)

        if len(right)>=len(left):
            return [root.val]+right

        return [root.val]+right+left[len(right):]

    # bfs
    # res=[]
    # q=[root]
    #
    # while q:
    #     size=len(q)
    #
    #     res.append(q[-1].val)
    #
    #     for s in range(size):
    #         cur=q[0]
    #         q.pop(0)
    #
    #         if cur.left:
    #             q.append(cur.left)
    #         if cur.right:
    #             q.append(cur.right)
    # return res
