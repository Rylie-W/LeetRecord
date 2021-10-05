class Solution:
    '''
    #dfs. Time limit exceeded.
    def searchMatrix(self, matrix, target: int) -> bool:
        return self.dfs(0, 0, matrix, target)

    def dfs(self, x, y, matrix, target):
        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1 or (not matrix[x][y] and matrix[x][y] != 0):
            return False
        if matrix[x][y] == target:
            return True

        if target > matrix[x][y]:
            matrix[x][y] = False
            return self.dfs(x + 1, y, matrix, target) or self.dfs(x, y + 1, matrix, target)
        else:
            matrix[x][y] = False
            return self.dfs(x - 1, y, matrix, target) or self.dfs(x, y - 1, matrix, target)
    '''

    def searchMatrix(self, matrix, target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        row=0
        col=len(matrix[0])-1
        while col>-1 and row<len(matrix):
            if matrix[row][col]==target:
                return True
            if target<matrix[row][col]:
                col-=1
            else:
                row+=1
        return False