class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[0 for x in range(m)]
        for i in range(m):
            dp[i]=1
        for i in range(1,n):
            for j in range(1,m):
                dp[j]=dp[j]+dp[j-1]
        return dp[m-1]
        '''
        if m < 1 or n < 1:
            return 0
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        '''

if __name__ == '__main__':
    sol=Solution()
    m=23
    n=12
    #193536720
    print(sol.uniquePaths(m,n))