class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        dp = [[""]]

        for i in range(1, n + 1):
            cur = list()
            for j in range(i):
                for p1 in dp[j]:
                    for p2 in dp[i - j - 1]:
                        cur.append("(" + p1 + ")" + p2)
            dp.append(cur)

        return dp[-1]

if __name__ == '__main__':
    sol=Solution()
    n=4
    print(sol.generateParenthesis(n))