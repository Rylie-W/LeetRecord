class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        #dfs
        res=set()
        self.dfs("",s,t,res)
        return len(res)

    def dfs(self,path,s,t,res):
        if self.lenOfPath(path)==len(t):
            res.add(path)
            return

        cur=self.lenOfPath(path)
        start=self.generateStart(path)+1 if cur>0 else 0
        for i in range(start,len(s)):
            if s[i]==t[cur]:
                self.dfs(path+str(i)+'.',s,t,res)

    def lenOfPath(self,path):
        if len(path)==0:
            return 0
        length=0
        for i in path:
            if i =='.':
                length+=1
        return length

    def generateStart(self,path):
        start=0
        for i in range(len(path)-2,-1,-1):
            if path[i]=='.':
                return start
            start+=int(path[i])*10**(len(path)-i-2)
            if i==0:
                return start
    '''

        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for col in range(len(dp[0])):
            dp[0][col] = 1
        for x in range(1, len(s) + 1):
            for y in range(1, len(t) + 1):
                if s[x - 1] == t[y - 1]:
                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]
                else:
                    dp[y][x] = dp[y][x - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    sol=Solution()
    s ="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    t ="bddabdcae"
    # s = "babgbag"
    # t = "bag"
    print(sol.numDistinct(s,t))