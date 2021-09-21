class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # left=-1
        right=0
        res=0
        count=0
        while right<len(nums):
            if count==0:
                while nums[right]==0:
                    right+=1
                    if right==len(nums):
                        return res
                # left=right
                count+=1
                right+=1

            # if nums[left]==1:
            else:
                c=nums[right]
                right+=1
                if c==1:
                    count+=1
                else:
                    count=0
                    # left=-1
            res = max(res, count)
        return res

if __name__ == '__main__':
    sol=Solution()
    nums = [1, 1, 0, 1, 1, 1]
    # nums = [1, 0, 1, 1, 0, 1]
    # nums=[1]
    print(sol.findMaxConsecutiveOnes(nums))
