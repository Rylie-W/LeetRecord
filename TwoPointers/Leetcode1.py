class Solution:
    def twoSum(self, nums, target: int):
        memo=dict()

        for i in range(len(nums)):
            s=target-nums[i]
            if memo.get(target-nums[i]) or memo.get(target-nums[i])==0:
                return [memo[target-nums[i]],i]

            memo[nums[i]]=i

        return False
if __name__ == '__main__':
    sol=Solution()
    nums = [2, 7, 11, 15]
    target = 9
    # nums=[3, 2, 4]
    # target=6
    print(sol.twoSum(nums,target))
