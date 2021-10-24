class Solution:
    def findMin(self, nums) -> int:
        left=0
        right=len(nums)-1

        while right>=left:
            mid=int(left+(right-left)/2)
            if nums[mid]>nums[left]:
                left=mid+1
            elif nums[mid]<=nums[right]:
                right=mid-1
        return min(nums[left],nums[right])