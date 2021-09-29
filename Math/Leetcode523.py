class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        dp={0:[-1]}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sum%=k
            if dp.get(sum) is not None:
                for j in dp[sum]:
                    if i-j>1:
                        return True
            dp[sum]=[i] if dp.get(sum) is None else dp[sum]+[i]
        return False

if __name__ == '__main__':
    sol=Solution()
    # nums = [23, 2, 4, 6, 7]
    # k = 6
    # nums = [23, 2, 6, 4, 7]
    # k = 6
    # nums=[0]
    # k=1
    # nums=[1]
    # k=1
    nums=[5, 0, 0, 0]
    k=3
    print(sol.checkSubarraySum(nums,k))