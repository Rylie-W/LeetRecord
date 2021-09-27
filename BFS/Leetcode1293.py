class Solution:
    def shortestPath(self, grid, k: int) -> int:
        q=[[0,0,k]]
        visited={(0,0,0)}
        res=0
        direction=[[-1,0],[0,-1],[0,1],[1,0]]
        while q:
            size=len(q)
            for s in range(size):
                cur=q[0]
                q.pop(0)
                if (cur[0],cur[1])==(len(grid)-1,len(grid[0])-1):
                    return res
                for ax,ay in direction:
                    nx=cur[0]+ax
                    ny=cur[1]+ay
                    nadd=cur[2]
                    if nx>-1 and nx<len(grid) and ny>-1 and ny<len(grid[0]):
                        if grid[nx][ny]==1:
                            nadd-=1
                        if nadd>= 0 and (nx,ny,nadd) not in visited:
                            visited.add((nx,ny,nadd))
                        # if (nx,ny) not in visited:
                        #     if grid[nx][ny]==0:
                            q.append([nx,ny,nadd])
                        #     elif cur[2]>0:
                        #         q.append([nx,ny,cur[2]-1])
                        #     visited.add((nx,ny))
            res+=1
        return  -1

if __name__ == '__main__':
    sol=Solution()
    # grid =[[0, 0, 0],
    #  [1, 1, 0],
    #  [0, 0, 0],
    #  [0, 1, 1],
    #  [0, 0, 0]]
    # k = 1
    # grid =[[0, 1, 1],
    #  [1, 1, 1],
    #  [1, 0, 0]]
    # k = 1
    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    k=1
    # 5374 9520 5899 9878 0266
    print(sol.shortestPath(grid,k))
