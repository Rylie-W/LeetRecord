class Solution:
    def partition(self, s: str):
        res = list()

        def dfs(res, track, dp, pos, s):
            if pos == len(s):
                res.append(track)
                return

            for i in range(pos, len(s)):
                if dp[pos][i]:
                    track.append(s[pos:i])
                    dfs(res, track, dp, i + 1, s)
                    track.pop()

        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j] and (i - j <= 2 or s[i + 1][j - 1]):
                    dp[i][j] = True

        track = list()
        dfs(res, track, dp, 0, s)
        return res

if __name__ == '__main__':
    sol=Solution()
    sol.partition("aab")