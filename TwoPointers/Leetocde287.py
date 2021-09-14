class Solution:
    def findDuplicate(self, nums) -> int:
        memo=[0 for i in range(10)]

        for i in nums:
            memo[i]+=1
            if memo[i]==2:
                return i
        return

if __name__ == '__main__':
    sol=Solution()
    nums = [3, 1, 3, 4, 2]
    print(sol.findDuplicate(nums))