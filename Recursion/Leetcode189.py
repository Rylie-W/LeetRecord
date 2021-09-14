class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.recurse(nums,k%len(nums))

    def recurse(self,nums,k):
        if k==1:
            temp=nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=temp
            return nums

        return self.recurse(self.recurse(nums,1),k-1)

if __name__ == '__main__':
    sol=Solution()
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    nums=[-1, -100, 3, 99]
    k=2
    print(sol.rotate(nums,k))