class Solution:
    def isPossible(self, nums) -> bool:

        def getDuplidate(left,right):
            while right<len(nums):
                if right==0 or (right>0 and nums[right]!=nums[right-1]):
                    right+=1
                else:
                    mark=right-1
                    while nums[right]==nums[mark]:
                        if right-mark>1:
                            return None,None,True
                        right+=1
                    if right-1-left<3:
                        return None,None,True

            return right-1,right,False

        left=right=0



