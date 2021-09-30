class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        if len(nums)==0:
            return -1
        memo=dict()
        res=float('inf')
        for i in range(len(nums)):
            memo[(i,i+1)]=nums[i]
            if memo[(i,i+1)]>=k:
                res=1
                return res
            for j in range(i):
                temp=nums[i]+memo[(j,i)]
                if temp>=k:
                    res=min(res,i-j+1)
                memo[(j,i+1)]=temp
        return res if res<float("inf") else -1
if __name__ == '__main__':
    sol=Solution()
    # nums = [1, 2]
    # k = 4
    # nums = [2, -1, 2]
    # k = 3
    nums=[84, -37, 32, 40, 95]
    k=167
    print(sol.shortestSubarray(nums,k))