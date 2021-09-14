class TreeNode:
    def __init__(self,val,leaves):
        self.val=val
        self.leaves=leaves

class Solution:
    def findWords(self, board, words):
        pass
    def dfs(self):
        pass

    def genTree(self,words,val):
        if words==None or len(words)==0:
            return None
        root=TreeNode(val=val,leaves=dict())
        words.sort(key=lambda a:a[0])
        left=right=0
        while right<len(words):
            c=words[right]
            right+=1

            if c[0]!=words[left][0]:
                root.leaves[words[left][0]]=self.genTree(self.removeFirstChar(words[left:right-1]),words[left][0])
                left=right-1
            elif right==len(words):
                root.leaves[words[left][0]] = self.genTree(self.removeFirstChar(words[left:right]), words[left][0])
        return root

    def printTree(self,root):
        if root==None:
            print("===")
            return
        print(root.val)
        for key in root.leaves.keys():
            self.printTree(root.leaves.get(key))

    def removeFirstChar(self,words):
        res=list()
        for i in words:
            if i[1:]!="":
                res.append(i[1:])
        return res
if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    sol=Solution()
    root=sol.genTree(words,None)
    sol.printTree(root)

