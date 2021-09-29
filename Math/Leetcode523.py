class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        dp=[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum!=0 and sum%k==0:
                return True
            for j in range(i):
                if (sum-dp[j])%k==0:
                    return True
            dp.append(sum)
        return False

if __name__ == '__main__':
    sol=Solution()
    # nums = [23, 2, 4, 6, 7]
    # k = 6
    # nums = [23, 2, 6, 4, 7]
    # k = 6
    nums=[0]
    k=1
    print(sol.checkSubarraySum(nums,k))