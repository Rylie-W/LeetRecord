class Solution:
    def minStartValue(self, nums) -> int:
        if len(nums)<1:
            return 1
        pre=nums[0]
        minVal=pre
        for i in range(1,len(nums)):
            cur=pre+nums[i]
            minVal=min(cur,minVal)
            pre=cur

        return -minVal+1 if minVal<=0 else 1
