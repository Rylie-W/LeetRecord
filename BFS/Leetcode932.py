class Solution:
    def beautifulArray(self, n: int):
        return self.bfs(n)
    def bfs(self,n):
        if n==1:
            return [1]
        q=[[i] for i in range(1,n+1)]
        nums=[i for i in range(n)]
        # visited=[[0 for j in range(i)] + [1] +[0 for j in range()] for i in range(n)]
        next=[nums[:i]+nums[i+1:] if i<n-1 else nums[:i] for i in range(n)]
        depth=1
        while q:
            size=len(q)
            for i in range(size):
                cur=q[0]
                q.pop(0)
                cnext=next[0]
                next.pop(0)

                for j in range(len(cnext)):
                    if self.isOK(cnext[j]+1,cur):
                        if depth==n-1:
                            return cur+[cnext[j]+1]
                        q.append(cur+[cnext[j]+1])
                        next.append(cnext[:j]+cnext[j+1:] if j <len(cnext)-1 else cnext[:j])
            depth+=1
        return list()

    def isOK(self,new,nums):
        # for i in range(len(nums)):
        #     for k in range(i,len(nums)):
        #         if 2*nums[k]==nums[i]+new:
        #             return False
        # return True
        for i in range(len(nums)):
            target=(nums[i]+new)/2
            if target%1!=0:
                continue
            if i<len(nums)-1 and self.findK(nums[i+1:],target):
                return False
        return True

    def findK(self,nums,k):
        if len(nums)==0:
            return False
        nums.sort()
        if k > nums[-1] or k<nums[0]:
            return False
        left=0
        right=len(nums)-1
        while left<=right:
            mid=int(left+(right-left)/2)
            if nums[mid]==k:
                return True
            elif nums[mid]<k:
                left=mid+1
            else:
                right=mid-1
        return False

if __name__ == '__main__':
    sol=Solution()
    n=100
    print(sol.beautifulArray(n))