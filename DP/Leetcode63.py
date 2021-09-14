class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        dp=list()
        for i in range(col):
            if i>0:
                if dp[i-1]==1 and obstacleGrid[0][i]==0:
                    dp.append(1)
                else:
                    dp.append(0)
            else :
                if obstacleGrid[0][i]==0:
                    dp.append(1)
                else:
                    dp.append(0)
        for r in range(1,row):
            for c in range(col):
                if obstacleGrid[r][c]==0:
                    if c>0:
                        dp[c]=dp[c]+dp[c-1]
                else:
                    dp[c]=0

        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))