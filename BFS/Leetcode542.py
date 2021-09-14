class Solution:
    direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    def updateMatrix(self, mat):
        res=[[0 for i in mat[0]] for i in mat]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[i][j]=self.bfs(i,j,mat,min(res[i-1][j] if i >0 else float('inf'),res[i][j-1]if j >0 else float('inf'))+1)
        return res

    def bfs(self, x, y, mat,limit):
        q = [[x,y]]
        visited=set()
        visited.add(str(x)+str(y))
        depth=0

        while q:
            size=len(q)
            for i in range(size):
                cur=q[0]
                q.pop(0)

                if mat[cur[0]][cur[1]]==0:
                    return depth

                for d in self.direction:
                    nx=cur[0]+d[0]
                    ny=cur[1]+d[1]
                    if nx>-1 and nx<len(mat) and ny>-1 and ny<len(mat[0]) and str(nx)+str(ny) not in visited:
                        q.append([nx,ny])
                        visited.add(str(nx)+str(ny))
            depth+=1
            if depth>=limit:
                return limit

        return float('inf')

if __name__ == '__main__':
    sol=Solution()
    mat = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]
    print(sol.updateMatrix(mat))

