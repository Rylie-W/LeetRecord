class Solution:
    def getSkyline(self, buildings):
        points=[]
        for b in buildings:
            points.append([b[0],b[-1],'s'])
            points.append([b[1],b[-1],'e'])
        def cmp(a,b):
            if a[0]!=b[0]:
                return a[0]<b[0]
            else:
                return a[1]>b[1]
        points=sorted(points,key=cmp)
        q=[0]
        maxh=0
        res=[]
        for p in points:
            if p[-1]=='s':
                q.append(p[1])
                q.sort()
                if maxh!=q[-1]:
                    res.append(p[:2])
            if p[-1]=='e':
                q.remove(p[1])
                if maxh!=q[-1]:
                    res.append([p[0],q[-1]])

            maxh=q[-1]
        return res

if __name__ == '__main__':
    sol=Solution()
    # buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    buildings=[[0,2,3],[2,5,3]]
    print(sol.getSkyline(buildings))

