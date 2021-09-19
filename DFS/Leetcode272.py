class Solution:
    def addOperators(self, num: str, target: int):
        memo=dict()
        self.dfs(num,target,memo)
        return memo[(target,len(num))] if memo.get((target,len(num)),-1)!=-1 else []

    def dfs(self,num,target,memo):
        if memo.get((target,len(num)),-1)!=-1:
            return memo[(target,len(num))]

        if len(num)==1:
            if int(num)==target:
                memo[(target,1)]=[num]
                return [num]
            else:
                return None

        if len(num)>0:
            temp=[]
            if num==str(target):
                temp.append(num)
            for i in range(1,len(num)):
                t1=self.dfs(num[:i],target-int(num[i:]),memo)
                if not t1 is None:
                    for t in t1:
                        temp.append(t+"+"+num[i:])

                t2=self.dfs(num[:i],target+int(num[i:]),memo)
                if not t2 is None:
                    for t in t2:
                        temp.append(t+"-"+num[i:])

                # t3 =self.dfs(num[:i],target/int(num[i:]),memo) if target/int(num[i:])==target//int(num[i:]) else None
                t3 = []
                if i==1:
                    if int(num[0])==target/int(num[i:]):
                        t3.append(num[0]+'*'+num[i:])
                if i>1:
                    for j in range(1,i):
                        # t4=self.dfs(num[:i-j],target/(int(num[i:])*int(num[i-j:i])),memo) if target/(int(num[i:])*int(num[i-j:i]))==target//((int(num[i:])*int(num[i-j:i])) else None
                        t4=self.dfs(num[:i-j],target-(int(num[i:])*int(num[i-j:i])),memo)
                        if not t4 is None:
                            for t in t4:
                                t3.append(t+'+'+num[i-j:i]+'*'+num[i:])
                        t4=self.dfs(num[:i-j],target+(int(num[i:])*int(num[i-j:i])),memo)

            memo[(target,len(num))]=temp
            return temp

if __name__ == '__main__':
    sol=Solution()
    # num = "123"
    # target = 6
    num = "232"
    target = 8
    print(sol.addOperators(num,target))
