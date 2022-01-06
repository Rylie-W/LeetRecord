class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i,n in enumerate(nums):
            if n!=i+1:
                nums[i]=nums[n-1]
                nums[n-1]=n
                i-=1
        for i,n in enumerate(nums):
            if n!=i+1:
                return i+1
