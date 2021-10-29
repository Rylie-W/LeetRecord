import collections
class Solution:
    def threeSum(self, nums):
        nums=list(set(nums))
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                return res
            for j in range(i+1,len(nums)):
                temp=-nums[i]-nums[j]
                if temp!=nums[i] and temp!=nums[j] and temp in nums:
                    res.append([nums[i],nums[j],-nums[i]-nums[j]])
        return res

if __name__ == '__main__':
    sol=Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))


