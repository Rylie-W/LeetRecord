class Solution:
    def arrayNesting(self, nums) -> int:
        res=0
        memo=set()
        for n in range(len(nums)):
            if n in memo:
                continue
            path=set()
            self.dfs(nums,n,path,memo)
            if len(path)>res:
                res=len(path)
                if res==len(nums):
                    return res
        return res


    def dfs(self,nums,index,path,memo):
        # if memo.get(index,-1)!=-1:
        #     if memo[index][-1]<len(nums) and nums[memo[index][-1]] not in path:
        #         path.update(set(memo[index]))
        #         memo[index].append(nums[memo[index][-1]])
        #         self.dfs(nums,nums[memo[index][-1]],path,memo)
        if index<len(nums) and nums[index] not in path:
            path.add(nums[index])
            # memo[index]=[nums[index]]
            memo.add(index)
            self.dfs(nums,nums[index],path,memo)

if __name__ == '__main__':
    sol=Solution()
    nums = [5, 4, 0, 3, 1, 6, 2]
    # nums = [0, 1, 2]
    print(sol.arrayNesting(nums))
