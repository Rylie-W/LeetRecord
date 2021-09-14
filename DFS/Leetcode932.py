class Solution:
    def beautifulArray(self, n: int):
        return self.dfs([],[i for i in range(1,n+1)])
    def dfs(self,track,nums):
        if not nums or len(nums)==0:
            return track

        res=None
        for i in range(len(nums)):
            if self.isOK(nums[i],track):
                res=self.dfs(track+[nums[i]],nums[:i]+nums[i+1:] if i<len(nums)-1 else nums[:i])
                if res!=None:
                    return res
        return res

    def isOK(self,new,nums):
        for i in range(len(nums)):
            for k in range(i,len(nums)):
                if 2*nums[k]==nums[i]+new:
                    return False
        return True

if __name__ == '__main__':
    sol=Solution()
    n=4
    print(sol.beautifulArray(n))