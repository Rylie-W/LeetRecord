class Solution:
    def uniquePathsIII(self, grid) -> int:
        start=list()
        paths=set()
        row=len(grid)
        col=len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    start.append(r)
                    start.append(c)
                if grid[r][c]==0:
                    paths.add(self.generateNext(r,c))

        res=set()
        self.dfs("",[start],start,res,grid,paths)
        return len(res)

    def dfs(self,path,visited, cur,res,grid, paths):
        row = len(grid)
        col = len(grid[0])
        if grid[cur[0]][cur[1]]==2:
            if len(paths)==0:
                res.add(path)
            return
        if grid[cur[0]][cur[1]]==-1:
            return

        steps=[[-1,0],[0,-1],[0,1],[1,0]]

        for step in steps:
            nextr=cur[0]+step[0]
            nextc=cur[1]+step[1]
            if nextr>-1 and nextr<row and nextc>-1 and nextc<col and [nextr,nextc] not in visited:
                curs=self.generateNext(nextr,nextc)
                paths.discard(curs)
                self.dfs(path+curs,visited+[[nextr,nextc]],[nextr,nextc],res,grid,paths)
                if grid[nextr][nextc]==0:
                    paths.add(curs)

    def generateNext(self,r,c):
        return "("+str(r)+","+str(c)+")"


if __name__ == '__main__':
    sol=Solution()
    # grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    grid=[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    print(sol.uniquePathsIII(grid))




