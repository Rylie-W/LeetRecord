class Solution:
    def rob(self, nums) -> int:
        return max(self.helper(nums, 0, len(nums) - 2), self.helper(nums, 1, len(nums) - 1))

    def helper(self, nums, start, end):
        include = 0
        exclude = 0
        for i in range(start, end + 1):
            i = exclude

            i = nums[i] + i
            exclude = max(exclude, include)
            include = i
        return max(exclude, include)