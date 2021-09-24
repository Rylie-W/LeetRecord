class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        memo = [0 for i in envelopes]
        envelopes.sort(key=lambda a: a[0])
        res = 1
        for i in range(len(envelopes)):
            res = max(res, self.dfs(i, envelopes, memo))

        return res

    def dfs(self, pos, envelopes, memo):
        if not memo[pos] == 0:
            return memo[pos]

        res = 1
        for i in range(pos+1,len(envelopes)):
            if envelopes[i][0] > envelopes[pos][0] and envelopes[i][1] > envelopes[pos][1]:
                res = max(res, 1 + self.dfs(i, envelopes, memo))

        memo[pos] = res
        return res

if __name__ == '__main__':
    sol=Solution()
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    # envelopes = [[1, 1], [1, 1], [1, 1]]
    print(sol.maxEnvelopes(envelopes))
