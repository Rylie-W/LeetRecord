class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        best=[float('inf') for i in arr]
        sum=0
        res=float('inf')
        bestSoFar=float('inf')
        start=0

        for i in range(len(arr)):
            sum+=arr[i]
            while sum>target:
                sum-=arr[start]
                start+=1
            if sum==target:
                if start>0:
                    res=min(res,best[start-1]+i-start+1)
                bestSoFar=min(bestSoFar,i-start+1)
            best[i]=bestSoFar

        return res if res<float('inf') else -1

if __name__ == '__main__':
    sol=Solution()
    # arr = [3, 2, 2, 4, 3]
    # target = 3
    arr = [5, 5, 4, 4, 5]
    target = 3
    print(sol.minSumOfLengths(arr,target))
