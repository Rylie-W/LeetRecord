class Solution:
    def orangesRotting(self, grid) -> int:
        q=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                if grid[i][j]==2:
                    q.append((i,j))
        if count==0:
            return 0
        depth=0
        direction=[[-1,0],[0,-1],[0,1],[1,0]]
        while q:
            size=len(q)
            for i in range(size):
                p=q[0]
                q.pop(0)
                for d in direction:
                    nx=p[0]+d[0]
                    ny=p[1]+d[1]
                    if nx>-1 and nx<len(grid) and ny>-1 and ny<len(grid[0]) and grid[nx][ny]==1:
                        count-=1
                        grid[nx][ny]=2
                        q.append([nx,ny])

            depth+=1
            if count == 0:
                return depth

        return -1 if count>0 else depth
if __name__ == '__main__':
    sol=Solution()
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(sol.orangesRotting(grid))


