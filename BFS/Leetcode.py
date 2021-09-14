class Solution:
    def subsetsWithDup(self, nums):
        # if len(nums)==0:
        #     return set(tuple())
        #
        # res=set()
        # temp=self.subsetsWithDup(nums[:-1])
        # for t in temp:
        #     res.add()
        #
        # return res
        res=list()
        nums.sort()
        self.dfs([],res,nums)
        return res
    def dfs(self,path,res,nums):
        res.append(path)

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.dfs(path+[nums[i]],res,nums[i+1:])

if __name__ == '__main__':
    sol=Solution()
    nums=[4,4,4,1,4]
    print(sol.subsetsWithDup(nums))

