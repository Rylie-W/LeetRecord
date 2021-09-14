class Solution:
    def removeBoxes(self, boxes) -> int:
        return self.bfs(boxes)

    def bfs(self,boxes):
        q=list()
        cboxes=list()
        start=0
        while start!=len(boxes)-1:
            temp=self.move(boxes,start)
            q.append(pow(temp-start,2))
            cbox=boxes[:start]+boxes[temp:]
            cboxes.append(cbox)
            start=temp
        res=0

        while q:
            size=len(q)
            for s in range(size):
                c=q[0]
                box=cboxes[0]
                q.pop(0)
                cboxes.pop(0)

                if len(box)==0:
                    res=max(res,c)
                    continue

                start=0
                if  len(box)==1:
                    q.append(c+1)
                    cboxes.append([])
                    continue
                while start!=len(box)-1:
                    temp=self.move(box,start)
                    q.append(c+pow(temp-start,2))
                    cbox=box[:start]+box[temp:]
                    cboxes.append(cbox)
                    start=temp

        return res

    def move(self,cboxes,start):
        for i in range(start,len(cboxes)):
            if cboxes[i]!=cboxes[start]:
                return i

        return i

if __name__ == '__main__':
    sol=Solution()
    boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    print(sol.removeBoxes(boxes))