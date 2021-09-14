class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        memo=sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp=dict()
        res=memo[-1][-1]
        for i in range(len(memo)-1,-1,-1):
            temp=0
            if dp.get(memo[i][0], -1) != -1:
                temp=dp[memo[i][0]]
            dp[memo[i][0]]=memo[i][2]
            keys=list(dp.keys())
            keys.sort(reverse=True)
            for key in keys:
                if key>=memo[i][1]:
                    dp[memo[i][0]]=max(dp[memo[i][0]],dp[key]+memo[i][-1])
                else:
                    dp[memo[i][0]]=max(dp[memo[i][0]],dp[key])
            dp[memo[i][0]]=max(dp[memo[i][0]],temp)
            res=max(res,dp[memo[i][0]])
        return res

if __name__ == '__main__':
    sol=Solution()
    # startTime = [1, 2, 3, 4, 6]
    # endTime = [3, 5, 10, 6, 9]
    # profit = [20, 20, 100, 70, 60]
    # startTime = [1, 1, 1]
    # endTime = [2, 3, 4]
    # profit = [5, 6, 4]
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(sol.jobScheduling(startTime,endTime,profit))
