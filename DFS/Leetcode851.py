class Solution:
    def loudAndRich(self, richer, quiet):
        # def findRicher(richer,start,memo):
        #     rich=set()
        #     for r in richer:
        #         if r[1]==start and r[0] not in memo:
        #             rich.add(r[0])
        #             memo.add(r[0])
        #     for r in rich:
        #         findRicher(richer,r,memo)
        #
        # def findQuietest(quiet,rich):
        #     res=-1
        #     for r in rich:
        #         if res==-1:
        #             res=r
        #         else:
        #             if quiet[r]<quiet[res]:
        #                 res=r
        #     return res
        #
        # res=[]
        #
        # for i in range(len(quiet)):
        #     memo={i}
        #     findRicher(richer,i,memo)
        #     res.append(findQuietest(quiet,memo))
        # return res
        def dfs(richer, quiet, start, path, memo):
            res = start
            for r in richer:
                if r[1] == start and r[0] not in path:
                    path.add(r[0])
                    if memo.get(r[0], -1) == -1:
                        temp = dfs(richer, quiet, r[0], path, memo)
                        memo[r[0]] = temp
                    else:
                        temp = memo[r[0]]
                    if quiet[temp] < quiet[res]:
                        res = temp
            memo[start] = res
            return res

        res = []
        memo = dict()
        for i in range(len(quiet)):
            if memo.get(i, -1) == -1:
                res.append(dfs(richer, quiet, i, {i}, memo))
            else:
                res.append(memo[i])
        return res


if __name__ == '__main__':
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    # richer = []
    # quiet = [0]
    print(sol.loudAndRich(richer, quiet))
