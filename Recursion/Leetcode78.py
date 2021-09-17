class Solution:
    def subsets(self, nums):
        # res=[[]]
        # self.dfs([],res,nums)
        # return res
        return self.recurse(nums)

    # def dfs(self,path,res,nums):
    #     for n in nums:
    #         if n not in path:
    #             res.append(path+[n])
    #             if len(path)+1<len(nums):
    #                 self.dfs(path+[n],res,nums)
    #     return
    def recurse(self,nums):
        if len(nums)==0:
            return [[]]
        res=self.recurse(nums[:-1])
        temp=[]
        for r in res:
            temp.append(r+[nums[-1]])
        return res+temp

if __name__ == '__main__':
    sol=Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums))