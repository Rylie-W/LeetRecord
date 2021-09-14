class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # dp=list()
        c0=0
        c1=0
        for i in s:
            # dp.append(0)
            if i =='1':
                c1+=1
            else: c0+=1

        # dp[-1]=c1-1 if s[-1]=='1' else c1+1
        # dp[0]=c0
        pre=c1-1 if s[-1]=='1' else c1+1
        res=len(s)
        for i in range(len(s)-2,0,-1):
            if s[i]=='1':
                cur=pre-1
            else:
                cur=pre+1
            res=min(res,cur)
            pre=cur

        return min(min(res,c1),min(c0,c1-1 if s[-1]=='1' else c1+1))


if __name__ == '__main__':
    sol=Solution()
    # s = "00011000"
    s="010110"
    print(sol.minFlipsMonoIncr(s))