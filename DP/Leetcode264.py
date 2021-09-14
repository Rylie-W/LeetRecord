class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        res=[1]
        t2,t3,t5=0,0,0
        while len(res)<n:
            cur=min(res[t2]*2,res[t3]*3,res[t5]*5)
            if cur==res[t2]*2:
                t2+=1
            elif cur==res[t3]*3:
                t3+=1
            else:
                t5+=1
            if cur in res:
                continue
            res.append(cur)
        return res[-1]

if __name__ == '__main__':
    sol=Solution()
    sol.nthUglyNumber(10)