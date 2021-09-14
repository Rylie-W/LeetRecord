class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        res=1
        memo=[[0 for i in matrix[0]] for i in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res=max(res,self.dfs(i,j,[],matrix,memo))

        return res

    def dfs(self,x,y,path,matirx,memo):
        #exit case
        if x<0 or x>len(matirx)-1 or y<0 or y>len(matirx[0])-1 or matirx[x][y]<=matirx[path[-1][0]][path[-1][1]] if len(path)>0 else False:
            return 0

        if not memo[x][y]==0:
            return memo[x][y]

        directions=[[-1,0],[0,-1],[0,1],[1,0]]
        res=0
        for d in directions:
            nx=x+d[0]
            ny=y+d[1]
            if [nx,ny] not in path:
                res=max(res,1+self.dfs(nx,ny,path+[[x,y]],matirx,memo))
        memo[x][y]=res
        return res

if __name__ == '__main__':
    sol=Solution()
    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    matrix=[[3,4,5],[3,2,6],[2,2,1]]
    memo = [[0 for i in matrix[0]] for i in matrix]
    # matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    print(sol.longestIncreasingPath(matrix))
    print(sol.dfs(2,1,[],matrix,memo))
