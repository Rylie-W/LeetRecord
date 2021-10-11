class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # leftbi=bin(left)[2:]
        # rightbi=bin(right)[2:]
        # if len(leftbi)<len(rightbi):
        #     return 0
        # l=[i for i in leftbi]
        # count=0
        # flag=False
        # for i in range(len(l)-1,-1 ,-1):
        #     if l[i]=='1':
        #         temp=pow(2,len(l)-i)
        #         t=temp/2
        #         while temp<left:
        #             temp*=2
        #         temp=min(temp,left+t)
        #         if not flag and temp>right:
        #             flag=True
        #             count+=t
        #         elif flag==True:
        #             count+=pow(2,len(l)-1-i)
        # return int(count)
        if left==0:
            return 0
        moveFactor=1
        while left!=right:
            left>>=1
            right>>=1
            moveFactor<<=1
        return left*moveFactor

if __name__ == '__main__':
    sol=Solution()
    left = 5
    right = 7
    # left = 1
    # right = 2147483647
    print(sol.rangeBitwiseAnd(left,right))
