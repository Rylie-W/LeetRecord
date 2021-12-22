from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res=[]
        d=deque()
        for i,n in enumerate(nums):
            while d and d[-1]<n:
                d.pop()
            d.append(n)
            if i-k>-2:
                if i-k>-1 and d[0] == nums[i - k]:
                    d.popleft()
                res.append(d[0])
        return res

if __name__ == '__main__':
    s=Solution()
    nums=[1, 3, -1, -3, 5, 3, 6, 7]
    k=3
    print(s.maxSlidingWindow(nums,k))
