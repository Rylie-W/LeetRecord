class Solution:
    def subarraySum(self, nums, k: int) -> int:
        res=0
        memo={0:1}
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if memo.get((sum-k)) is not None:
                res+=memo[sum-k]
            memo[sum]=1 if memo.get(sum) is None else memo[sum]+1
        return res

if __name__ == '__main__':
    sol=Solution()
    # nums = [1, 1, 1]
    # k = 2
    # nums = [1, 2, 3]
    # k = 3
    # nums=[1]
    # k=1
    # nums=[-1, -1, 1]
    # k=0
    nums=[1, -1, 0]
    k=0
    print(sol.subarraySum(nums,k))