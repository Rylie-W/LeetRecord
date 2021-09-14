class Solution:
    def threeSumClosest(self, target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
    # def threeSumClosest(self, nums, target: int) -> int:
    #     nums.sort()
    #     return self.bfs(nums,target)
    #
    # def bfs(self,nums,target):
    #     q=list()
    #     res = None
    #     for i,num in enumerate(nums):
    #         q.append([[i],num])
    #         # if diff> q[-1][-1]:
    #         #     res=q[-1][-2]
    #         #     diff=q[-1][-1]
    #     depth=1
    #
    #     while depth<3:
    #         size=len(q)
    #         for i in range(size):
    #             cur=q[0]
    #             q.pop(0)
    #             for j in range(cur[0][-1]+1,len(nums)):
    #                 if j not in cur[0]:
    #                     if depth==2:
    #                         res=cur[1]+nums[j] if res==None or abs(target-res)>abs(target-(cur[1]+nums[j])) else res
    #                         if res==target:
    #                             return res
    #                     else:
    #                         q.append([cur[0]+[j],cur[1]+nums[j]])
    #         depth+=1
    #     return res

if __name__ == '__main__':
    sol=Solution()
    # nums = [-1, 2, 1, -4]
    # target = 1
    # nums=[-1, 0, 1, 2, -1, -4]
    # target=0
    nums=[84, 49, -47, -56, 13, -3, 62, -95, 23, 38, -97, 92, 34, 68, 30, 90, 41, 24, -58, 83, 96, -99, -40, 28, -18, -69,
     -78, 95, -62, 45, -66, -71, 5, 94, -42, -66, 27, 60, -90, -62, 87, -22, 56, 7, -11, 75, 53, -16, -7, -19, 17, 18,
     -14, 43, 98, -11, 0, 80, -82, 40, 5, 37, -94, -14, -62, -82, 84, 23, -9, -68, 37, -23, 10, 26, -22, -52, 14, 18,
     -40, -74, -32, 47, -87, -81, -68, 34, 60, 75, 93, -28, 100, -42, 0, -87, 60, 75, -47, 7, -57, -61, -2, -96, -18,
     -98, -3, 25, 38, -83, 60, -12, -62, 78, -41, 75, -5, 89, -97, -1, 87, 92, 57, 93, -83, -67, -76, 28, -98, -12, 22,
     -2, 54, -67, 7, 99, 100, 50, 5, 84, 49, -96, -61, -62, -61, 29, -59, 43, 55, 30, -10, -22, 50, -32, -81, -42, 32,
     55, -94, 84, -90, -71, -10, 61, 56, 94, 51, 8, 54, 22, 22, 31]
    target=82
    print(sol.threeSumClosest(nums,target))


