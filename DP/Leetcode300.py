class Solution:
    def lengthOfLIS(self, nums) -> int:
        # dp=[0 for  i in range(len(nums))]
        # res=1
        # dp[0]=1
        # for i in range(1,len(nums)):
        #     if nums[i]>nums[i-1]:
        #         dp[i]=dp[i-1]+1
        #     else:
        #         dp[i]=1
        #     res=max(res,dp[i])
        # return res
        dp = [[] for i in nums]
        res = 1
        dp[0] = [nums[0]]
        for i in range(1, len(nums)):
            res = max(res, self.dfs([], nums[:i + 1], res))
        return res

    def dfs(self,track, nums, res):
        if not nums or len(nums) == 0:
            res = max(res, len(track))
            return res

        for i in range(0, len(nums) - 1):
            if i < nums[-1]:
                track.append(i)
                self.dfs(track, nums[:i], res)
                track.pop()

if __name__ == '__main__':
    sol=Solution()
    sol.lengthOfLIS([10,9,2,5,3,7,101,18])