class Solution:
    def orderOfLargestPlusSign(self, n, mines) -> int:
        #     def generateDir(res):
        #         direc=[[0,0] for i in range(4)]
        #         direc[0][0] -= (res+1)
        #         direc[1][1] -= (res+1)
        #         direc[2][1] += (res+1)
        #         direc[3][0] += (res+1)
        #         return direc
        #
        #     dp=[[-1 for i in range(n)] for i in range(n)]
        #     for m in range(len(mines)):
        #         mines[m]=(mines[m][0],mines[m][1])
        #     mines=set(mines)
        #     res=0
        #
        #     for i in range(n):
        #         for j in range(n):
        #             if (i,j) in mines:
        #                 dp[i][j]=0
        #             else:
        #                 if not (i-1>-1 and j-1>-1 and dp[i-1][j]>0 and dp[i][j-1]>0):
        #                     dp[i][j]=self.getOrder(i,j,mines,n,1,generateDir(0))
        #                 else:
        #                     temp=min(dp[i-1][j],dp[i][j-1])-1
        #                     dp[i][j]=self.getOrder(i,j,mines,n,temp,generateDir(temp-1))
        #                 # dp[i][j]=self.getOrder(i,j,mines,n,1,generateDir(0))
        #                 res=max(res,dp[i][j])
        #     return res
        #
        #
        # def getOrder(self,x,y,mines,n,res,direc):
        #     while True:
        #         if all(x+d[0]>-1 and x+d[0]<n and y+d[1]>-1 and y+d[1]<n and (x+d[0],y+d[1]) not in mines for d in direc):
        #             res+=1
        #             direc[0][0]-=1
        #             direc[1][1]-=1
        #             direc[2][1]+=1
        #             direc[3][0]+=1
        #         else:
        #             return res
        dp = [[1 for i in range(n)] for i in range(n)]
        for m in mines:
            dp[m[0]][m[1]] = 0
        res = 0

        for i in range(n):
            for j in range(n):
                if dp[i][j] != 0:
                    count = 1
                    # left
                    k = 1
                    while j - k > -1 and dp[i][j - k] > 0:
                        count += 1
                        k += 1
                    dp[i][j] = count
                    count = 1
                    k = 1
                    # right
                    while j + k < n and dp[i][j + k] > 0:
                        count += 1
                        k += 1
                    dp[i][j] = min(dp[i][j], count)
                    # up
                    count = 1
                    k = 1
                    while i - k > -1 and dp[i - k][j] > 0:
                        count += 1
                        k += 1
                    dp[i][j] = min(dp[i][j], count)
                    # down
                    count = 1
                    k = 1
                    while i + k < n and dp[i + k][j] > 0:
                        count += 1
                        k += 1
                    dp[i][j] = min(dp[i][j], count)
                    res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    sol = Solution()
    # n = 5
    # mines = [[4, 2]]
    # n=0
    # mines=[[0,0]]
    # n = 10
    # mines = [[1, 2], [1, 8], [2, 4], [4, 7], [5, 0], [5, 6], [6, 4], [6, 9]]
    n=5
    mines=[[0, 0], [0, 3], [1, 1], [1, 4], [2, 3], [3, 0], [4, 2]]
    print(sol.orderOfLargestPlusSign(n, mines))
