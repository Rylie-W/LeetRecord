class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mark= 0 if matrix[0][0]==0 else 3
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

                    if j==0:
                        mark=self.determineMark(mark,1)
                    if i==0:
                        mark=self.determineMark(mark,0)

        for i in range(1,len(matrix[0])):
            if matrix[0][i]==0:
                self.fillZeros(None,i,matrix)
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                self.fillZeros(i,None,matrix)

        if mark==0:
            self.fillZeros(None,0,matrix)
            self.fillZeros(0,None,matrix)
        if mark==1:
            self.fillZeros(0, None, matrix)
        if mark==2:
            self.fillZeros(None, 0, matrix)
        return matrix

    def determineMark(self,mark,index):
        if mark==0:
            return 0

        if mark==1 :
            if index == 1:
                return 0
            else:
                return 1

        if mark==2:
            if index==0:
                return 0
            else:
                return 2

        if index==0:
            return 1
        else:
            return 2

    def fillZeros(self,x,y,matrix):
        if x!=None:
            for i in range(len(matrix[0])):
                matrix[x][i]=0

        if y!=None:
            for i in range(len(matrix)):
                matrix[i][y]=0

if __name__ == '__main__':
    sol=Solution()
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

    print(sol.setZeroes(matrix))