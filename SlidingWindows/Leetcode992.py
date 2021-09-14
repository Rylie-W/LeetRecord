class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        return  self.Kmost(nums,k)-self.Kmost(nums,k-1)
    def Kmost(self,nums,k):
        window=dict()
        valid=0
        right=left=0
        res=0
        while right<len(nums):
            c=nums[right]
            right+=1
            if not window.get(c):
                window[c]=1
                valid+=1
            else:
                window[c]+=1

            if valid>k:
                res+=(right-left)
            while valid>k:
                d=nums[left]
                left+=1
                window[d]-=1
                if window[d]==0:
                    valid-=1
        return res
        # res=0
        # for i in range(len(nums)):
        #     j=i
        #     windows = dict()
        #     valid = 0
        #     while j < len(nums):
        #         c=nums[j]
        #         j+=1
        #         if not windows.get(c):
        #             windows[c]=1
        #             valid+=1
        #         else:
        #             windows[c]+=1
        #
        #         if valid==k:
        #             res+=1
        #         elif valid>k:
        #             break
        # return res

if __name__ == '__main__':
    sol=Solution()
    nums = [1, 2, 1, 2, 3]
    k = 2
    # nums = [1, 2, 1, 3, 4]
    # k = 3
    # nums=[1, 2]
    # k=1
    print(sol.subarraysWithKDistinct(nums,k))
