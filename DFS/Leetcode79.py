class Solution:
    def exist(self, board, word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    board[i][j]=-1
                    if self.dfs(1,i,j,board,word):
                        return True
                    else:
                        board[i][j]=word[0]
        return False

    def dfs(self,pos,x,y,board,word):
        #exit
        if pos==len(word):
            return True

        direc=[[-1,0],[0,-1],[0,1],[1,0]]
        for d in direc:
            nx=x+d[0]
            ny=y+d[1]
            if nx>-1 and nx<len(board) and ny>-1 and ny<len(board[0]) and board[nx][ny]==word[pos]:
                board[nx][ny]=-1
                if self.dfs(pos+1,nx,ny,board,word):
                    return True
                else:
                    board[nx][ny]=word[pos]
        return False

if __name__ == '__main__':
    sol=Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "SEE"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    print(sol.exist(board,word))