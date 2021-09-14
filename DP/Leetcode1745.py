class Solution:
    '''#bfs
        def checkPartitioning(self, s: str):
            return self.bfs(s)

        def bfs(self, s):
            q = list()
            for i in range(1, len(s) + 1):
                if self.isPal(s[:i]):
                    q.append(i)
            depth = 1
            while depth < 3:
                size = len(q)
                for i in range(size):
                    cur = q[0]
                    q.pop(0)

                    # exit case
                    if depth == 2 and self.isPal(s[cur:]):
                        return True

                    for j in range(cur + 1, len(s) + 1):
                        if self.isPal(s[cur:j]):
                            q.append(j)
                depth += 1

            return False

        def isPal(self, s):
            if not s or len(s)==0:
                return False
            return s == s[::-1]'''

    # dp
    def checkPartitioning(self, s: str):
        dp = [[False for i in s] for i in s]

        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if j + 1 < i - 1:
                        dp[j][i] = dp[j + 1][i - 1]
                    else:
                        dp[j][i] = True

        for i in range(1, len(s) - 1):
            for j in range(i + 1, len(s)):
                if dp[0][i-1] and dp[i][j-1] and dp[j][len(s) - 1]:
                    return True
        return False


if __name__ == '__main__':
    sol=Solution()
    s="abcbdd"
    # s="acab"
    print(sol.checkPartitioning(s))