class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in s] for i in p]
        for i in range(len(s)):
            if p[0] == '.' and i == 0:
                dp[0][0] = True
            elif p[0] == s[0]:
                dp[0][0] = True

        for i in range(1, len(p)):
            if p[i] == '*':
                dp[i][0] = dp[i - 1][0]

        pre = s[0]

        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == '*' and s[j] == pre:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    pre = s[j]
                elif p[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    sol=Solution()
    
    # s = "aab"
    # p = "c*a*b"
    # s="mississippi"
    # p="mis*is*p*."
    print(sol.isMatch(s,p))