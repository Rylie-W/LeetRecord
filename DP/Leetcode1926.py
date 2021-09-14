class Solution:
    # def accessibleDirection(pos,maze):
    #     res=[]
    #     direc=[[0,-1],[-1,0],[1,0],[0,1]]
    #     for d in direc:
    #         if maze[pos[0]+d[0]][pos[1]+d[1]]==".":
    #             res.append([pos[0]+d[0],pos[1]+d[1]])
    #     return res

    def nearestExit(self, maze, entrance) -> int:
        q = [entrance]
        visited = {tuple(entrance): 1}
        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                cur = q[0]
                # exit
                if (cur[0] == 0 or cur[1] == 0 or cur[0]==len(maze)-1 or cur[1]==len(maze[0])-1) and not cur == entrance:
                    return depth
                direc = [[0, -1], [-1, 0], [1, 0], [0, 1]]
                for d in direc:
                    if cur[0] + d[0]>-1 and cur[0] + d[0]<len(maze) and cur[1] + d[1]>-1 and cur[1] + d[1]<len(maze[0]):
                        if maze[cur[0] + d[0]][cur[1] + d[1]] == "." and not visited.get((cur[0] + d[0], cur[1] + d[1])):
                            visited[(cur[0] + d[0], cur[1] + d[1])] = 1
                            q.append([cur[0] + d[0], cur[1] + d[1]])
                q.pop(0)
            depth += 1
        return -1



if __name__ == '__main__':
    sol=Solution()
    maze=[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance=[1,2]
    sol.nearestExit(maze,entrance)