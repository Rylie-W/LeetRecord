class Solution:
    def rectangleArea(self, rectangles) -> int:
        def findRC():
            row=column=0
            for rec in rectangles:
                row=max(row,rec[3])
                column=max(column,rec[2])
            return row,column

        row,column=findRC()
        modulo=pow(10,9) + 7
        map=[[False for i in range(column)] for i in range(row)]

        res=0
        for rec in rectangles:
            for i in range(rec[0],rec[2]):
                for j in range(rec[1],rec[3]):
                    c=i
                    r=row-1-j
                    if not map[r][c]:
                        map[r][c]=True
                        res+=1
        return res%modulo

if __name__ == '__main__':
    sol=Solution()
    # rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    rectangles = [[0, 0, 1000000000, 1000000000]]
    print(sol.rectangleArea(rectangles))
