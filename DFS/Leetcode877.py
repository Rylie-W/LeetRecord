class Solution:
    def stoneGame(self, piles) -> bool:
        return self.dfs([0,0],piles,0)

    def dfs(self, path, nums,pos):
        if len(nums) == 0:
            return path[0] > path[1]
        if nums[0]>nums[-1]:
            path[pos]+=nums[0]
            pos = 1 if pos == 0 else 0
            return self.dfs(path,nums[1:],pos)
        elif nums[0]<nums[-1]:
            path[pos]+=nums[-1]
            pos = 1 if pos == 0 else 0
            return self.dfs(path, nums[:-1], pos)
        else:
            path[pos]+=nums[0]
            pos=1 if pos==0 else 0
            if len(nums)>2:
                if max(nums[1],nums[-1])>max(nums[0],nums[-2]):
                    return self.dfs(path,nums[:-1],pos)
                elif max(nums[1],nums[-1])<max(nums[0],nums[-2]):
                    return self.dfs(path, nums[1:], pos)
                else:
                    return self.dfs(path,nums[:-1],pos) or self.dfs(path, nums[1:], pos)
            return self.dfs(path,nums[:-1],pos)

        # if nums[0]>=nums[-1] and nums[1]>=nums[-1]:
        #     return self.dfs([path[0] + nums[0], path[1] + nums[1]], nums[2:] if len(nums) > 2 else [])
        #
        # if nums[0]>=nums[-1] and nums[-1]>=nums[1]:
        #     return self.dfs([path[0] + nums[0], path[1] + nums[-1]], nums[1:len(nums) - 1] if len(nums) > 2 else [])
        #
        # if nums[0]<=nums[-1] and nums[0]>=nums[-2]:
        #     return self.dfs([path[0] + nums[-1], path[1] + nums[0]], nums[1:len(nums) - 1] if len(nums) > 2 else [])
        #
        # else:
        #     return self.dfs([path[0]+nums[-1],path[1]+nums[-2]], nums[:-2] if len(nums) > 2 else [])

if __name__ == '__main__':
    sol=Solution()
    # piles = [5, 3, 4, 5]
    # piles=[3, 7, 2, 3]
    # piles=[4, 3, 4, 3, 2, 5]
    piles=[3, 2, 10, 4]
    print(sol.stoneGame(piles))
