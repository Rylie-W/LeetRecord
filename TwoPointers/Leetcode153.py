class Solution:
    def findMin(self, nums) -> int:
        left=0
        right=len(nums)-1
        if nums[left]<nums[right]:
            return nums[left]
        while left<=right:
            if left==right:
                return nums[left]
            if left==right-1:
                return min(nums[left],nums[right])
            mid=int((left+right)/2)
            if nums[mid]>nums[left]:
                left=mid
            if nums[mid]<nums[right]:
                right=mid

if __name__ == '__main__':
    sol=Solution()
    nums = [3, 4, 5, 1, 2]
    print(sol.findMin(nums))