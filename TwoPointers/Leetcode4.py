class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1=l2=0
        r1=len(nums1)-1
        r2=len(nums2)-1

        m1=l1+int((r1-l1)/2)
        m2 = l2 + int((r2 - l2) / 2)
        if nums1[m1]<nums2[m2]:
