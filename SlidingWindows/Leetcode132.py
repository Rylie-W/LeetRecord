class Solution:
    def minCut(self, s: str) -> int:
        dp=self.isPal(s)
        return self.bfs(s,dp)

    def isPal(self,s):
        dp=[[False for i in s] for i in s]
        for i in range(len(s)):
            dp[i][i]=True
            if i+1<len(s):
                dp[i][i+1]=True if s[i]==s[i+1] else False

        for i in range(len(s)):
            for j in range(1,min(i+1,len(s)-i)):
                # if j==1:
                #     dp[i][i+j]=True if s[i]==s[i+j] else False
                #     dp[i-j][i] = True if s[i] == s[i - j] else False
                # else:
                if i-j>-1 and i+j<len(s):
                    dp[i-j][i+j]= True if s[i-j]==s[i+j] and dp[i-j+1][i+j-1] else False
                if i-j>-1 and i+j+1<len(s):
                    dp[i-j][i+j+1]=True if s[i-j]==s[i+1+j] and dp[i-j+1][i+j] else False
        return dp

    def bfs(self,s,dp):
        q=list()
        depth=1
        for i in range(len(dp[0])):
            if dp[0][i]:
                if i==len(s)-1:
                    return 0
                q.append(i+1)
        while q:
            size=len(q)

            for i in range(size):
                c=q[0]
                q.pop(0)

                for index in range(len(dp[c])):
                    if dp[c][index]:
                        if index==len(s)-1:
                            return depth
                        q.append(index+1)
            depth+=1
        return depth


if __name__ == '__main__':
    sol=Solution()
    # s='aammbbc'
    # s='bb'
    s="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    print(sol.minCut(s))