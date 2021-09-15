class Solution:
    def lexicalOrder(self, n: int):
        res=list()
        self.dfs(res,n,0)
        return res

    def dfs(self,res,n,start):
        i=1 if start==0 else 0
        while i<10:
            add=start*10+i
            if add>n:
                return
            res.append(add)
            self.dfs(res,n,add)
            i+=1
        return

if __name__ == '__main__':
    sol=Solution()
    n=13
    print(sol.lexicalOrder(n))