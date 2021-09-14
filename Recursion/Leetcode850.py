class Solution:
    def rectangleArea(self, rectangles) -> int:
        modulo=pow(10,9) + 7
        memo=list()
        for rec in rectangles:
            self.addRec(memo,0,rec)

        res=0
        for rec in memo:
            res+=((rec[2]-rec[0])*(rec[3]-rec[1]))
            res=res%modulo

        return res


    def addRec(self,memo,start,cur):
        if start>=len(memo):
            memo.append(cur)
            return

        rec=memo[start]
        if cur[2]<=rec[0] or cur[0]>=rec[2] or cur[3]<=rec[1] or cur[1]>=rec[3]:
            self.addRec(memo,start+1,cur)
            return

        if cur[0]<rec[0]:
            self.addRec(memo,start+1,[cur[0],cur[1],rec[0],cur[3]])

        if cur[2]>rec[2]:
            self.addRec(memo,start+1,[rec[2],cur[1],cur[2],cur[3]])

        if cur[3]>rec[3]:
            self.addRec(memo,start+1,[max(rec[0],cur[0]),rec[3],min(rec[2],cur[2]),cur[3]])
        if cur[1]<rec[1]:
            self.addRec(memo,start+1,[max(rec[0],cur[0]),cur[1],min(rec[2],cur[2]),rec[1]])

        return

if __name__ == '__main__':
    sol=Solution()
    # rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    # rectangles = [[0, 0, 1000000000, 1000000000]]
    # rectangles=[[0, 0, 1, 1], [2, 2, 3, 3]]
    rectangles=[[41,59,61,89],[49,83,95,98],[32,9,43,66]]
    print(sol.rectangleArea(rectangles))