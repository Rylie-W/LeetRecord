class Solution:
    def reachableNodes(self, edges, maxMoves: int, n: int) -> int:
        dp=[0,0]*len(edges)
        edges.sort(key=lambda a: (a[0],a[1],a[2]))
        if edges[0][0]!=0:
            return 1
        res=1
        def dfs(index,steps,res):
            if steps<=edges[index][-1]:
                res+=steps