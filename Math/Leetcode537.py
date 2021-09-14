class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=self.str2list(num1)
        num2=self.str2list(num2)
        res=[0,0]
        res[0]=num1[0]*num2[0]-num1[1]*num2[1]
        res[1]=num1[0]*num2[1]+num1[1]*num2[0]

        return str(res[0])+'+'+str(res[1])+'i'

    def str2list(self,s):
        res=[0,0]
        first=0
        if s[0]=='-':
            i=1
            nega=True
        else:
            i=0
            nega=False
        while i<len(s) and s[i]>='0' and s[i]<='9':
            first=first*10+int(s[i])
            i+=1
        # if i==len(s):
        #     res[0]=first if not nega else -first
        #     return res
        # if s[i]=='i':
        #     res[1]=first if not nega else -first
        #     return res

        res[0]=first if not nega else -first
        i += 1
        if s[i]=='-':
            i+=1
            nega=True
        else:
            nega=False
        first=0
        while i<len(s) and s[i]>='0' and s[i]<='9':
            first=first*10+int(s[i])
            i+=1

        res[1]=first if not nega else -first
        return res

if __name__ == '__main__':
    sol=Solution()
    num1 = "1+1i"
    num2 = "1+1i"
    print(sol.complexNumberMultiply(num1,num2))



