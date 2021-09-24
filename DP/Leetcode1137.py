class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0,1,1]
        if n<3:
            return dp[n]
        for i in range(3,n+1):
            dp.append(sum(dp))
            dp.pop(0)
        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    n=25
    print(sol.tribonacci(n))