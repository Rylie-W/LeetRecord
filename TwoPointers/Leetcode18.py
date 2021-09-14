class Solution:
    def fourSum(self, nums, target: int):
        res=set()
        nums.sort()

        for i in range(len(nums)):
            t1=target-nums[i]
            # if (i<len(nums)-1 and t1<nums[i+1] ) or t1>nums[-1]:
            #     continue
            for j in range(i+1,len(nums)):
                t2=t1-nums[j]
                # if (j<len(nums)-1 and t2<nums[j+1]) or t2>nums[-1]:
                #     continue
                for k in range(j+1,len(nums)):
                    t3=t2-nums[k]
                    if (k<len(nums)-1 and t3<nums[k+1]) or t3>nums[-1]:
                        continue
                    l=self.findK(nums,k+1,t3)
                    if l or l==0:
                        res.add((nums[i],nums[j],nums[k],l))
        res=list(res)
        for r in range(len(res)):
            c=res[0]
            res.pop(0)
            res.append(list(c))

        return res



    def findK(self,nums,start,target):
        left=start
        right=len(nums)-1
        while right>=left:
            mid=int(left+(right-left)/2)
            if nums[mid]==target:
                return target
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return None

if __name__ == '__main__':
    sol=Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    # nums = [2, 2, 2, 2, 2]
    # target = 8
    # nums=[0, 0, 0, 0]
    # target=0
    print(sol.fourSum(nums,target))

