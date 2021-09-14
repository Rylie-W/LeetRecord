class Solution:
    def minSwaps(self, s: str) -> int:
        dp=[[-1 for i in s+"a"] for i in s+"a"]
        for i in range(len(s)):
            dp[i][i]=0
            if i+1<len(s) and s[i]=='[' and s[i+1]==']':
                dp[i][i+2]=0
            if i+1<len(s) and s[i]==']' and s[i+1]=='[':
                dp[i][i+2]=1
        for i in range(len(s)-2,-1,-1):
            for j in range(i+3,len(s)):
                dp[i][j]=min()

    def dfs(self,s,start,end):
        if start==end:
            return 0
