class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp=[[1,1] for i in nums]
        res=[1,1]
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    if dp[j][0]+1>dp[i][0]:
                        dp[i]=[dp[j][0]+1,dp[j][1]]
                    elif dp[j][0]+1==dp[i][0]:
                        dp[i][1]+=dp[j][1]
            if dp[i][0]>res[0]:
                res=dp[i].copy()
            elif dp[i][0]==res[0]:
                res[1]+=dp[i][1]
        return res[1]
if __name__ == '__main__':
    sol=Solution()
    # nums=[1,2,4,3,5,4,7,2]
    # nums = [1, 3, 5, 4, 7]
    nums = [2, 2, 2, 2, 2]
    print(sol.findNumberOfLIS(nums))
