class Solution:
    def addOperators(self, num: str, target: int):
        res=[]
        def dfs(idx=0,path='',value=0,prev=None):
            if idx==len(num) and value==target:
                res.append(path)
                return

            for i in range(idx+1,len(num)+1):
                if i==idx+1 or num[idx]!='0':
                    if prev is None:
                        dfs(i,num[idx:i],int(num[idx:i]),int(num[idx:i]))
                    else:
                        dfs(i,path+'+'+num[idx:i],value+int(num[idx:i]),int(num[idx:i]))
                        dfs(i,path+'-'+num[idx:i],value-int(num[idx:i]),-int(num[idx:i]))
                        dfs(i,path+'*'+num[idx:i],value-prev+prev*int(num[idx:i]),prev*int(num[idx:i]))
        dfs()
        return res


if __name__ == '__main__':
    sol=Solution()
    # num = "123"
    # target = 6
    # num = "232"
    # target = 8
    num = "00"
    target = 0
    print(sol.addOperators(num,target))
