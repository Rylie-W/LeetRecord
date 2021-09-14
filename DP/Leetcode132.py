class Solution:
    def minCut(self, s: str) -> int:
        return self.bfs(s)

    def bfs(self, s):
        if self.isPal(s):
            return 0

        q = list()
        visited = set()
        depth = 1
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                q.append(i)
                visited.add(i)
        while q:
            size = len(q)
            for i in range(size):
                cur = q[0]
                q.pop(0)
                # exit case
                if self.isPal(s[cur:]):
                    return depth

                for j in range(cur + 1, len(s) + 1):
                    if self.isPal(s[cur:j]) and not j in visited:
                        q.append(j)
                        visited.add(j)
            depth+=1

    def isPal(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    sol=Solution()
    s="aabc"
    print(sol.bfs(s))