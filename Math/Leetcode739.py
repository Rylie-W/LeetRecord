class Solution:
    def dailyTemperatures(self, temperatures):
            res=[0 for t in temperatures]
            q=[]
            for i,t in enumerate(temperatures):
                while q and q[-1][0]<t:
                    res[q[-1][1]]=i-q[-1][1]
                    q.pop()
                q.append([t,i])
            return res