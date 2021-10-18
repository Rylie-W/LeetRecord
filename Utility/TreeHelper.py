class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrre(tree):
    size=1
    p=0
    q=[]
    root=None
    while p<len(tree):
        for i in range(size):
            if p>=len(tree):
                break
            # pre=int((p-1)/2)
            cur=TreeNode(val=tree[p]) if tree[p] is not None else None
            if p==0:
                root=cur
            if len(q)>0:
                pre=q[0]
                if p%2==1:
                    pre.left=cur
                else:
                    pre.right=cur
                    q.pop(0)
            p+=1
            if cur is not None:
                q.append(cur)
        size*=2
    return root
