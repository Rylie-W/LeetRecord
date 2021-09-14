class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or len(word1)==0:
            return len(word2)
        if not word2 or len(word2)==0:
            return len(word1)

        l1=len(word1)
        l2=len(word2)
        dp=[[max(l1,l2) for i in word2] for i in word1]
        if word1[0]==word2[0]:
            dp[0][0]=0
        else:
            dp[0][0]=1
        for i in range(1,l1):
            dp[i][0]=dp[0][0]+i
        for i in range(1,l2):
            dp[0][i]=dp[0][0]+i

        for r in range(1,l1):
            for c in range(1,l2):
                if word1[r]==word2[c]:
                    dp[r][c]=dp[r-1][c-1]
                else:
                    dp[r][c]=min(dp[r-1][c]+1,dp[r][c-1]+1)
                    dp[r][c]=min(dp[r][c],dp[r-1][c-1]+1)
        return dp[-1][-1]

if __name__ == '__main__':
    sol=Solution()
    word1 = "sea"
    word2 = "eat"
    print(sol.minDistance(word1,word2))