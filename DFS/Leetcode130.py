class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[[-1,0],[0,-1],[0,1],[1,0]]
        # def dfs(cur,path,flip,count):
        #     flip=flip if not flip else not (cur[0]==0 or cur[0]==len(board)-1 or cur[1]==0 or cur[1]==len(board[0])-1)
        #     for d in directions:
        #         nx=cur[0]+d[0]
        #         ny=cur[1]+d[1]
        #         if nx>-1 and nx<len(board) and ny>-1 and ny<len(board[0])-1 and (nx,ny) not in path and board[nx][ny]=='O':
        #             path.add((nx,ny))
        #             flip=dfs([nx,ny],path,flip,count+1) if flip else flip
        #     if flip and count==1:
        #         for p in path:
        #             board[p[0]][p[1]]='X'
        #     return flip
        def dfs(x,y):
            board[x][y]='Z'
            for d in directions:
                nx=x+d[0]
                ny=y+d[1]
                if nx>-1 and nx<len(board) and ny>-1 and ny<len(board[0]) and board[nx][ny]=='O':
                    dfs(nx,ny)

        for i in [0,len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    dfs(i,j)
        for i in [0,len(board[0])-1]:
            for j in range(len(board)):
                if board[j][i]=='O':
                    dfs(j,i)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]='O' if board[i][j]=='Z' else 'X'
        return board


if __name__ == '__main__':
    sol=Solution()
    board=[["X","O","X"],["O","X","O"],["X","O","X"]]
    print(sol.solve(board))