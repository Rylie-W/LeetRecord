class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        if l1 == 0 or l2 == 0:
            return str1 if not len(str1)==0 else str2
        dp = [[list() for i in range(l2)] for i in range(l1)]

        if str1[0] == str2[0]:
            dp[0][0] =[[0,0]]
        for i in range(1, l2):
            if len(dp[0][0]) >0:
                dp[0][i] = [[0, 0]]
            elif len(dp[0][i-1])>0:
                dp[0][i]=dp[0][i-1]
            elif str2[i] == str1[0]:
                dp[0][i] = [[0,i]]

        for i in range(1, l1):
            if str1[i] == str2[0] or dp[0][0]==1 or dp[i-1][0]==1:
                dp[i][0] = 1
            if len(dp[0][0]) >0:
                dp[i][0] = [[0, 0]]
            elif len(dp[i-1][0])>0:
                dp[i][0]=dp[i-1][0]
            elif str1[i] == str2[0]:
                dp[i][0] = [[i,0]]

        for i in range(1, l1):
            for j in range(1, l2):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i - 1][j - 1]+[[i,j]]
                else:
                    # dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                    dp[i][j]=dp[i][j-1] if len(dp[i][j-1])==max(len(dp[i][j-1]),len(dp[i-1][j])) else dp[i-1][j]

        if len(dp[-1][-1])==0:
            return str1+str2
        res=""
        pre=[0,0]
        for sub in dp[-1][-1]:
            res+=str1[pre[0]:sub[0]]
            res+=str2[pre[1]:sub[1]]
            res+=str1[sub[0]]
            pre=[sub[0]+1,sub[1]+1]

        if pre[0]<l1:
            res+=str1[pre[0]:]
        if pre[1]<l2:
            res+=str2[pre[1]:]

        return res

if __name__ == '__main__':
    sol=Solution()
    str1 = "abac"
    str2 = "cab"
    print(sol.shortestCommonSupersequence(str1,str2))
