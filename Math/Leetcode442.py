class Solution:
    def findDuplicates(self, nums) :
        res=[]
        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                res.append(abs(num))
            else:
                nums[index]*=-1
        return res

if __name__ == '__main__':
    sol=Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDuplicates(nums))