class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not len(s3)==len(s1)+len(s2):
            return False
        dp=[[False for i in range(len(s2)+1)] for i in range(len(s1)+1)]
        dp[0][0]=True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=(s3[j-1]==s2[j-1] and dp[i][j-1])
                elif j==0:
                    dp[i][j]=(s3[i-1]==s1[i-1] and dp[i-1][j])
                else:
                    dp[i][j]=(s3[i+j-1]==s1[i-1] and dp[i-1][j])or(s3[i+j-1]==s2[j-1] and dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    sol=Solution()
    s1="aabcc"
    s2="dbbca"
    s3="aadbbbaccc"
    sol.isInterleave(s1,s2,s3)