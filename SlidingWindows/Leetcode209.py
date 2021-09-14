class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        res=len(nums)+1
        left=right=0
        sum=0
        while right<len(nums):
            sum+=nums[right]
            right+=1

            if sum>=target:
                while sum>=target:
                    sum-=nums[left]
                    left+=1
                res = min(res, right - left+1)
        return res if res<len(nums)+1 else 0

if __name__ == '__main__':
    sol=Solution()
    # target = 7
    # nums = [2, 3, 1, 2, 4, 3]
    # target = 4
    # nums = [1, 4, 4]
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(sol
          .minSubArrayLen(target,nums))
