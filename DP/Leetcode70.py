class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [1, 1]
        for i in range(2, n+1):
            dp[i % 2] = dp[0] + dp[1]

        return dp[n % 2]

if __name__ == '__main__':
    sol=Solution()
    sol.climbStairs(2)