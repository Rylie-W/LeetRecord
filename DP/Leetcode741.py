class Solution:
    def cherryPickup(self, grid) -> int:
        res=list()
        self.dfs([[0,1],[1,0]],[0,0],res,0,grid,True)
        if len(res)==0:
            return 0
        return max(res)
    def dfs(self,dir,cur,res,count,grid,turnover):
        row=len(grid)
        col=len(grid[0])
        #end case
        if row==1 and col==1:
            if grid[0][0]==1:
                res.append(1)
            return
        if cur==[0,0] and not turnover:
            res.append(count)
            return

        if cur[0]>-1 and cur[0]<row and cur[1]>-1 and cur[1]<col and grid[cur[0]][cur[1]]>=0:
            if grid[cur[0]][cur[1]]==1:
                count+=1
            temp=count
            cur_val=grid[cur[0]][cur[0]]
            grid[cur[0]][cur[1]]=2

            if cur==[row-1,col-1]:
                dir=[[0,-1],[-1,0]]
                turnover=False

            for d in dir:
                nr=cur[0]+d[0]
                nc=cur[1]+d[1]
                self.dfs(dir,[nr,nc],res,count,grid,turnover)
                count=temp

            grid[cur[0]][cur[1]]=cur_val

if __name__ == '__main__':
    sol=Solution()
    # grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    grid=[[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
    print(sol.cherryPickup(grid))


