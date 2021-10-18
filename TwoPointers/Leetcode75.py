class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        while right>=left:
            if nums[left]>nums[right]:
            