class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        pre=dict()
        def convertPre():
            for c,p in prerequisites:
                if pre.get(c) is not None:
                    pre[c].append(p)
                else:
                    pre[c]=[p]
        convertPre()
        res=list(set(i for i in range(numCourses))-set(pre.keys()))
        mark=[False for i in range(numCourses)]
        for i in res:
            mark[i]=True
        new_len=len(res)
        while new_len>0:
            temp=len(res)
            for i,c in enumerate(mark):
                if not c and all(mark[j] for j in pre[i]):
                    res.append(i)
                    mark[i]=True
            new_len=len(res)-temp

        return res if len(res)==numCourses else []





if __name__ == '__main__':
    sol=Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(sol.findOrder(numCourses,prerequisites))