class Solution:
    def tictactoe(self, moves) -> str:
        dp=[[' 'for i  in range(3)] for i in range(3)]
        def win(x,y):
            def diagonal():
                if x==0 and y==0:
                    if dp[1][1]==dp[x][y] and dp[2][2]==dp[x][y]:
                        return True
                if x==0 and y==2:
                    if dp[1][1]==dp[x][y] and dp[2][0]==dp[x][y]:
                        return True
                if x==1 and y==1:
                    if (dp[0][0]==dp[x][y] and dp[2][2]==dp[x][y]) or (dp[2][0]==dp[x][y] and dp[0][2]==dp[x][y]):
                        return True
                if x==2 and y==0:
                    if dp[1][1]==dp[x][y] and dp[0][2]==dp[x][y]:
                        return True
                if x==2 and y==2:
                    if dp[1][1]==dp[x][y] and dp[0][0]==dp[x][y]:
                        return True
                return False
            if all(dp[x][i]==dp[x][y] for i in range(3)) or all(dp[i][y]==dp[x][y] for i in range(3)) or diagonal():
                return True

            return False

        count=0
        for x,y in moves:
            if count%2==0:
                dp[x][y]='X'
                if win(x,y):
                    return 'A'
            else:
                dp[x][y]='O'
                if win(x,y):
                    return 'B'
            count+=1

        return 'Pending' if count<9 else 'Draw'

if __name__ == '__main__':
    sol=Solution()
    # moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    # moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    # moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    moves = [[0, 0], [1, 1]]
    print(sol.tictactoe(moves))