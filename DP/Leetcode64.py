class Solution:
    def minPathSum(self, grid) -> int:
        dp=list()
        row = len(grid)
        col = len(grid[0])

        for i in range(col):
            if i>0:
                dp.append(grid[0][i]+dp[-1])
            else:
                dp.append(grid[0][i])


        for r in range(1,row):
            for c in range(col):
                if c>0:
                    dp[c]=min(dp[c],dp[c-1])+grid[r][c]
                else:
                    dp[c]=dp[c]+grid[r][c]

        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(grid))
