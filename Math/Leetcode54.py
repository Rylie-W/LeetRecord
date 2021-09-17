class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==1:
            return matrix[0]
        if len(matrix[0])==1:
            return [x[0] for x in matrix]
        res=[]
        direction='left'
        x,y=0,0
        # count=0
        # while count<len(matrix)*len(matrix[0]):
        while x>-1 and x<len(matrix) and y>-1 and y<len(matrix[0]) and not matrix[x][y] is None:
            if direction=='left':
                while y<len(matrix[0]) and not matrix[x][y]is None:
                    res.append(matrix[x][y])
                    matrix[x][y]=None
                    y+=1
                x+=1
                y-=1
                direction='down'
            elif direction=='down':
                while x<len(matrix) and not matrix[x][y] is None:
                    res.append(matrix[x][y])
                    matrix[x][y] = None
                    x += 1
                x -= 1
                y-=1
                direction = 'right'
            elif direction=='right':
                while y>-1 and not matrix[x][y] is None:
                    res.append(matrix[x][y])
                    matrix[x][y] = None
                    y -= 1
                x-= 1
                y+=1
                direction = 'up'
            else:
                while x>-1 and not matrix[x][y] is None:
                    res.append(matrix[x][y])
                    matrix[x][y] = None
                    x -= 1
                x+= 1
                y+=1
                direction = 'left'
        return res

        # left=0
        # right=len(matrix[0])-1
        # up=1
        # down=len(matrix)-2
        # res=[]
        # direction='left'
        # x=0
        # y=right
        # end=set()
        # while len(end)!=2:
        #     if direction=='left':
        #         for i in range(left,right+1):
        #             res.append(matrix[x][i])
        #         right-=1
        #         if right<left:
        #             end.add("x")
        #         x=down+1
        #         direction='down'
        #     elif direction=='right':
        #         for i in range(right,left-1,-1):
        #             res.append(matrix[x][i])
        #         left+=1
        #         if right<left:
        #             end.add("x")
        #         x=up
        #         direction='up'
        #     elif direction=='down':
        #         for i in range(up,down+1):
        #             res.append(matrix[i][y])
        #         up+=1
        #         if up>down:
        #             end.add("y")
        #         y=left
        #         direction='right'
        #     else:
        #         for i in range(down,up-1,-1):
        #             res.append(matrix[i][y])
        #         down-=1
        #         if up>down:
        #             end.add("y")
        #         y=right
        #         direction='left'
        # return res

if __name__ == '__main__':
    sol=Solution()
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))
