class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[-1 for i in s] for i in s]
        l=len(s)
        for i in range(l):
            dp[i][i]=True
            if i+1<l:
                if s[i]==s[i+1]:
                    dp[i][i+1]=True
                else:
                    dp[i][i+1]=False

        def getDp(start,end):
            if dp[start][end]!=-1:
                return dp[start][end]
            if start==end or start==end-1:
                return dp[start][end]

            if s[start]==s[end]:
                dp[start][end]= getDp(start+1,end-1)
                return dp[start][end]
            else:
                dp[start][end]=False
                return False

        res=s[0]
        for i in range(l):
            for j in range(i,l):
                getDp(i,j)
                if dp[i][j] and j-i+1>len(res):
                    res=s[i:j+1] if j<l-1 else s[i:]
        return res

if __name__ == '__main__':
    sol=Solution()
    # s = "cbbd"
    s = "babad"
    print(sol.longestPalindrome(s))


