class Solution:
    def islandPerimeter(self, grid) -> int:
        res=0
        direction=[[-1,0],[0,-1],[0,1],[1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    for x,y in direction:
                        nx=i+x
                        ny=j+y
                        if nx<0 or nx>len(grid)-1 or ny<0 or ny>len(grid[0])-1 or(nx>-1 and nx<len(grid) and ny>-1 and ny<len(grid[0]) and grid[nx][ny]==0):
                            res+=1

        return res

if __name__ == '__main__':
    sol=Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(sol.islandPerimeter(grid))