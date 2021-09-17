import collections
class Solution:
    def intersect(self, nums1, nums2):
        nums1=collections.Counter(nums1)
        nums2=collections.Counter(nums2)
        res=[]
        for k1 in nums1.keys():
            if nums2.get(k1,-1)!=-1:
                res+=[k1]*min(nums1[k1],nums2[k1])
        return res

if __name__ == '__main__':
    sol=Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(sol.intersect(nums1,nums2))