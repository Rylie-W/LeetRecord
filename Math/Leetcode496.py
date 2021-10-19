class Solution:
    def nextGreaterElement(self, nums1, nums2):
        memo=dict()
        s=[]
        for i in nums2:
            while len(s)>0 and s[-1]<i:
                memo[s.pop()]=i
            s.append(i)

        for i in range(len(nums1)):
            nums1[i]=memo.get(nums1[i],-1)

        return nums1

if __name__ == '__main__':
    sol=Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(sol.nextGreaterElement(nums1,nums2))
