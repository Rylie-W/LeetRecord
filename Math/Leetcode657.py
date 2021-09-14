class Solution:
    def outerTrees(self, trees):
        h=dict()
        w=dict()
        wmin=wmax=hmin=hmax=-1
        for tree in trees:
            if h.get(tree[1],-1)==-1:
                h[tree[1]] = [tuple(tree)]
            else:
                h[tree[1]].append(tuple(tree))
            if w.get(tree[0],-1)==-1:
                w[tree[0]] = [tuple(tree)]
            else:
                w[tree[0]].append(tuple(tree))

            wmin=tree[0] if wmin==-1 else min(wmin,tree[0])
            wmax=tree[0] if wmax==-1 else max(wmax,tree[0])
            hmin=tree[1] if hmin==-1 else min(hmin,tree[1])
            hmax=tree[1] if hmax==-1 else max(hmax,tree[1])

        res=list(set(h[hmin]+h[hmax]+w[wmin]+w[wmax]))
        for i in range(len(res)):
            res[i]=list(res[i])
        return res

if __name__ == '__main__':
    sol=Solution()
    points = [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
    print(sol.outerTrees(points))
