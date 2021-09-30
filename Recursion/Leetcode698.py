class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        count=dict()
        each=0
        for i in nums:
            each+=i
            count[i]=1 if count.get(i) is None else count[i]+1

        if each%k!=0:
            return False

        each=each/k
        for key in count.keys():
            if key>each:
                return False

        def isOK(count,target):
            if count.get(target) is not None and count[target]!=0:
                count[target]-=1
                return True

            keys=list(count.keys())
            keys.sort(reverse=True)
            for key in keys:
                if target-key>0 and count[key]!=0:
                    count[key]-=1
                    if isOK(count,target-key):
                        return True
                    else:
                        count[key]+=1
            return False

        for i in range(k):
            if not isOK(count,each):
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    # nums = [4, 3, 2, 3, 5, 2, 1]
    # k = 4
    # nums = [1, 2, 3, 4]
    # k = 3
    # nums=[1, 1, 1, 1, 2, 2, 2, 2]
    # k=2
    # nums=[12, 1, 2, 3, 18, 2, 5, 2, 11, 1]
    # k=3
    # nums=[2, 11, 1, 10, 4, 10, 1, 4, 2]
    # k=3
    # nums=[3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269]
    # k=5
    nums=[85, 35, 40, 64, 86, 45, 63, 16, 5364, 110, 5653, 97, 95]
    k=7
    print(sol.canPartitionKSubsets(nums,k))
