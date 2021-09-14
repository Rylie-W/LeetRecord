class Solution:
    def isValidSudoku(self, board) -> bool:
        def isOK(x, y, cur):
            for i in range(len(board[0])):
                if i!=y and board[x][i] == cur:
                    return False
            for i in range(len(board)):
                if i!=x and board[i][y] == cur:
                    return False

            for i in range(x - 2, x + 3):
                for j in range(y - 2, y + 3):
                    if i > -1 and i < len(board) and j > -1 and j < len(board[0]):
                        if i!=x and j!=y and board[i][j] == cur:
                            return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    if not isOK(i,j,board[i][j]):
                        return False
        return True
        # return self.dfs(0,0,board)
    def dfs(self,x,y,board):
        def isOK(x, y, cur):
            for i in board[x]:
                if i == cur:
                    return False
            for i in range(len(board)):
                if board[i][y] == cur:
                    return False

            for i in range(x - 2, x + 3):
                for j in range(y - 2, y + 3):
                    if i > -1 and i < len(board) and j > -1 and j < len(board[0]):
                        if board[i][j] == cur:
                            return False
            return True

        def nextIndex(x,y):
            if y==len(board[0])-1:
                return x+1,0
            return x,y+1

        if x==len(board)-1 and y==len(board[0])-1:
            for i in range(1,10):
                if isOK(x,y,str(i)):
                    return True
            return False

        nx, ny = nextIndex(x, y)
        if board[x][y]!='.':
            return self.dfs(nx,ny,board)

        for i in range(1,10):
            if isOK(x,y,str(i)):
                board[x][y]=str(i)
                if self.dfs(nx,ny,board):
                    return True
                board[x][y]="."

        return False

if __name__ == '__main__':
    sol=Solution()
    board =[["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # board=[["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    #  ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    #  ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    #  ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    #  ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    #  ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    #  ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    #  ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    #  ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]


    print(sol.isValidSudoku(board))






