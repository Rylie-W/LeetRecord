class Solution:
    def findIntegers(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 2
        dp=[0 for i in range(32)]
        dp[0]=1
        dp[1]=2
        for i in range(2,32):
            dp[i]=dp[i-1]+dp[i-2]
        n=bin(n)[2:]
        ans=1
        k=0
        while k<len(n):
            if n[-1-k]=='1':
                ans+=dp[k]
            k+=1
        return ans
        # return self.dfs(['',0],1,n)
        # return self.bfs(n)

    # def bfs(self,n):
        # if n==0:
        #     return 1
        # if n==1:
        #     return 2
        #
        # q=[['0',0],['1',1]]
        #
        # res=2
        # while q:
        #     size=len(q)
        #
        #     for s in range(size):
        #         cur=q[0]
        #         q.pop(0)
        #         if cur[0][0]=='0':
        #             add=cur[1]+pow(2,len(cur[0]))
        #             if add<=n:
        #                 res+=1
        #                 q.append(['0'+cur[0],cur[1]])
        #                 q.append(['1'+cur[0],add])
        #         else:
        #             add = cur[1] + pow(2, len(cur[0]))
        #             if add<n:
        #                 q.append(['0'+cur[0],cur[1]])
        # return res

    # def dfs(self,path,res,n):
    #     if path[1]==n:
    #         return 1
    #
    #     if len(path[0])>0 and path[0][0]=='0':
    #         add=path[1]+pow(2,len(path[0]))
    #         if add<n:
    #             res+=self.dfs(['0'+path[0],path[1]],0,n)
    #
    #             res += 1
    #             res+=self.dfs(['1'+path[0],add],0,n)
    #         elif add==n:
    #             res+=1
    #             return res
    #         else:
    #             return 0
    #     elif len(path[0])>0 and path[0][0]=='1':
    #         res+=self.dfs(['0'+path[0],path[1]],0,n)
    #
    #     else:
    #         res+=self.dfs(['0',0],0,n)
    #         if 1<=n:
    #             res+=1 if 1<n else 0
    #             res+=self.dfs(['1',1],0,n)
    #
    #     return res

if __name__ == '__main__':
    sol=Solution()
    n=3289321
    # n=5
    print(sol.findIntegers(n))