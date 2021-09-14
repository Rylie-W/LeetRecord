import collections
class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        nums.sort()

        def combination(n,r):
            if n==r:
                return 1
            res=1
            for i in range(r+1,n+1):
                res*=i
            for i in range(r,0,-1):
                res/=i
            return res

        if nums[-1]-nums[0] and len(nums)>2:
            res=0
            for i in range(3,len(nums)+1):
                res+=combination(len(nums),i)
            return res

        mark=collections.Counter(nums)
        res=0
        nums=list(mark.keys())
        memo=[[0 for i in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                memo[i][j]=nums[i]-nums[j]

                if mark[nums[i]]>2:
                    for k in range(3,mark[nums[i]]+1):
                        res+=combination(mark[nums[i]],k)


