class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return self.dfs(0,0,matrix,target)
    def dfs(self,x,y,matrix,target):
        if x<0 or x>len(matrix)-1 or y<0 or y>len(matrix[0])-1 or (not matrix[x][y] and matrix[x][y]!=0):
            return False
        if matrix[x][y]==target:
            return True

        if target>matrix[x][y]:
            matrix[x][y]=False
            return self.dfs(x+1,y,matrix,target) or self.dfs(x,y+1,matrix,target)
        else:
            matrix[x][y]=False
            return self.dfs(x - 1, y, matrix,target) or self.dfs(x, y - 1, matrix,target)

if __name__ == '__main__':
    sol=Solution()
    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
    #           [18, 21, 23, 26, 30]]
    # target = 5
    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
    #                  [18, 21, 23, 26, 30]]
    # target = 20
    matrix=[[0, 0, 0], [2, 7, 9], [7, 8, 11]]
    target=7

    print(sol.searchMatrix(matrix,target))